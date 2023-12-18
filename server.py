
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






def send_email(subject, body):
    sender_email = "tuo@email.com"
    receiver_email = ""

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, "la_tua_password")
            server.sendmail(sender_email, receiver_email, message)
            print("Email inviata con successo!")
    except Exception as e:
        print(f"Errore durante l'invio dell'email: {e}")

# Esempio di utilizzo
send_email("Oggetto dell'email", "Questo è il corpo dell'email.")