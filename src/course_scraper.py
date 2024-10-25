import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import logging
import time
import uuid
from flask_caching import Cache
from concurrent.futures import ThreadPoolExecutor

import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Course:
    id: str
    title: str
    provider: str
    detail: str
    rating: str
    category: str
    link: str

class CourseScraper:
    def __init__(self, cache):
        self.cache = cache
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/83.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
            # Add more user agents as needed
        ]
        self.headers = {
            "User-Agent": random.choice(self.user_agents)
        }

    def _make_request(self, url):
        # Check if the result is cached
        cached_result = self.cache.get(url)
        if cached_result:
            logger.info(f"Fetching {url} from cache")
            return cached_result
        
        try:
            logger.info(f"Fetching: {url}")  # Log the URL being fetched
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Raise an error for bad responses
            # Cache the result for future use
            self.cache.set(url, response.text, timeout=3600)  # Cache for 1 hour
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def _fetch_coursera_page(self, page):
        base_url = 'https://www.coursera.org/courses?query=free'
        url = f"{base_url}&page={page}&index=prod_all_launched_products_term_optimization"
        return self._make_request(url)

    def get_coursera_courses(self):
        courses_list = []
        page_numbers = range(1, 4)  # Change this range for more pages

        with ThreadPoolExecutor(max_workers=3) as executor:
            # Fetch all pages concurrently
            page_contents = list(executor.map(self._fetch_coursera_page, page_numbers))

        for page_content in page_contents:
            if page_content is None:
                continue

            soup = BeautifulSoup(page_content, "html.parser")
            courses = soup.find_all('div', class_='css-16m4c33')

            for course in courses:
                try:
                    title_element = course.find('h3', class_='cds-CommonCard-title')
                    provider_element = course.find('p', class_='cds-ProductCard-partnerNames')
                    detail_element = course.find('div', class_='cds-ProductCard-body')
                    rating_element = course.find('p', class_='css-2xargn')
                    a_tag = course.find('a', class_=lambda value: value and 'cds-CommonCard-titleLink' in value)

                    if not (title_element and provider_element and a_tag):
                        continue

                    link_href = f"https://www.coursera.org{a_tag['href']}"

                    course_data = Course(
                        id=str(uuid.uuid4()),
                        title=title_element.text.strip(),
                        provider=f"coursera / {provider_element.text.strip()}",
                        detail=detail_element.text.strip() if detail_element else 'N/A',
                        rating=rating_element.text.strip() if rating_element else 'N/A',
                        category=provider_element.text.strip(),
                        link=link_href
                    )

                    courses_list.append(vars(course_data))

                except Exception as e:
                    logger.error(f"Error parsing Coursera course: {str(e)}")
                    continue

        return courses_list

    def get_harvard_courses(self):
        course_list = []
        soup_content = self._make_request('https://pll.harvard.edu/catalog/free')

        if not soup_content:
            return course_list

        soup = BeautifulSoup(soup_content, "html.parser")
        courses = soup.find_all('div', class_='group-details')

        for course in courses: 
            try:
                title_element = course.find('div', class_='field field---extra-field-pll-extra-field-subject field--name-extra-field-pll-extra-field-subject field--type- field--label-inline clearfix')
                provider_element = course.find('h3', class_='field__item')
                course_href = provider_element.find('a')['href']

                if not (title_element and provider_element):
                    continue

                course_data = Course(
                    id=str(uuid.uuid4()),
                    title=provider_element.text.strip(),
                    provider="Harvard",
                    detail='N/A',
                    rating='N/A',
                    category=title_element.text.strip(),
                    link=f"https://pll.harvard.edu{course_href}"
                )

                course_list.append(vars(course_data))

            except Exception as e:
                logger.error(f"Error parsing Harvard course: {str(e)}")
                continue

        return course_list
