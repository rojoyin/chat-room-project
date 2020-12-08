FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /consumers
WORKDIR /consumers
COPY ./redis /redis

RUN adduser -D user
USER user
