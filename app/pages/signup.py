from app import render_template, request, redirect, url_for, flash
from app.models import UserTable

class Signup:
    def __init__(self):
        pass

    def serve(self):
        if request.method == 'POST':
            return self.handlePostReq()
        
        return render_template("signup.html")
    
    def handlePostReq(self):
        if 'create_account' in request.form:
            if 'name' not in request.form or 'email' not in request.form or 'pass' not in request.form:
                return render_template("signup.html", error="Invalid form Data", signupFailed=True)

            success = UserTable().insert(request.form['name'], request.form['email'], request.form['pass'])
            if success:
                flash("Account created successfully")
                return redirect(url_for('login'))
            print("Email or name already exists")
            return render_template("signup.html", error="Email or name already exists", signupFailed=True)

        return render_template("signup.html", error="Signup Failed", signupFailed=True)
        
