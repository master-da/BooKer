from app import render_template, request, hotelApi

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
        if request.method == "GET":
            print(">>>>>>>>>>>>>>>>>>", request.args, "<<<<<<<<<<<<<<")
            if 'fsq_id' in request.args:
                self.fsq_id = request.args['fsq_id']
                self.getHotelDetails()
            else:
                print(">>>>>>>>>>>>>>>>>>", "FSQ ID NOT PROVIDWED", "<<<<<<<<<<<<<<")
        return render_template("hotel.html", photos=self.photos,tips=self.tips,tel=self.tel,email=self.email,website=self.website,social_media=self.social_media)
    
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
    
