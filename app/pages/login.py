from app import render_template

class Login:
    def __init__(self):
        pass

    def serve(self):
        return render_template("login.html", name="Login")