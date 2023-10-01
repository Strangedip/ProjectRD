import os

from flask import Flask, render_template


# create and configure the app
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

app.run(debug=True)