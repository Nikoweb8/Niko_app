from flask import Flask , render_template , request, redirect
import csv
app = Flask(__name__)
print(__name__)

############# l'R.B.A  del sito ############################
#############   route.base.app  ############################

@app.route('/')
def my_home():
    return render_template('index.html')


