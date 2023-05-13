from app import render_template

class Profile:
    def __init__(self):
        pass

    def serve(self):
        return render_template("profile.html")