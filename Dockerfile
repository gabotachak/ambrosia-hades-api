# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /ambrosia-hades-api

ENV DB_HOST host.docker.internal
ENV DB_PORT 3308
ENV DB_SCHEMA hades
ENV DB_USER root
ENV DB_PASSWORD ambrosia

COPY requirements.txt requirements.txt
RUN apk add build-base
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]