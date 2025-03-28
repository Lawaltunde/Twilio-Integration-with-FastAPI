import requests

def getweather():

    # Fetching sudbury weather data and description
    weather_data = []
    city = "Sudbury"
    API_KEY = "4112c6619d2d55c92f12f83eeaa133a5"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    weather_data.append(f"{round(data['main']['temp'])} °C")
    weather_data.append(data['weather'][0]['main'])
    return weather_data