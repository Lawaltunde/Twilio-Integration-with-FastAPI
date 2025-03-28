import requests

def harrtPot():

    harryPotterData = []
    url = "https://hp-api.onrender.com/api/characters"
    response = requests.request("GET", url)
    data = response.json()
    for potter in data:
        if potter["hairColour"] is None:
            potter["hairColour"] = "Note available"
        item = [potter["name"], potter["gender"], potter["hairColour"]]
        harryPotterData.append(item)
    return harryPotterData