from app import render_template, request, redirect, url_for, login_user
from app.models import UserTable

class Login:
    def __init__(self):
        pass

    def serve(self):
        if request.method == 'POST':
            return self.handlePostReq()
        
        return render_template("login.html")
    
    def handlePostReq(self):
        if 'to_signup' in request.form:
            print("to signup")
            return redirect(url_for('signup'))
        elif 'signin' in request.form:

            if 'email' not in request.form or 'pass' not in request.form:
                return render_template("login.html", error="Invalid email or password")
            user = UserTable().authenticate(request.form['email'], request.form['pass'])
            # print(user)
            if user != None:
                login_user(user)
                return redirect(url_for('home'))
            return render_template("login.html")