from app import render_template, request, redirect, url_for, login_user, get_flashed_messages
from app.models import UserTable

class Login:

    def serve(self):
        
        if request.method == 'POST':
            return self.handlePostReq()
        
        flashed_mesage = get_flashed_messages()

        if len(flashed_mesage) > 0:
            return render_template("login.html", error=flashed_mesage[0], loginFailed=True)    

        return render_template("login.html")
    
    def handlePostReq(self):
        if 'to_signup' in request.form:
            return redirect(url_for('signup'))
        elif 'signin' in request.form:
            
            if 'email' not in request.form or 'pass' not in request.form:
                return render_template("login.html", error="Empty email or password", loginFailed=True)
            
            elif request.form['email'] == "" or request.form['pass'] == "":
                return render_template("login.html", error="Empty email or password", loginFailed=True)
            
            user = UserTable().authenticate(request.form['email'], request.form['pass'])
            if user != None:
                login_user(user)
                return redirect(url_for('home'))
            return render_template("login.html", error="No matching Account Found", loginFailed=True)
