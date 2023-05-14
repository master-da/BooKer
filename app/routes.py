from app import app, render_template, request, hotelApi, redirect, url_for, login_required
from app.pages.login import Login
from app.pages.signup import Signup
from app.pages.home import Home
from app.pages.hotel import Hotel
from app.pages.profile import Profile
from app.pages.itinerary import Itinerary

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def home():
    return Home().serve()

@app.route("/hotel", methods=["GET", "POST"])
def hotels():
    return Hotel().serve()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return Signup().serve()

@app.route("/login", methods=["GET", "POST"])
def login():
    return Login().serve()

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    return Profile().serve()

@app.route("/itinerary", methods=["GET", "POST"])
def itinerary():
    return Itinerary().serve()
