from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9e5be3e78db0fb59ba72329ec01a90af'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(20), unique=True, nullable=True)
    Email = db.Column(db.String(120), unique=True, nullable=True)
    Phone = db.Column(db.String(20), nullable=True)
    City = db.Column(db.String(60), nullable=True)
    Address = db.Column(db.String(60), nullable=True)
    Date= db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f"User('{self.Name}', '{self.email}')"


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/aboutus")
def about():
    return render_template('aboutus.html')
    
@app.route("/Booking")
def Booking():
    return render_template('Booking.html')
    
@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
   
    return render_template('register.html',form=form)
@app.route("/info")
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)