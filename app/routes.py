from app import app, render_template, request, hotelApi, redirect, url_for
from app.pages.login import Login
from app.pages.signup import Signup
from app.pages.home import Home
from app.pages.hotel import Hotel

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("base.html")

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