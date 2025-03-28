from twilio.rest import Client
from harryPotter import harrtPot
from weather import getweather
from openNotify import issInfo


def sendMessage():
    harr = harrtPot()
    weather = getweather()
    iss = issInfo()

    info = (f"\nDetails of the first Harry Potter character, including their name, gender, and eye color: {harr[0]}\n"
            f"\nThe present temperature in Sudbury, Canada, along with its weather conditions: {weather}\n"
            f"\nThe names of people currently in space and the total number of them: {iss}")

    #TWILIO_ACCOUNT_SID = "ACf828ffaa242c44d5cb5ed5efa5360a20"
    #TWILIO_AUTH_TOKEN = "da3d1fc6e7a18e0315ddcb8f55db5e88"

    account_sid = "ACf828ffaa242c44d5cb5ed5efa5360a20"
    auth_token = "da3d1fc6e7a18e0315ddcb8f55db5e88"
    client =Client(account_sid, auth_token)

    message = client.messages.create(
        body= info,
        from_="+16573872606",
        to="+17059186763",
    )

    print(message.body)

    return "Ok"
