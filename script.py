from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)
CORS(app)

# Function to scrape Coursera courses
def get_coursera_courses():
    courses_list = []
    URL = 'https://www.coursera.org/courses?query=free'
    response = requests.get(URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        courses = soup.find_all('div', class_='css-16m4c33')

        for idx, course in enumerate(courses):
            title_element = course.find('h3', class_='cds-CommonCard-title')
            provider_element = course.find('p', class_='cds-ProductCard-partnerNames')
            detail_element = course.find('div', class_='cds-ProductCard-body')
            rating_element = course.find('p', class_='css-2xargn')
            # Find the relevant <a> tag
            a_tag = course.find('a', class_=lambda value: value and 'cds-CommonCard-titleLink' in value)

            if title_element and provider_element:
                title = title_element.text.strip()
                provider = provider_element.text.strip()
                rating = rating_element.text.strip() if rating_element else 'N/A'
                detail = detail_element.text.strip() if detail_element else 'N/A'

                # Extract the link from the <a> tag
                # Extract the href attribute
                link_href = 'https://www.coursera.org' + a_tag['href'] if a_tag and 'href' in a_tag.attrs else None

                course_data = {
                    "id": idx + 1,  # Incremental ID
                    "title": title,
                    "provider": "coursera / " + provider,
                    "detail": detail,
                    "rating": rating,
                    "category": "Online Course", # Default category
                    "link": link_href
                }
                courses_list.append(course_data)

    return courses_list

# Function to scrape Harvard courses
def get_harvard_courses():
    courses_list = []
    URL2 = 'https://pll.harvard.edu/catalog/free'
    response2 = requests.get(URL2)

    if response2.status_code == 200:
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        oxfords = soup2.find_all('div', class_='group-details')

        for idx, oxford in enumerate(oxfords, start=len(courses_list) + 1):  # Ensure unique ID continues
            title_element = oxford.find('div', class_='field field---extra-field-pll-extra-field-subject field--name-extra-field-pll-extra-field-subject field--type- field--label-inline clearfix')
            provider_element = oxford.find('h3', class_='field__item')

            if title_element and provider_element:
                title = title_element.text.strip()
                provider = provider_element.text.strip()

                course_data = {
                    "id": idx + 1,  # Incremental ID
                    "title": provider,
                    "provider": "Harvard",
                    "detail": 'N/A',
                    "rating": 'N/A',
                    "category": title
                }
                courses_list.append(course_data)

    return courses_list

# API endpoint to return all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    coursera_courses = get_coursera_courses()
    harvard_courses = get_harvard_courses()

    # Ensure unique IDs by offsetting the Harvard courses
    harvard_start_id = len(coursera_courses) + 1
    for idx, course in enumerate(harvard_courses):
        course["id"] = harvard_start_id + idx  # Assign new unique ID

    all_courses = coursera_courses + harvard_courses

    # Shuffle the course list to randomize order
    random.shuffle(all_courses)
    return jsonify(all_courses)

if __name__ == '__main__':
    app.run(debug=True)
