import requests
from requests.auth import HTTPBasicAuth
import sys
import json

def getUserData(user):

    baseURL = "https://api.github.com/users/"

    req = requests.get(baseURL + user, auth=HTTPBasicAuth('teste', 'teste123'))

    if req.status_code == 200:
        json_data = req.json()
        following = json_data["following"]
        return following
    elif req.status_code == 403:
        print("Requisition status code:", req.status_code, "Forbidden")
    elif req.status_code == 404:
        print("Requisition status code:", req.status_code, "Not found")

def followThem(users):
    baseURL = "https://api.github.com/user/following/" + users
    req = requests.put(baseURL, auth=HTTPBasicAuth('teste', 'teste123'))
    print(req)

def getFollowers(user):
    following = getUserData(user)
    print(following)
    pages = following // 30
    
    for page in range(pages):
        baseURL = "https://api.github.com/users/"+ user+ "/following?page=" + str(page)
        req = requests.get(baseURL, auth=HTTPBasicAuth('teste', 'teste123'))
        json_data = req.json()
        counter = 0
        for people in range(1, 30):
            counter += 1
            users = json_data[people]["login"]
            print(users, counter)
            followThem(users)

def main():
    if len(sys.argv) == 2:
        getFollowers(sys.argv[1])

    else:
        print("")
        print("Parece que você não colocou um nome de usuário para procurarmos.")
        print("Sintaxe: python using_git_api.py <username>")
        sys.exit()
main()