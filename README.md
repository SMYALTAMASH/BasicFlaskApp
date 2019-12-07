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


