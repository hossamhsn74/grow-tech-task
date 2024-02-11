# GrowTech API Task
## Overview
This is a Django-based blog application that allows users to create, read, update, and delete blog posts. It comes with a RESTful API built using Django REST Framework.

## Setup
- **Clone the Repository:**
  ```bash
  git clone https://github.com/hossamhsn74/grow-tech-task
  ```
- **Build and Run Docker Containers:**
  ```bash
  cd grow-tech-task
  docker-compose up --build
  ```
  This command will build the Docker images and start the containers. The app should now be accessible at 
  http://localhost:8000.

- **Database Setup:**
  - Once the containers are up and running, you can set up the database by running:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

  - Create Superuser:
  Create a superuser to access the Django admin panel:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```


- **Running Tests:**
  To run the test cases for the app using pytest, follow these steps:
  
  - Access Docker Container:
  Access the Docker container running the Django app
    ```bash
    docker-compose exec web bash
    ```
  - Run Tests:
  Run the test suite using pytest:
    ``` bash
    pytest
    ```
  - Generate Coverage Report:
  To generate a coverage report, use the following command:
    ``` bash
    pytest --cov=.
    ```
    This command will generate a coverage report showing the percentage of code covered by the tests.

## API Documentation

The API documentation can be found at http://localhost:8000/redoc/. This provides detailed information on the available endpoints and how to interact with them.
Also feel free to try the app through swagger http://localhost:8000/swagger/, just make sure to login for the endpoints that require authentication, if you don't want to use session auth and login. you can use the /token endpoint passing the username & password to get auth token.

## License

This project is licensed under the MIT License - see the LICENSE file for details.