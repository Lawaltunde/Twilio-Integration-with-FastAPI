import json
from harryPotter import harrtPot
from openNotify import  issInfo
from weather import  getweather

def log_message():
    message = [harrtPot(), issInfo(), getweather()]
    """Log sent messages to a JSON file"""
    log_data = {"message": message}

    with open("sent_messages.json", "w") as file:
        json.dump(log_data, file)
        #file.write("\n")  # New line for each entry
