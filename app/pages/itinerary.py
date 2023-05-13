from app import render_template

class Itinerary:
    def __init__(self):
        pass

    def serve(self):
        return render_template("itinerary.html")