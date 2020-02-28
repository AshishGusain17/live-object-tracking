from flask import Flask, render_template, url_for, request, redirect,Response,send_file
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cv2
from cam_shift import *
from mean_shift import *
from mouse_click_event import *

app = Flask(__name__)


from time import time

inde = 0


@app.route('/')
def index():
    return render_template('index.html',choice=1)

@app.route('/onspot')
def onspot():
    return render_template('index.html',choice=2)


@app.route('/click')
def click():
    func1()
    return render_template('index.html',choice=2)

@app.route('/mean')
def mean():
    func2()
    return render_template('index.html',choice=2)

@app.route('/crop')
def crop():
    return send_file('roi.jpg', mimetype='image/gif')


@app.route('/cam')
def cam():
    func3()
    return render_template('index.html',choice=2)



if __name__ == "__main__":
    app.run(debug=True)
