import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file




class DataManager:

    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_path = current_directory + r"\.env"
        load_dotenv(env_path)
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.sheety_headers = {
            "Content-Type": "application/json",
        }

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url="https://api.sheety.co/9d35800cc93cd9e88b948de3cc435447/flightDeals/prices",auth = self._authorization)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/9d35800cc93cd9e88b948de3cc435447/flightDeals/prices/{city['id']}",
                json=new_data,
                auth = self._authorization
            )
            print(response.text)
if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_destination_data()
    data_manager.update_destination_codes()