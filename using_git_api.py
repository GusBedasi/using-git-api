import requests
from requests.auth import HTTPBasicAuth
import sys
import json


def getUserData(user):

    baseURL = "https://api.github.com/users/"

    req = requests.get(baseURL + user, auth=HTTPBasicAuth('username', 'password'))

    """#print(req.headers)
        print(req.text)
        print(req.encoding)
        print(req.json())
    """

    if req.status_code == 200:
        json_data = req.json()
        login = json_data["login"]
        name = json_data["name"]
        email = json_data["email"]
        location = json_data["location"]

        print("Login:", login) 
        print("Name:", name)
        print("E-mail:", email)
        print("Location:", location)
    elif req.status_code == 403:
        print("Requisition status code:", req.status_code, "Forbidden")
    elif req.status_code == 404:
        print("Requisition status code:", req.status_code, "Not found")

def follow(user):
    baseURL = "https://github.com/users/follow?target=" + user

    requests.post(baseURL, auth=HTTPBasicAuth('username', 'password'))

def unfollow(user):
    baseURL = "https://github.com/users/unfollow?target=" + user

    print(requests.post(baseURL, auth=HTTPBasicAuth('username', 'password')))

def main():
    if len(sys.argv) == 2:
        getUserData(sys.argv[1])
        unfollow(sys.argv[1])

main()