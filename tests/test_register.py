import uuid

from utils.api_utils import APIUtils

BASE_URL = "https://api.eventhub.rahulshettyacademy.com"
REGISTER_URL = f"{BASE_URL}/api/auth/register"

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def test_register_user_positive():

    #generate a unique email so repeated jenkins runs don't
    #fail because the email already exist
    email = f"student_{uuid.uuid4().hex[:8]}@example.com"

    payload = {
        "email" : email,
        "password" : "secret123"
    }

    response = APIUtils.post_request(
        REGISTER_URL,
        payload,
        HEADERS
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    # Successful registration is normally 200 or 201.
    assert response.status_code in [200,201]

    response_json = response.json()


    # Successful registration is normally 200 or 201.
    assert response_json is not None

# def test_register_user_negative():
#
#     #Missing Password
#     payload = {
#         "email" : "student_negative@example.com"
#     }
#
#     response = APIUtils.post_request(
#         REGISTER_URL,
#         payload,
#         HEADERS
#     )
#
#     print("Status Code:", response.status_code)
#     print("Response:", response.text)
#
#     # Invalid request should result in a 4xx response.
#     assert 400<= response.status_code < 500