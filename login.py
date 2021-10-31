from flask import Flask,render_template,request,redirect
import os
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hack'
db = SQLAlchemy(app)

class Stock(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    stock = db.Column(db.String(12), nullable=False)
    price = db.Column(db.String(120), nullable=False)
    profit = db.Column(db.String(12), nullable=True)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    pas = db.Column(db.String(12), nullable=False)
  

@app.route("/", methods = ['GET','POST'])
def signin():
    
    user = User.query.all()
    return render_template('index.html',params=params , user=user)
    UN= request.form['Username']
    PN= request.form['Password']

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/home")
def home():
    return render_template('home.html')

if __name__=="__main__":
        app.run()
