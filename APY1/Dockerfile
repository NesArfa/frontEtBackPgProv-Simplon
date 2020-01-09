FROM python:3.8.0-buster

RUN apt-get install libpq-dev && mkdir /app

WORKDIR /app

COPY . /app/

#RUN pip3 install -r requirements.txt

CMD python3 api-crud.py
