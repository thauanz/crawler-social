FROM python:latest

MAINTAINER 'Thauan <thauanz@gmail.com>'

RUN apt-get update && \
    pip install tapioca-wrapper tapioca-twitter && \
    pip install -U Celery

WORKDIR /app/lib

COPY . /app

CMD sleep 5 && /usr/local/bin/celery -A main.app worker -B --loglevel=debug