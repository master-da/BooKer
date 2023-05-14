from app import render_template, current_user, request, url_for, app, hotelApi, logout_user, flash, redirect
from app.models import UserTable
import pandas as pd
import os

class Profile:
    def __init__(self):
        pass

    user = current_user
    bookingTableHeaders = [
        "Hotel Name",
        "Location",
        "Check In",
        "Check Out",
        "No Of Adults",
        "No Of Children",
        "No of Rooms"
    ]
    bookingTableRow = []
    def serve(self):
        print(request.form)
        if 'test' not in request.form:
            
            bookingList = self.user.getBookings() 
            self.bookingTableRow = []
            for _, booking in bookingList.iterrows():
                hotel = hotelApi.getPlaceNameBasic(booking['hotel_fsq_id'])
                self.bookingTableRow.append([
                    hotel['name'],
                    hotel['location']['formatted_address'],
                    booking['check_in'],
                    booking['check_out'],
                    booking['adults'],
                    booking['children'],
                    booking['rooms']
                ])
        

        if request.method == 'POST':
            return self.handlePostRequest()
        
        return render_template("profile.html", user=self.user, bookingTableHeaders=self.bookingTableHeaders, bookingTableRow=self.bookingTableRow)

    def handlePostRequest(self):
        print(request.form, current_user)
        if 'profile' in request.form:

            if 'test' in request.form:
                UserTable().updateUsername(request.form['id'], request.form['inputUsername'])
            else :
                if 'pfp' in request.files and request.files['pfp'].filename != "":
                    print("pfp")
                    pfp = request.files['pfp']
                    pfp.save(os.path.join(app.root_path, 'static', 'images', 'pfp', self.user.name + '.' + request.files['pfp'].filename.split('.')[-1]))
                    self.user.updatePfp('pfp/' + self.user.name + '.' + pfp.filename.split('.')[-1])
                if 'inputUsername' in request.form:
                    self.user.updateUsername(request.form['inputUsername'])

        if 'password' in request.form:

            error = None
            print(request.form)
            if 'passwordCurrent' not in request.form or request.form['passwordCurrent'] == "":
                error = "Current Password Not Provided"
            elif 'passwordNew' not in request.form or request.form['passwordNew'] == "":
                error = "New Passwords not Provided"
            elif 'passwordNew2' not in request.form or request.form['passwordNew2'] == "":
                error = "New Passwords not Provided"
            else:

                passwordCurrent = request.form['passwordCurrent']
                passwordNew = request.form['passwordNew']
                passwordNew2 = request.form['passwordNew2']

                if passwordCurrent != current_user.password:
                    error = "Current Password Incorrect"
                elif passwordNew != passwordNew2:
                    error = "New Passwords Do Not Match"
                else:
                    success = current_user.changePassword(passwordCurrent, passwordNew)
                    if success: error = "Password Changed Successfully"
                    else: error = "Password Change Failed"

            return render_template("profile.html", user=self.user, error=error, bookingTableHeaders=self.bookingTableHeaders, bookingTableRow=self.bookingTableRow)

        if 'delete' in request.form:

            if 'inputPassword' not in request.form or request.form['inputPassword'] == "":
                error = "Password Not Provided"
                return render_template("profile.html", user=self.user, error=error, bookingTableHeaders=self.bookingTableHeaders, bookingTableRow=self.bookingTableRow)

            if request.form['inputPassword'] != self.user.password:
                error = "Password Incorrect"
                return render_template("profile.html", user=self.user, error=error, bookingTableHeaders=self.bookingTableHeaders, bookingTableRow=self.bookingTableRow)

            success = self.user.deleteAccount()
            if success: 
                flash("Account Deleted Successfully")
                logout_user()
                return redirect(url_for('login'))

        return render_template("profile.html", user=self.user, bookingTableHeaders=self.bookingTableHeaders, bookingTableRow=self.bookingTableRow)

