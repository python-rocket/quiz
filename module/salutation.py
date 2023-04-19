import requests
import json


def get_salutation(name):
    url = f"https://api.genderize.io?name={name}"
    api_response = json.loads(requests.get(url).text)
    gender = api_response["gender"]
    if gender == "male":
        salutation = f"Mr. {name}"
    elif gender == "female":
        salutation = f"Ms. {name}"
    return salutation