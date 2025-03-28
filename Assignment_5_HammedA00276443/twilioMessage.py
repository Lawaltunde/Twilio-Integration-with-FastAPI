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

    #TWILIO_ACCOUNT_SID = "addYourSID" #add correct unique key, already removed for mine for security purpose
    #TWILIO_AUTH_TOKEN = "addYourTOKEN" #add correct unique key

    account_sid = "addYourSID" #add correct unique key
    auth_token = "addYourTOKEN" ##add correct unique key
    client =Client(account_sid, auth_token)

    message = client.messages.create(
        body= info,
        from_="+16573872606",
        to="+17059186763",
    )

    print(message.body)

    return "Ok"
