from app import app, hotelApi
import requests

host = '127.0.0.1:5000'
app.config.update({"TESTING": True})

