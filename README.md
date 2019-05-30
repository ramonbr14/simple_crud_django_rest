
# Simple CRUD with Django REST-framework and Sqlite

This project was generated with [Python](https://www.python.org/downloads/release/python-368/) version 3.6.


### Environment

Create, activate python environments and install dependencies to run project.

##### Creating a virtualenv

First you have to install virtualenv with python's package manager 'PIP' with command bellow

```
$ pip3 install virtualenv
```
After installed you have to create an env to your project with the command bellow

```
$ virtualenv -p PYTHON_DIR ENV_NAME
```

Now you have to activate your env in the project with the command bellow

```
$ python -m venv ENV_DIR

$ source ENV_DIR/bin/activate
```

> **Note** : You must first activate python environments before install dependencies.


### Install dependencies

```
pip install -r requirements.txt
```

> **Note** : You may update the requirements file with `pip freeze > requirements.txt`. Run `make md5` when changing.


## Development server

### Django

Run `python manage.py runserver 0.0.0.0:8000` for a dev server. Navigate to `http://localhost:8000/` to check django page. The app will automatically reload if you change any of the source files.
