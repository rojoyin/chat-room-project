FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /bot
WORKDIR /bot
COPY ./bot /bot

RUN adduser -D user
USER user
