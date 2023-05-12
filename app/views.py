from app import app, render_template, request, hotelApi

@app.route("/", methods=["GET", "POST"])
def index():
    locations = []
    if request.method == "POST":
        # print(request.form['location'])
        locations = hotelApi.searchPlace(request.form['location'])
        print(locations)

    return render_template("home.html", locations=locations)

@app.route("/hotel")
def hotels():
    return render_template("hotel.html", name="Hotel")

@app.route("/signup")
def signup():
    return render_template("sign_up.html", name="Signup")

@app.route("/login")
def login():
    return render_template("login.html", name="Login")