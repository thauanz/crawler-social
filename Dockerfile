FROM python:latest

MAINTAINER 'Thauan <thauanz@gmail.com>'

RUN apt-get update && \
    pip install tapioca-wrapper tapioca-twitter

RUN adduser --disabled-password bart
USER bart
WORKDIR /home/bart

COPY . /home/bart/app
