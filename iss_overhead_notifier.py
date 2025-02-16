import requests
import datetime as dt
import time
import smtplib
def main():
    used_gmail_account = "minhtuongle10@gmail.com"
    python_mail_password = "bnpj qcfy pglc pzmz"
            
    
    geolocation_response = requests.get(url = 'https://api.ipgeolocation.io/ipgeo?apiKey=50004833fa7f4c0f963c561d2188bfc9')
    geolocation_data = geolocation_response.json()
    current_location_latitude = float(geolocation_data["latitude"])
    current_location_longitude = float(geolocation_data["longitude"])
    print(current_location_latitude,current_location_longitude)
    
             
    while True:
        time.sleep(60)
        is_within_observable_distance = None
        current_time = dt.datetime.now()
        current_time_hour = current_time.hour
        current_time_minute = current_time.minute
        

        sunrise_sunset_parameters = {"lat": str(current_location_latitude),
    "lng" : str(current_location_longitude),
    "tzid":"Asia/Ho_Chi_Minh",
    "formatted": "0"
    }
        sunrise_sunset_response = requests.get(url = "https://api.sunrise-sunset.org/json",params = sunrise_sunset_parameters)
        sunrise_sunset_data = sunrise_sunset_response.json()
        sunrise_time = sunrise_sunset_data["results"]["sunrise"]
        sunset_time = sunrise_sunset_data["results"]["sunset"]
        formatted_sunset_time = sunset_time.split("T")
        sunset_time_hour = int(formatted_sunset_time[1].split(":")[0])
        sunset_time_minute = int(formatted_sunset_time[1].split(":")[1])
        print(sunset_time_hour,sunset_time_minute)

        iss_response = requests.get(url = "http://api.open-notify.org/iss-now.json#")
        iss_response.raise_for_status()
        data = iss_response.json()
        iss_longitude = float(data["iss_position"]["longitude"])
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_position = (iss_latitude,iss_longitude)
        print(iss_position)
        
        def is_observable():
            if abs(current_location_latitude - iss_position[0]) <= 5 and abs(current_location_longitude - iss_position[1]) <= 5:
                return True
        
        def is_night():
            if sunset_time <= current_time_hour or sunrise_time >= current_time_hour:
                return True

        if is_observable() and is_night():
            with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                connection.starttls()
                connection.login(user = used_gmail_account, password = python_mail_password)
                connection.sendmail(from_addr = used_gmail_account, to_addrs = "letuongminh10@gmail.com", msg = "Subject: ISS overhead\n\n Come out and view the ISS now lol." )

if __name__ == "__main__":
    main()