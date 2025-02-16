import requests
from dotenv import load_dotenv
import os

def main():
    #api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
    load_dotenv()
    twilio_sid = os.getenv("twilio_account_sid")
    twilio_auth_token = os.getenv("twilio_auth_token")

    open_weather_parameters = {
        "appid" : os.getenv("twilio_api_key"),
        "lat" : os.getenv("current_latitude"),
        "lon": os.getenv("current_longitude"),
        "cnt": 4,
    }
    open_weather_response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast",params = open_weather_parameters)
    open_weather_response.raise_for_status()
    open_weather_data = open_weather_response.json()
    data_list = open_weather_data["list"]
    will_rain = False

    for timestamp in data_list :
       timestamp_data = timestamp["weather"][0]["id"]
       if timestamp_data < 700:
           will_rain = True
    #if will_rain:
        #client = Client(twilio_sid,twilio_auth_token)
        #message = client.messages.create(
    body="Come join us at stupid lol XDDDDDD",
    from_="+12348135171",
    to="+840966879978",

  
    

if __name__ == "__main__":
    main()