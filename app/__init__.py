from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app.models import User
from app.services.foursquareApi import FourSquareApi

hotelApi = FourSquareApi()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-application-needs-a-secret-key-why-does-it-need-it'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User().get(user_id)

from app import routes