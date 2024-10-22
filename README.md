


# Free Course Hive Backend

  Welcome to the **Free Course Hive Backend!** This backend API scrapes free online courses from platforms like Coursera, Harvard, and Stanford and serves them via a RESTful API. 
  The backend is built using Flask and leverages BeautifulSoup for web scraping.


## Table of Contents

- Overview
- Features
- Technologies Used
- Installation
- Usage
- API Endpoints
- Contributing
- License


  ## Overview
  
    The Free Course Hive Backend scrapes data from different educational platforms, aggregates the courses, and serves them through a Flask API.
    It is part of the Free Course Hive project and supports the frontend by providing dynamic course content.


  ## Features

    - Scrapes free online courses from:
      - Coursera
      - Harvard University
      - Stanford University
      - More sites needed! contribute
        
   - Provides a REST API to fetch all the scraped courses.
     
   - Randomizes and serves course data, including titles, providers, ratings, and course details.
     

## Technologies Used


  - Flask for the API.
  - BeautifulSoup for web scraping.
  - Flask-CORS to allow cross-origin requests from the frontend.
  - Requests to fetch HTML content from the course websites.

## Installation

1. Clone the Repository

    First, clone the backend repository to your local machine:
   
   ```
   git clone https://github.com/yourusername/freecoursehive-backend.git
   cd freecoursehive-backend
   ```

2. Set Up Virtual Environment

   It's recommended to use a virtual environment to manage dependencies. To create and activate a virtual environment:


   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   
3. Install Dependencies

   Install the required Python packages using pip and the requirements.txt file:


   ```
   pip install -r requirements.txt

   ```

4. Run the Flask Application

   After installing the dependencies, run the Flask development server:


   ```
   python script.py
   
   ```


   By default, the app will run at `http://127.0.0.1:5000`.



## Usage

  Once the backend is running, you can fetch course data by sending a `GET` request to the `/api/courses` endpoint. 
  This will return a JSON response containing all the scraped courses.

  ### Example Request:

    ```
    GET http://127.0.0.1:5000/api/courses

    ```

## API Endpoints

  `GET /api/courses`

  - Description: Returns a list of free courses scraped from Coursera, Harvard, and Stanford.
    
  - Response: A JSON array of course objects, where each object contains the following fields:
  - id: A unique identifier for the course.
  - title: The title of the course.
  - provider: The platform providing the course (e.g., Coursera, Harvard, etc.).
  - detail: A brief detail or description of the course.
  - rating: Course rating (if available).
  - category: The category of the course.
  - link: A URL to the course.

### Example Response:


  [
    {
      "id": 1,
      "title": "Machine Learning",
      "provider": "Coursera / Stanford University",
      "detail": "Learn the foundations of machine learning...",
      "rating": "4.8",
      "category": "Online Course",
      "link": "https://www.coursera.org/learn/machine-learning"
    },
    {
      "id": 2,
      "title": "CS50's Introduction to Computer Science",
      "provider": "Harvard",
      "detail": "N/A",
      "rating": "N/A",
      "category": "Computer Science",
      "link": "https://pll.harvard.edu/course/cs50-introduction-computer-science"
    }
  ]




### Contributing

  We welcome contributions from developers of all levels! If you'd like to contribute, please follow these steps:


  - Fork the repository.
  - Create a new branch for your feature or bugfix.
  - Commit your changes and push your branch to your fork.
  - Submit a pull request for review.


  Please refer to our [CONTRIBUTING.md](https://pages.github.com/](https://github.com/freecoursehive/freecoursehive_be/blob/master/CONTRIBUTING.md)) for detailed contribution guidelines.


### License

  This project is licensed under the MIT License. See the LICENSE file for more information.

    


  

