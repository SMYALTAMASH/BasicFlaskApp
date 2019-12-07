FROM python:3
WORKDIR /app
ADD app/requirements.txt /app
RUN apt-get update
RUN pip install -r requirements.txt
ADD app/ /app
CMD python app.py
