from app import render_template, request, hotelApi, current_user

class Home:
    def __init__(self):
        pass

    def serve(self):
        searched = False
        locations = []
        if request.method == "POST":
            # print(request.form['location'])
            locations = hotelApi.searchPlace(request.form['location'])
            searched = True
            # print(locations)

        user = current_user
        if user.is_authenticated:
            return render_template("home.html", locations=locations, user=user, noLocation=True if len(locations) == 0 and searched else False)

        return render_template("home.html", locations=locations)