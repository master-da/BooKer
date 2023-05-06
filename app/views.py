from app import app, render_template, request, hotelApi

@app.route("/home", methods=["GET", "POST"])
def index():
    locations = []
    if request.method == "POST":
        # print(request.form['location'])
        locations = hotelApi.searchPlace(request.form['location'])
        print(locations)

    return render_template("home.html", locations=locations)

