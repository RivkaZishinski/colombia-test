FROM ubuntu:24.04

ARG FLET_SERVER_PORT

ENV FLET_SERVER_PORT=$FLET_SERVER_PORT

WORKDIR /app

COPY ./ /app

EXPOSE $FLET_SERVER_PORT

RUN apt-get update && apt-get install -y python3 python3-pip libgdal-dev

RUN  pip install . --break-system-packages

CMD flet run -d --web --port $FLET_SERVER_PORT main.py
