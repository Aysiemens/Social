from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'
db = SQLAlchemy(app)
app.secret_key = '736427652364578236458237465823465823765263485762349875696'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
manager = LoginManager(app)


@manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@app.route('/')
def header():
    return render_template('login.html')


app.run(host='127.0.0.1', port=80, debug=True)




