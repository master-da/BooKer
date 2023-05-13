from app import render_template, request, redirect, url_for

class Login:
    def __init__(self):
        pass

    def serve(self):
        if request.method == 'POST':
            return self.handlePostReq()
        
        return render_template("login.html")
    
    def handlePostReq(self):
        if 'to_signup' in request.form:
            return redirect(url_for('signup'))
        elif 'signin' in request.form:
            if 'email' not in request.form or 'pass' not in request.form:
                return render_template("login.html", error="Please enter both email and password")
    