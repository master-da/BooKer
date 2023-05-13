from app import render_template, request, hotelApi, current_user

class Home:
    def __init__(self):
        pass

    def serve(self):

        locations = []
        if request.method == "POST":
            # print(request.form['location'])
            locations = hotelApi.searchPlace(request.form['location'])
            # print(locations)

        return render_template("home.html", locations=locations)