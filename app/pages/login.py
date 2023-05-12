from app import render_template, request, redirect, url_for

class Login:
    def __init__(self):
        pass

    def serve(self):
        if request.method == 'POST':
            self.handlePostReq()
        
        return render_template("login.html", name="Login")
    
    def handlePostReq(self):
        if 'to_signup' in request.form:
            print("to_signup")
            redirect(url_for('signup'))
    