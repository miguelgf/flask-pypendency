FROM python:3.13.0a1

WORKDIR /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install pipenv

RUN pipenv install --dev
