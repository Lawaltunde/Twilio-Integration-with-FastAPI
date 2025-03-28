import requests

def issInfo():
    overAllData = []
    url = "http://api.open-notify.org/astros.json"
    response = requests.request("GET", url)
    data = response.json()
    for individual in data["people"]:
        name = individual["name"]
        overAllData.append(name)
    overAllData.append(f"\nThey are {data['number']} in total")
    return overAllData
