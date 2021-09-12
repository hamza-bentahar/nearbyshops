## About NearbyShops

Implement an app that list shops nearby

## Overview

- Sign up using username, email and password
- Sign in using username and password
- Display list of shops sorted by distance
- Like a shop
- Display list of liked shops
- Remove a shop from the liked shops

## Technologies used

- [Django 3.2](https://www.djangoproject.com/)
- [Django Rest Framework 3.12](https://www.django-rest-framework.org/)
- [Vue 2.6](https://vuejs.org/)
- [axios](https://github.com/axios/axios)
- [Vuetify 2.4](https://vuetifyjs.com/en/)


## Requirements

- Python 3
- NodeJs
- MySQL

## Quick Project Setup - Installation

##### 1. Clone the repository using the following command in terminal:

    git clone https://github.com/hamza-bentahar/nearbyshops.git

##### 2. Install python dependencies

    cd nearbyshops
    pip install -r requirements.txt

##### 3. build frontend
    cd frontent
    npm install
    npm run build

##### 4. Create a Mysql database called nearbyshops

##### 5. Setup database schema and then seed data
    python manage.py makemigrations api
    python manage.py migrate api

##### 9. Start development server

    python manage.py runserver 8000

##### 10. All set! Access the application in the browser with the given url
