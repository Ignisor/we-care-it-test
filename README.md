# We Care IT test task

Test task for We Care IT

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Using

- Python 3.7 :snake:
- Django 2.1

### Installing

First of all you need to clone the project
```
git clone https://github.com/Ignisor/we-care-it-test.git
```

There are two ways to run the project. By using Docker compose (recommended) or with raw python

#### Docker compose (recommended)

- Make sure you have [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) installed
- Make the `docker-entrypoint.sh` executable
    ```
    chmod +x docker-entrypoint.sh
    ```
- Create volume for static files
    ```
    docker volume create --name=static
    ```
- Build images
    ```
    docker-compose build
    ```
- Start application
    ```
    docker-compose up
    ```

#### Raw python

- It's recommended to create and use [virtual environment](https://docs.python.org/3/library/venv.html)
- Install requirements
    ```
    pip install -r requirements.txt
    ```
- Apply migrations
    ```
    python manage.py migrate
    ```
- Run the server
    ```
    python manage.py runserver
    ```
