import os
from flask import request
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


# create and configure the app
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    email = request.values.get('email')
    password = request.values.get('password')
    if email == 'admin@gmail.com' and password == 'admin':
        return render_template('home.html', msg="true")

    return redirect(url_for('login'))


app.run(debug=True)
