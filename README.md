# Getting Started
THIS IS SIMPLE DJANGO REST APPLICATION WHICH INSERTS AND DELETES MOVIES FROM SQLITE DATABASE

#STEPS TO START PROJECT

### `git clone https://github.com/mithjain/movies-rest`
### `cd movies`
### `python manage.py migrate`
### `python manage.py makemigrations`

## ENDPOINT

To Insert Movie

### `POST http:127.0.0.1:8000/api`

To Get Movies

### `GET http:127.0.0.1:8000/api`