from app import render_template

class Signup:
    def __init__(self):
        pass

    def serve(self):
        return render_template("sign_up.html", name="Signup")
