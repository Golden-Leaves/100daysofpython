import smtplib
from dotenv import load_dotenv
import os
from data_manager import DataManager
class NotificationManager:
    def __init__(self,sender_email_account,sender_email_app_password,users_email) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_path = current_directory + r"\.env"
        load_dotenv(env_path)
        self.SENDER_EMAIL = os.getenv("SENDER_EMAIL_ACCOUNT")
        self.SENDER_EMAIL_APP_PASSWORD = os.getenv("SENDER_EMAIL_APP_PASSWORD")
        self.RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        self.users_email = users_email
        self.sender_email_account = sender_email_account
        self.sender_email_app_password  = sender_email_app_password
        self.formatted_flights_info = ""
        self.formatted_message = ""
    
        
    def add_message(self, departure_info, return_info, total_price,stops):
        # Consolidate all the flight data into one big blob
        self.message_contents = f"""
        Found cheap flight from {departure_info["departure_location"]} to {departure_info["arrival_location"]} with {stops} stops!
        Total Flight Price: {total_price} USD

        Departure Flight:
        - Departure Date: {departure_info['departure_date']}
        - Departure Time: {departure_info['departure_time']}
        - Departure Location: {departure_info['departure_location']}
        - Arrival Date: {departure_info['arrival_date']}
        - Arrival Time: {departure_info['arrival_time']}
        - Arrival Location: {departure_info['arrival_location']}

        Return Flight:
        - Departure Date: {return_info['departure_date']}
        - Departure Time: {return_info['departure_time']}
        - Departure Location: {return_info['departure_location']}
        - Arrival Date: {return_info['arrival_date']}
        - Arrival Time: {return_info['arrival_time']}
        - Arrival Location: {return_info['arrival_location']}
        \n\n
        """

        self.formatted_flights_info += self.message_contents
        
    def send_notification(self):
        #Send emails to all users subscribed
 
        print(self.formatted_flights_info)
        self.users_email_list = self.users_email["users"]
        for user in self.users_email_list:

            user_mail = user["whatIsYourEmail?"]
            user_first_name = f"Hi {user["whatIsYourFirstName?"]}! Below is your weekly report of cheap flights! \n"
            self.formatted_message = "Subject: Cheap Flights Tracker\n\n" + user_first_name + self.formatted_flights_info
            with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                connection.starttls()
                connection.login(user = self.SENDER_EMAIL, password = self.SENDER_EMAIL_APP_PASSWORD)
                connection.sendmail(to_addrs = user_mail, from_addr = self.SENDER_EMAIL,msg = self.formatted_message)
            print(f"Sent email to {user["whatIsYourEmail?"]} successfully!")
            

        
