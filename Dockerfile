FROM python:3.11-buster

WORKDIR /var/apps/rep_tracker
COPY . /var/apps/rep_tracker

RUN pip install -r requirements.txt
