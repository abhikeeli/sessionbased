from flask import Blueprint,redirect,url_for,request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user
from . import db
from flask_login import login_required, current_user,logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/login',methods=['POST'])
def login_post():
    email=request.json['email']
    password=request.json['password']
    remember = True if request.json['remember'] else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    login_user(user,remember=remember)
    
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/signup',methods=['POST'])
def signup_post():
    email=request.json['email']
    name = request.json['name']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()
    if user:
        return redirect(url_for('auth.signup'))  
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))