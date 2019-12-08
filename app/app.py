import logging
from flask import jsonify, Flask, render_template, url_for
from flask_events import Events
from datetime import datetime
import requests

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
events = Events(app)

@app.route("/", methods = ['GET'])
def first():
    events.add('type : webpage' , 'endpoint : /')
    return render_template('index.html')

@app.route("/myinfo", methods = ['GET'])
def myinfo():
    events.add('type : request','endpoint : /myinfo')
    return jsonify(
        quote="The King Never Fails To Win His Destiny",
        name="S M Y ALTAMSH",
        profession="DevOps Engineer",
        github="https://github.com/smyaltamash/",
        status="200"
    )

@app.route('/status', methods = ['GET'])
def status():
    StartTime = datetime.now()
    logStartTime = StartTime.strftime("%d/%m/%Y %H:%M:%S:%f")
    url = "http://localhost:5000/"
    code = requests.get("{}".format(url))
    EndTime = datetime.now()
    logEndTime = EndTime.strftime("%d/%m/%Y %H:%M:%S:%f")
    events.add('type : request','endpoint : /status')
    return jsonify(
        starttimestamp=logStartTime,
        service="Kings App",
        statuscode="{}".format(code),
        endtime=logEndTime
    )

@app.errorhandler(404) 
def invalid_route(e):
    logging.info(e)
    events.add('type : request',e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
