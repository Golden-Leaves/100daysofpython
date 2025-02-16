from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
from insta_follower import InstaFollower
from dotenv import load_dotenv
import os
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))        
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
   
    email  = os.getenv("EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    phone_number = os.getenv("PHONE_NUMBER")
    account_username = os.getenv("ACCOUNT_USERNAME")
    search_term = "Gordon Ramsay"
    insta_follower = InstaFollower()
    PAGE_LOAD_WAIT = 4
    insta_follower.login()
    time.sleep(PAGE_LOAD_WAIT)
    insta_follower.find_followers()
    time.sleep(PAGE_LOAD_WAIT)
    insta_follower.follow()
    


    
   
    
    while True:
        pass
    
    
if __name__ == "__main__":
    main()
  