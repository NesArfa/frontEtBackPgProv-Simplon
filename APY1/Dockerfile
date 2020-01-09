FROM python:3.8.0-buster

RUN apt-get install libpq-dev && mkdir /app

WORKDIR /app

COPY . /app/

CMD python3 api-crud.py
