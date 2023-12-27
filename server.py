
import smtplib
from flask import Flask , render_template , request, redirect
import csv
app = Flask(__name__)
print(__name__)

############# l'R.B.A  del sito ############################
#############   route.base.app  ############################

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def my_index():
    return render_template('index.html')

@app.route('/video.html')
def my_video():
    return render_template('video.html')

@app.route('/photo.html')
def my_photo():
    return render_template('photo.html')

@app.route('/Results.html')
def my_Results():
    return render_template('Results.html')

