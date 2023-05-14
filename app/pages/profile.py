from app import render_template, current_user

class Profile:
    def __init__(self):
        pass

    def serve(self):
        user = current_user
        return render_template("profile.html", username=user.name)
