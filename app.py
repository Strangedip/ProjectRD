from flask import request
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy.sql import func


# create and configure the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/sg022/Desktop/Git/ProjectRD/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Inventory(db.Model):
    Item_ID = db.Column(db.Integer, primary_key=True)
    Item_Name = db.Column(db.String(50), nullable=False)
    Item_Price = db.Column(db.Integer, nullable=False)
    Item_Count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<{self.Item_Name}>'



def verify(email, password):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    user = conn.execute(
        'SELECT * FROM user WHERE email = ?', (email,)).fetchone()
    conn.close()
    if user is None:
        return False
    if password == user['password']:
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    email = request.values.get('email')
    password = request.values.get('password')
    if verify(email, password):
        return render_template('home.html', msg="true")

    return redirect(url_for('invalid_login_msg'))


@app.route('/invalid-credentials')
def invalid_login_msg():
    return render_template('error.html')


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


@app.route('/create-order')
def create_order():
    return render_template('create-order.html')


@app.route('/current-orders')
def current_orders():
    return render_template('current-orders.html')


@app.route('/order-history')
def order_history():
    return render_template('order-history.html')


@app.route('/create')
def create():
    return render_template('error.html')


app.run(debug=True)
