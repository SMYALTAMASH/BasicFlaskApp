import requests
from flask import jsonify, Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def first():
    return render_template('index.html')


@app.route("/myinfo")
def myinfo():
    return jsonify(
        user="king",
        quote="The King Never Fails To Win His Destiny",
        profession="DevOps Engineer",
        github="https://github.com/smyaltamash/",
        status="200"
    )

@app.route('/status')
def status():
    StartTime = datetime.now()
    logStartTime = StartTime.strftime("%d/%m/%Y %H:%M:%S:%f")
    url = "http://localhost:5000/"
    code = requests.get("{}".format(url))
    EndTime = datetime.now()
    logEndTime = EndTime.strftime("%d/%m/%Y %H:%M:%S:%f")
    return jsonify(
        starttimestamp=logStartTime,
        service="Kings App",
        statuscode="{}".format(code),
        endtime=logEndTime
    )

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')