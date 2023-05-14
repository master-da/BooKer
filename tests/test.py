from tests import host, requests, hotelApi
from app.models import UserTable, BookingTable

# fsq_id=4c7d0128247cb60c0b905f5e
# 52f4c71111d28cbffcfa1001
def login_success():
    url = 'http://' + host + '/login'
    data = {"email": "mail@outlook.com", "pass": "pass", "signin": "Sign In"}
    user = UserTable().getUserFromEmail(data['email'])
    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert user.email == data['email']
    assert user.password == data['pass']

    print("Login Successful!!")

def signup_success():
    url = 'http://' + host + '/signup'
    data = {"name": "testuser", "email": "mail@outlook.com", "pass": "pass", "create_account": "Create Account"}
    response = requests.post(url, data=data)
    user = UserTable().getUserFromEmail(data['email'])

    assert response.status_code == 200
    assert user.email == data['email']
    assert user.password == data['pass']
    print("Signup Successful!!")

def hotel_search():
    hotelList = hotelApi.searchPlace("Dhaka, Bangladesh")

    assert len(hotelList) > 0

    for idx, hotel in enumerate(hotelList):
        print(f"{idx+1}. {hotel['name']} - {hotel['address']} \n")

def hotel_book():
    url = 'http://' + host + '/hotel?fsq_id=4c7d0128247cb60c0b905f5e'
    data={"book": "Book", "check_in": "2020-12-12", "check_out": "2020-12-13", "adults": "2", "children": "1", "room": "1"}
    login_success()
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print("Hotel Booked!!")

def profile_edit():
    url = 'http://' + host + '/profile'
    data={"profile": "profile", "test": "test", "inputUsername": "test-changed", "id": "5", "email": "mail@outlook.com"}
    login_success()
    requests.post(url, data=data)
    user = UserTable().getUserFromEmail(data['email'])

    assert user.name == data['inputUsername']
    print("Profile Edit Successful!!")


# login_success()
# signup_success()
# hotel_search()
# hotel_book()
# profile_edit()
