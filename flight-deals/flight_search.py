import requests
from dotenv import load_dotenv
import os
import datetime
from notification_manager import NotificationManager

class FlightSearch:

    def __init__(self,sheety_data,origin_destination_code,notification__manager: NotificationManager) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_path = current_directory + r"\.env"
        load_dotenv(env_path)
        SENDER_EMAIL = os.getenv("SENDER_EMAIL_ACCOUNT")
        SENDER_EMAIL_APP_PASSWORD = os.getenv("SENDER_EMAIL_APP_PASSWORD")
        RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        
        
    
        self.unformatted_message = []
        self.origin_destination_code = origin_destination_code
        self.today = datetime.datetime.today() 
        self.tomorrow = (self.today + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
        self.all_cities_data = []
        self.return_flight_information_list = []
        self.departure_flight_information_list = []
        self.cities_data = None
        self.sheety_data = sheety_data
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.amadeus_token = ""
        self.amadeus_headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "Authorization": None,
        }
       
        self.notification_manager = notification__manager
        self.get_token()
        self.get_city_airport_codes()
        
    def get_token(self):

            self.amadeus_security_parameters = {
                "grant_type": "client_credentials",
                "client_id": self.amadeus_api_key,
                "client_secret": self.amadeus_api_secret,
            }
            
            self.amadeus_security_response = requests.post(url = "https://test.api.amadeus.com/v1/security/oauth2/token",data = self.amadeus_security_parameters, headers = self.amadeus_headers)
            self.amadeus_security_response.raise_for_status()
            self.amadeus_security_data = self.amadeus_security_response.json()
            self.amadeus_headers["Authorization"] = f"Bearer {self.amadeus_security_data["access_token"]}"
            print(self.amadeus_headers["Authorization"])
            
    def get_city_airport_codes(self):

        for city in self.sheety_data["prices"]: #Everything included in the sheet ("prices" is just the root name)
           self.city_name_unformatted = city["city"].split(" ")
           self.city_name_formatted = self.city_name_unformatted[0].capitalize()
           self.amadeus_city_parameters = {
               "keyword": self.city_name_formatted,
           }
           self.cities_response = requests.get(url = "https://test.api.amadeus.com/v1/reference-data/locations/cities", params = self.amadeus_city_parameters, headers = self.amadeus_headers )
           self.cities_response.raise_for_status()
           self.cities_data = self.cities_response.json()
           self.all_cities_data.append(self.cities_data)
        
    
    def get_flight_prices(self):
        counter = 0
        for city in self.all_cities_data:
            self.flight_price_factor = 1
            self.current_airport_code = city["data"][0]["iataCode"]#Takes the iataCode of the current iteration
            print(self.current_airport_code)
            
            flight_offers_parameters = {
                "originLocationCode": self.origin_destination_code,
                "destinationLocationCode": self.current_airport_code,
                "departureDate": self.tomorrow,
                "returnDate": (datetime.datetime.today() + datetime.timedelta(days = 182)).strftime("%Y-%m-%d"),
                "travelClass": "ECONOMY",
                "nonStop": "true",
                "currencyCode": "USD",
                "max": "10",
                "adults": "1",   
            }
            flight_offers_response = requests.get(url = "https://test.api.amadeus.com/v2/shopping/flight-offers", params = flight_offers_parameters,headers = self.amadeus_headers)
            flight_offers_response.raise_for_status()
            flight_offers_data = (flight_offers_response.json())["data"]

            if len(flight_offers_data) == 0:  # If no flights are found, try with indirect flights
                flight_offers_parameters["nonStop"] = "false"
                flight_offers_response = requests.get(url = "https://test.api.amadeus.com/v2/shopping/flight-offers", params = flight_offers_parameters,headers = self.amadeus_headers)
                flight_offers_response.raise_for_status()
                flight_offers_data = (flight_offers_response.json())["data"]
                print(flight_offers_data)
                
                
                if len(flight_offers_data) == 0:
                    print(f"No flights found for {self.current_airport_code}")
                    continue
                    
            else: #Direct flights
                self.flight_price_factor = 1
                
            for flight in flight_offers_data: 
                            
                # total_flights_list = [len(flight["segments"]) for flight in flight_offers_data[counter]["itineraries"]]
                # total_flights  = sum(total_flights_list) 
                total_flights = len(flight["itineraries"][0]["segments"]) + len(flight["itineraries"][1]["segments"]) #itineraries always has 2 elements, the return and the arrival flights
                    
                if total_flights - 2 != 0:
                    #flight_offers_data is a list with one element for some reason, hence the [0] at the start
                    #We are finding the factor if the trip has stops, and will ONLY account for those stops, you need to have minimum 2 flights if a trip has no stops right?
                    self.flight_price_factor = 1 - ((total_flights - 2) * 0.1)  #No stops is 1, one stop is 0.9,.etc
                    print(f"Flights with stops for {self.current_airport_code} found...")
                    
                    
                print(f"Flights with no stops for {self.current_airport_code} found! ")
                total_flight_prices_modified = float(flight["price"]["total"]) * self.flight_price_factor #This will account for flights with multiple stops
                actual_total_flight_prices = flight["price"]["total"]
                # Return flight info
                # # Return flight info
                return_flight_first_segment = flight["itineraries"][1]["segments"][0]  # First segment of the return flight
                return_flight_last_segment = flight["itineraries"][1]["segments"][-1]  # Last segment of the return flight

                # Extract departure information from the first segment
                return_departure_date = return_flight_first_segment["departure"]["at"].split("T")[0]
                return_departure_time = return_flight_first_segment["departure"]["at"].split("T")[1]
                return_departure_location = return_flight_first_segment["departure"]["iataCode"]

                # Extract arrival information from the last segment
                return_arrival_date = return_flight_last_segment["arrival"]["at"].split("T")[0]
                return_arrival_time = return_flight_last_segment["arrival"]["at"].split("T")[1]
                return_arrival_location = return_flight_last_segment["arrival"]["iataCode"]

                self.return_flight_information = {
                    "departure_date": return_departure_date,
                    "departure_time": return_departure_time,
                    "departure_location": return_departure_location,
                    "arrival_date": return_arrival_date,
                    "arrival_time": return_arrival_time,
                    "arrival_location": return_arrival_location,
}
                
                # Departure flight info
                departure_flight_segment = flight["itineraries"][0]["segments"][0]
                departure_flight_last_segment = flight["itineraries"][0]["segments"][-1] #There might be multiple stops, so the arrival time will be the og destination's
                departure_departure_date = departure_flight_segment["departure"]["at"].split("T")[0]
                departure_departure_time = departure_flight_segment["departure"]["at"].split("T")[1]
                departure_departure_location = departure_flight_segment["departure"]["iataCode"]
                departure_arrival_date = departure_flight_last_segment["arrival"]["at"].split("T")[0]
                departure_arrival_time = departure_flight_last_segment["arrival"]["at"].split("T")[1]
                departure_arrival_location = departure_flight_last_segment["departure"]["iataCode"]

                self.departure_flight_information = {
                    "departure_date": departure_departure_date,
                    "departure_time": departure_departure_time,
                    "departure_location": departure_departure_location,
                    "arrival_date": departure_arrival_date,
                    "arrival_time": departure_arrival_time,
                    "arrival_location": departure_arrival_location,
                }

                #Adds to final message if flight is cheap enough
                if self.sheety_data["prices"][counter]["lowestPrice"] > float(total_flight_prices_modified):  #total_flight_prices_modified to account for stops
                    print("Found cheap flight!")
                    self.notification_manager.add_message(self.departure_flight_information,self.return_flight_information,actual_total_flight_prices,total_flights - 2)
                else:
                    print(f"Flight from {return_departure_location} to {return_arrival_location} is not sufficiently cheap")
            counter += 1           
        #This only gets sent after all the data is done 
        self.notification_manager.send_notification()
                    
 
                
   
           

           
        
if __name__ == "__main__":
    flight_search = FlightSearch()
    flight_search.get_city_airport_codes()

