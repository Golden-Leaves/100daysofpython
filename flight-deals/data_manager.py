import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

class DataManager:
    def __init__(self) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_path = current_directory + r"\.env"
        load_dotenv(env_path)
        self.airport_codes  = None
        self.sheety_username = os.getenv("SHEETY_USERNAME")
        self.sheety_password = os.getenv("SHEETY_PASSWORD")
        self.sheety_headers = {
            "Content-Type": "application/json",
        }
        self.get_sheety_prices_data()
        self.get_customer_emails()
    def get_sheety_prices_data(self):
        self.sheety_get_response = requests.get(url = "https://api.sheety.co/f13a44eb8c045dcd421aac9c0c3ecfbb/flightDeals/prices",
                                            auth = HTTPBasicAuth(self.sheety_username,self.sheety_password))
        self.sheety_prices_data = self.sheety_get_response.json()
        print(self.sheety_prices_data)

        
    def insert_airport_codes_sheety_data(self):
      
        
                
        counter = 0
        for city in self.sheety_prices_data["prices"]:



            self.current_airport_code = self.airport_codes[counter]["data"] #self.airport_codes is a list, hence the counter
            

            self.sheety_put_parameters = {
            "price":{
                "iataCode": self.current_airport_code[0]["iataCode"], 
            },
            }
            self.row_id = city["id"]
            self.sheety_put_response = requests.put(url = f"https://api.sheety.co/f13a44eb8c045dcd421aac9c0c3ecfbb/flightDeals/prices/{self.row_id}",
                                                    headers = self.sheety_headers,
                                                    json = self.sheety_put_parameters,
                                                    auth = HTTPBasicAuth(self.sheety_username,self.sheety_password))
            counter += 1
            
    def get_customer_emails(self):
        self.sheety_get_response = requests.get(url = "https://api.sheety.co/f13a44eb8c045dcd421aac9c0c3ecfbb/flightDeals/users",
                                            auth = HTTPBasicAuth(self.sheety_username, self.sheety_password))
        self.sheety_users_data = self.sheety_get_response.json()
        print(self.sheety_users_data)

            

if __name__ == "__main__":
    data_manager = DataManager()
