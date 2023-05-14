<<<<<<< HEAD
from app import render_template
=======
from app import render_template, current_user
>>>>>>> 172cb062a8bfc81e0e7e9942ee2073db4708edbf

class Profile:
    def __init__(self):
        pass

    def serve(self):
<<<<<<< HEAD
        return render_template("profile.html")
=======
        user = current_user
        return render_template("profile.html", username=user.name)
>>>>>>> 172cb062a8bfc81e0e7e9942ee2073db4708edbf
