from flask import Flask, render_template, request
from app.services.foursquareApi import FourSquareApi

hotelApi = FourSquareApi()

app = Flask(__name__)

from app import routes
