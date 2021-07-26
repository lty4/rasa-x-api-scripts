import csv
import requests


def send_to_inbox(username, password, link):
    auth_api_string = link + "/api/auth"
    auth_json_str = {"username": username, "password": password}
    auth_token = requests.post(auth_api_string, json=auth_json_str)

    api_string = link + "/api/conversations/"

    with open('statements.csv', newline='') as statementfile:
        statementreader = csv.reader(statementfile, delimiter=',')
        for row in statementreader:
            full_api_string = api_string + "test/messages?" + auth_token
            json_str = {"message": row}
            conversation = requests.post(full_api_string, json=json_str)
            print("accepted")

    return


link = input("Please provide the URL to your Rasa X server.\n")
username = input("Username: ")
password = input("Password: ")

send_to_inbox(username, password, link)
