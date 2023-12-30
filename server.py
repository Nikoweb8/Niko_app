
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


@app.route('/2019.html')
def my_2019():
    return render_template('2019.html')

@app.route('/2020.html')
def my_2020():
    return render_template('2020.html')

@app.route('/2021.html')
def my_2021():
    return render_template('2021.html')

@app.route('/2022.html')
def my_2022():
    return render_template('2022.html')

@app.route('/2023.html')
def my_2023():
    return render_template('2023.html')

@app.route('/NewsPaper.html')
def my_NewsPaper():
    return render_template('NewsPaper.html')