# Backabuddy
Drinks/Cocktails API

## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)

## Installing
### Setting up the database
- Start your database server and create your database

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/kwanj-k/Backabuddy.git) `git clone https://github.com/kwanj-k/Backabuddy.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv venv`
- Create a .env file and put these key=values in it:
```
source venv/bin/activate
export SECRET_KEY="key"
export DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/NAME"
export DJANGO_SETTINGS_MODULE="drinksapi.settings.dev"
export SUPER_NAME=""
export SUPER_EMAIL=""
export SUPER_PASS=""
```

- Load the environment variable `source .env`
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## Run tests
- Run `make test`

