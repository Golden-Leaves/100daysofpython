import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
from dotenv import load_dotenv
import os

def main():
    global print
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    SENDER_EMAIL =os.getenv("SENDER_EMAIL_ACCOUNT")
    SENDER_APP_PASSWORD = os.getenv("SENDER_EMAIL_APP_PASSWORD")
    RECEIVER_EMAIL = "letuongminh10@gmail.com"
    while True:
        try:
            headers = {"User-Ageent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                       "Accept-Language": "en-US,en;q=0.9",}
            item_URL = "https://www.amazon.com/JILANI-HANDICRAFT-Beanie-Accessory-Medium-Large/dp/B0BHDWZYRT/ref=sr_1_11?crid=1X5OG3HCLWEUV&dib=eyJ2IjoiMSJ9.onzRBZIYnCfzFlK3LZzajqRK-r87YjvHqKawv3QTOlEhEHFXPvg0QaCuz0eBJl52l0SNHb2YgQ_BZdCakOFWtgkaNS7qp_EvUj61j-JiJZh1xyI3S8ezBXRO_2Le_pPhmcikw0jXaCh0ZDyHiCpcjz4EMHu5oVVwmReg3NwHJ5T-aq0GFFLFMfYqCiOw7vrkrEDtMRRd0uz7rgOHVgUtkF98aJTWlGdHBR15PKSOyv4.BhrwmXa5gcnIrJsyPXUfMBX5dDva0fmFrW4wLmqEQyQ&dib_tag=se&keywords=anime&qid=1735133864&sprefix=anime%2Caps%2C393&sr=8-11"
            desired_price = float(input("Enter your desired price for the item (use dots'.'): "))
            response = requests.get(f"{item_URL}", headers=headers)
            amazon_webpage = response.text
            soup = BeautifulSoup(amazon_webpage,"html.parser")
            item_price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])
           
            item_name = soup.select_one(selector="div>h1>#productTitle").get_text(strip=True).replace("\n", " ").strip()
       
            
            if item_price < desired_price:
                formatted_message=(f"Subject: Amazon Price Alert\n\n{item_name} is now {item_price}$, which is {round(desired_price - item_price, 2)}$ lower than your desired price of {desired_price}$\n{item_URL}").encode("utf-8")
                print(formatted_message)
                

                with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                    connection.starttls()
                    connection.login(user = SENDER_EMAIL, password = SENDER_APP_PASSWORD)
                    connection.sendmail(to_addrs = RECEIVER_EMAIL, from_addr = SENDER_EMAIL,msg = formatted_message)
            print("DEBUG STOP")    
            
        except TypeError:
            print("Invalid price, pelase try again")
            continue
        break

if __name__ == "__main__":
    main()