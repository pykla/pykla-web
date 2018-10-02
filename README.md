# Pykla-web

The official website for Python Kampala (PyKla)

## Technologies

* Python 3.6
* SQLite3

## Requirements

* Install [Python](https://www.python.org/downloads/)

## Setup (Mac OS)

* Run `git clone` this repository and `cd` into the project root.
* Run `pip install virtualenv` on command prompt
* Run `virtualenv ../pykla-venv --python=python3`
* Run `source ../pykla-venv/bin/activate`
* Run `pip install -r requirements.txt`
* Run `python manage.py migrate`
* Run `python manage.py runserver`
* View the app at `http://127.0.0.1:8000/`

## Contributing

* Create a branch off `master`.
* Make changes and raise a PR to `master`
* Add your name and Github URL to [Contributors.md](./Contributors.md)
