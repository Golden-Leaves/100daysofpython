from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
from dotenv import load_dotenv
import os
class InstaFollower:
    def __init__(self):
        # Set up the environment variables
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env_path = current_directory + r"\.env"
        load_dotenv(env_path)
        
        # Load variables from .env file
        self.email = os.getenv("EMAIL")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.phone_number = os.getenv("PHONE_NUMBER")
        self.account_username = os.getenv("ACCOUNT_USERNAME")
        self.account_name = "chefsteps"
        self.insta_follower = None
        self.PAGE_LOAD_WAIT = 4
        self.instagram_account = f"https://www.instagram.com/{self.account_name}/followers/"
        

        # Set up Chrome WebDriver options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://instagram.com")
    
    def login(self):
        time.sleep(self.PAGE_LOAD_WAIT)
        username_login = self.driver.find_element(By.NAME, value="username")
        username_login.send_keys(self.account_username)
        password_login = self.driver.find_element(By.NAME, value="password")
        password_login.send_keys(self.email_password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        time.sleep(self.PAGE_LOAD_WAIT)
        #Setup
        #Close the pop-ups
        try:
            not_now = self.driver.find_element(By.XPATH, "//div[@role='button' and contains(text(), 'Not now')]")
            not_now.click()
        except NoSuchElementException:
            print("Skipping...")
    
       
            
    def find_followers(self):
        while True:
                
                self.driver.get(self.instagram_account)
                time.sleep(self.PAGE_LOAD_WAIT)
                current_url = self.driver.current_url
                if current_url != self.instagram_account:
                    continue_program = input("Detected unwanted pop-up, resolve it then press any key to continue.")
                    continue
                followers_link= self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")
                
                followers_link.click()
                time.sleep(self.PAGE_LOAD_WAIT)
                #/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
                #/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]
                followers_scrollbar = self.driver.find_elements(By.CSS_SELECTOR,"div[role='dialog'] div[style='max-height: 400px; min-height: 200px;'] div")[-1]
                all_followers = followers_scrollbar.find_elements(By.XPATH,"./*")
                
                for i in range(10):#This is needed because the element dynamically loads, it doesnt show the full scrollbar all at once
                    print(f"scroll{i}")
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",all_followers)#This just scrolls to the bottom of the element
                    time.sleep(2)
                break

        
    def follow(self):
        pass