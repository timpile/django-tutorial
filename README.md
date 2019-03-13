# Django Tutorial App

[Tutorial]:(https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

## Requirements
- You'll need the package `venv` for creating virtual environments.

From the root of this directory:

- Create a new virtual environment: `python3 -m venv venv`
- Activate the new virtual environment: `source venv/bin/activate`

> TODO 
> Setup dependencies in requirements.txt
> `pip install -r requirements.txt`

- Install Django`pip install Django`
  - `python -m django --version` to check version
- Install Direnv with `brew install direnv`
  - Follow the instruction for [hooking direnv into your shell](https://github.com/direnv/direnv#bash)
  - Copy `.envrc.example` and paste it as `.envrc` at the same directory level
  - Run `direnv allow .`


## Database setup

- Install postgres `pip install psycopg2`
- Create database `psql -U postgres` -> `CREATE DATABASE django_tutorial;`
- `python manage.py migrate`
