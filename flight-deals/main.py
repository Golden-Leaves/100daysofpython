#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    
    ORIGIN_LOCATION_CODE = "SGN"
    SENDER_EMAIL = os.getenv("SENDER_EMAIL_ACCOUNT")
    SENDER_EMAIL_APP_PASSWORD = os.getenv("SENDER_EMAIL_APP_PASSWORD")
    data_manager = DataManager()
    notification_manager = NotificationManager(SENDER_EMAIL,SENDER_EMAIL_APP_PASSWORD,data_manager.sheety_users_data)
    flight_search = FlightSearch(data_manager.sheety_prices_data,ORIGIN_LOCATION_CODE,notification_manager)
    data_manager.airport_codes = flight_search.all_cities_data
    data_manager.insert_airport_codes_sheety_data()
    flight_search.get_flight_prices()
    
    
if __name__ == "__main__":
    main()