FROM python:3.10.0b4

WORKDIR /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install pipenv

RUN pipenv install --dev
