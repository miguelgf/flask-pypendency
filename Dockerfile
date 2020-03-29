FROM python:3.6-slim

ENV PYTHONPATH /usr

WORKDIR /usr

COPY Pipfile /usr/Pipfile
COPY Pipfile.lock /usr/Pipfile.lock

RUN pip install pipenv \
    && pipenv install --dev
