from app import render_template, request, hotelApi, current_user
from app.models import BookingTable

class Hotel:

    fsq_id = ""
    
    photos = []
    tips = []
    tel = ''
    email = ''
    website = ''
    social_media = {}

    def __init__(self):
        pass

    def serve(self):
        # print(">>>>>>>>>>>>>>>>>>", request.args, "<<<<<<<<<<<<<<")
        if 'fsq_id' in request.args:
            self.fsq_id = request.args['fsq_id']
            self.getHotelDetails()
        else:
            print(">>>>>>>>>>>>>>>>>>", "FSQ ID NOT PROVIDWED", "<<<<<<<<<<<<<<")
        error = ""
        if request.method == 'POST':
            if 'book' in request.form:
                error = self.booking()
        return render_template("hotel.html", fsq_id=self.fsq_id, photos=self.photos, tips=self.tips, tel=self.tel, email=self.email, website=self.website, social_media=self.social_media, error=error)
    
    def getHotelDetails(self):
        hotelDetails = hotelApi.getPlaceDetails(self.fsq_id)
        try:
            
            self.photos = hotelDetails['photos']
            self.tips = hotelDetails['tips']
            self.tel: hotelDetails['tel']
            self.email: hotelDetails['email']
            self.website: hotelDetails['website']
            self.social_media = hotelDetails['social_media']

        except KeyError as e: print(e)

    def booking(self):
        
        if 'check_in' not in request.form:
            return "Please provide Check In data"
        if 'check_out' not in request.form:
            return "Please provide Check Out data"
        if 'adults' not in request.form:
            return "Please provide no of adults"
        if 'children' not in request.form:
            return "Please provide no of children"
        if 'rooms' not in request.form:
            return "Please provide no of rooms"
        
        user = current_user
        if user is None:
            return "You have to log in first"
        
        # print(user.id, request.form['check_in'], request.form['check_out'], request.form['adults'], request.form['children'], request.form['rooms'])
        success = BookingTable().insert(user.id, self.fsq_id, request.form['check_in'], request.form['check_out'], request.form['adults'], request.form['children'], request.form['rooms'])
        print(success)
    
