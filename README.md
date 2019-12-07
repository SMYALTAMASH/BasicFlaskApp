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

| COMMAND | DESCRIPTION |
| --- | --- |
| FROM python:3.6-alpine | specifies the OS/Base Image from which the application is getting built. |
| MAINTAINER "S M Y ALTAMSH <smy.altamash@gmail.com>" | Maintainer Details. |
| WORKDIR /app | Our Flask Application code resides in /app of the docker container so changing directory to /app. |
| ADD app/requirements.txt /app | copying only "requirements.txt" to install flask dependencies. |
| RUN apk update | Updating the docker cache and refreshing the container image repositories. |
| RUN pip install -r requirements.txt | Installing the dependencies in the container image. |
| ADD app/ /app | Copy the code files and static contents. TIP: [Always keep changing data at the last to build the image faster]. |
| CMD python app.py | Run the flask application at startup. |

### Try out the docker image.
```
sudo docker run -d -p 1111:5000 --name flaskrestapi kingalt/flask:1.0
```
* Open the browser and play with the flask app.
* There are 3 APIS which are exposed by the APP.

| API-ENDPOINT | DESCRIPTION |
| --- | --- |
| "http://localhost:1111/" | This Displays the starting page. |
| "http://localhost:1111/myinfo" | This gives the developer description. |
| "http://localhost:1111/status" | This gives the health check details of the API. |

* Check the logs of the application running.
```
sudo docker logs -f flaskrestapi
```

* TO Remove the conatiner
```
sudo docker rm -f flaskrestapi
```

## App file description
```
@app.route("/myinfo", methods = ['GET'])
def myinfo():
    return jsonify(
        quote="The King Never Fails To Win His Destiny",
        name="S M Y ALTAMSH",
        profession="DevOps Engineer",
        github="https://github.com/smyaltamash/",
        status="200"
    )

@app.errorhandler(404)
def invalid_route(e):
    return render_template('index.html')

```

* @app.route("/myinfo", methods = ['GET']) # This indicates the API ENDPOINT for the flask application and the allowed method is "GET".
* Below this flask API Definition we can have python functions and perform various operations on the data.
* return jsonify # This is used to return json responses, the First part is the key and the second part is the value.
* @app.errorhandler(404) # This is like an error handler for the image if we get 404 status code the below function will be called.
