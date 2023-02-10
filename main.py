import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": "tokenization",
    "username": "cams",
    "notMinor": "yes",
    "agreeTermsOfService": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)


