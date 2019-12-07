# Flask Project
* This is a Flask project to demonstrate how to build a RESTful API with Docker`.

## Requirements
* Docker 

## Build and Run

* Build the docker image using the below command
```
sudo docker build -t kingsflaskapp:latest .

```
* After the app is built run it using below command
```
sudo docker run -d -p someFreeSystemPort:5000 kingsflaskapp:latest # Replace someFreeSystemPort with unused system ports else use 5000 itself 
```
* Congratulations your flask app is up and running, now open the Browser and you can see the Flask App Up and Running.

## Tree Structure of the flask app

```
.
├── app
│   ├── app.py
│   ├── requirements.txt
│   ├── static
│   │   └── tiger.jpg
│   └── templates
│       └── index.html
```

* "app" directory contains the Entire Flask Application
* The File "app.py" contains the application code
* The File "requirements.txt" contains the pre-requisites for the flask app to work.
* static contents of the html files like images go inside the "static" directory.
* "templates" folder contains the html pages that our app.py uses to render the website.

## Dockerfile Description
```
FROM python:3
MAINTAINER "S M Y ALTAMSH <smy.altamash@gmail.com>"
WORKDIR /app
ADD app/requirements.txt /app
RUN apt-get update
RUN pip install -r requirements.txt
ADD app/ /app
CMD python app.py
```

* FROM python:3 # specifies the OS/Base Image from which the application is getting built.
* MAINTAINER "S M Y ALTAMSH <smy.altamash@gmail.com>" # Maintainer Details.
* WORKDIR /app # Our Flask Application code resides in /app of the docker container so changing directory to /app.
* ADD app/requirements.txt /app # copying only "requirements.txt" to install flask dependencies.
* RUN apt-get update # Updating the docker cache and refreshing the container image repositories.
* RUN pip install -r requirements.txt # Installing the dependencies in the container image.
* ADD app/ /app # Copy the code files and static contents. TIP: [Always keep changing data at the last to build the image faster].
* CMD python app.py # Run the flask application at startup.

## App file description
```
@app.route("/myinfo")
def myinfo():
    return jsonify(
        user="king",
        quote="The King Never Fails To Win His Destiny",
        profession="DevOps Engineer",
        github="https://github.com/smyaltamash/",
        status="200"
    )
```

* @app.route("/myinfo") # This indicates the API ENDPOINT for the flask application.
* Below this flask API Definition we can have python functions and perform various operations on the data.
* return jsonify # This is used to return json responses.
