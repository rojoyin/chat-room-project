FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /initializer
WORKDIR /initializer
COPY ./initializer /initializer

RUN adduser -D user
USER user
