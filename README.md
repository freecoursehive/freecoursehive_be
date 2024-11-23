# Free Course Hive Backend

Welcome to the **Free Course Hive Backend!** This backend API scrapes free online courses from platforms like Coursera, Harvard, and Stanford and serves them via a RESTful API. 
The backend is built using Flask and leverages BeautifulSoup for web scraping.

## Table of Contents

- Overview
- Features
- Technologies Used
- Installation
  - Traditional Setup
  - Docker Setup
    - Single Container
    - Docker Compose (Recommended)
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
    
- Provides a REST API to fetch all the scraped courses
- Randomizes and serves course data, including titles, providers, ratings, and course details
- Uses Redis for caching and task queue management

## Technologies Used

- Flask for the API
- BeautifulSoup for web scraping
- Flask-CORS to allow cross-origin requests from the frontend
- Requests to fetch HTML content from the course websites
- Docker and Docker Compose for containerization
- Redis for caching and message broker

## Installation

You can set up the backend either traditionally or using Docker.

### Traditional Setup

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/freecoursehive-backend.git
   cd freecoursehive-backend
   ```

2. Set Up Virtual Environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Install and Start Redis

   You'll need Redis running locally. Install it according to your operating system:

   - Ubuntu/Debian:
     ```bash
     sudo apt-get install redis-server
     sudo service redis-server start
     ```
   - macOS:
     ```bash
     brew install redis
     brew services start redis
     ```
   - Windows: Download and install from the [Redis website](https://redis.io/download)

5. Run the Flask Application

   ```bash
   python src/script.py
   ```

   By default, the app will run at `http://127.0.0.1:5000`.

### Docker Setup

There are two ways to run the application with Docker: using a single container or using Docker Compose (recommended).

#### Single Container Setup

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/freecoursehive-backend.git
   cd freecoursehive-backend
   ```

2. Build the Docker Image

   ```bash
   docker build -t freecoursehive-backend .
   ```

3. Run Redis Container

   ```bash
   docker run -d --name redis-server -p 6379:6379 redis
   ```

4. Run the Application Container

   ```bash
   docker run -d \
     --name freecoursehive \
     -p 5000:5000 \
     --link redis-server:redis \
     -e CACHE_REDIS_URL=redis://redis:6379/0 \
     
   ```

#### Docker Compose Setup (Recommended)

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/freecoursehive-backend.git
   cd freecoursehive-backend
   ```

2. Start the Services

   ```bash
   docker-compose up -d
   ```

   This will:
   - Build the Flask application image
   - Start the Redis service
   - Start the Flask application
   - Set up all necessary networking

3. View Logs

   ```bash
   docker-compose logs -f
   ```

4. Stop the Services

   ```bash
   docker-compose down
   ```

## Environment Variables

The application uses the following environment variables:

```
FLASK_APP=src/script
PYTHONPATH=/app
CACHE_REDIS_URL=redis://redis:6379/0
FLASK_DEBUG=1
PORT=5000
```

These are automatically set in the Docker environment, but you'll need to set them manually for traditional setup.

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
  - id: A unique identifier for the course
  - title: The title of the course
  - provider: The platform providing the course (e.g., Coursera, Harvard, etc.)
  - detail: A brief detail or description of the course
  - rating: Course rating (if available)
  - category: The category of the course
  - link: A URL to the course

### Example Response:

```json
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
```

## Contributing

We welcome contributions from developers of all levels! If you'd like to contribute, please follow these steps:

- Fork the repository
- Create a new branch for your feature or bugfix
- Commit your changes and push your branch to your fork
- Submit a pull request for review

Please refer to our [CONTRIBUTING.md](https://github.com/freecoursehive/freecoursehive_be/blob/master/CONTRIBUTING.md) for detailed contribution guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
