FROM python:3
MAINTAINER "S M Y ALTAMSH <smy.altamash@gmail.com>"
WORKDIR /app
ADD app/requirements.txt /app
RUN apt-get update
RUN pip install -r requirements.txt
ADD app/ /app
CMD python app.py
