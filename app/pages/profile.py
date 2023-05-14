from app import render_template, current_user

class Profile:
    def __init__(self):
        pass

    def serve(self):
        user = current_user
<<<<<<< HEAD
        return render_template("profile.html", username=user.name)
=======
        return render_template("profile.html", username=user.name)
>>>>>>> dc3238daf0c25b916f0805b9f19d1e9044759d24
