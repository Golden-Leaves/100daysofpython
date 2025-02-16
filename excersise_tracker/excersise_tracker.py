import requests
import os
from dotenv import load_dotenv
import datetime
from requests.auth import HTTPBasicAuth
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    username = os.getenv("EXERCISE_TRACKER_NAME")
    password = os.getenv("EXERCISE_TRACKER_PASSWORD")
    sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    formatted_date = current_time.strftime("%d/%m/%Y")
    print(formatted_time,formatted_date)
    
    
    nutritionix_headers = {
        "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
        "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
    }
    
    nutritionix_parameters = {
        "query": "I walked at 6.2 km/h for  50 minutes with a total of 5.2km",
        "weight_kg": 76,
        "height_cm": 170,
        "age": 14,
    }
    
    nutritionix_response = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise",json = nutritionix_parameters, headers = nutritionix_headers)
    nutritionix_response.raise_for_status()
    nutritionix_data = nutritionix_response.json()
    print(nutritionix_data)
    
    sheety_headers = {
        "Content-Type": "application/json",
    }
    
    sheety_parameters = {
        "workout":{
            "date": formatted_date,
            "time": formatted_time,
            "exercise": nutritionix_data["exercises"][1]["user_input"],
            "duration": str(nutritionix_data["exercises"][0]["duration_min"]),
            "calories": nutritionix_data["exercises"][0]["nf_calories"],
        }
    }
   
    
    sheety_response = requests.post(url = sheety_endpoint, json = sheety_parameters,headers = sheety_headers,auth = HTTPBasicAuth(username,password))
    sheety_response.raise_for_status()
    print(sheety_response)
    

    
if __name__ == "__main__":
    main()