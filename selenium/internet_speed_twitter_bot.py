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
class InternetSpeedTwitterBot:
    def __init__(self):
        self.formatted_text = None
        self.promised_up = 10
        self.promised_down = 150
        self.download_speed = None
        self.upload_speed = None
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.env_path = self.current_directory + r"\.env"
        load_dotenv(self.env_path)
        self.email = os.getenv("EMAIL")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.phone_number = os.getenv("PHONE_NUMBER")
        self.account_username = os.getenv("ACCOUNT_USERNAME")

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.start_test = self.driver.find_element(By.CSS_SELECTOR,value=".js-start-test.test-mode-multi")
        self.start_test.click()
        time.sleep(25)
        #TODO: Turn all these into XPATHS
        
        while True:
            time.sleep(1.5)
            print("OMG")
            try:
                self.download_speed = WebDriverWait(self.driver,25).until(EC.presence_of_element_located((By.CSS_SELECTOR,".result-data-large number.result-data-value.download-speed")))
                self.upload_speed = WebDriverWait(self.driver,25).until(EC.presence_of_element_located((By.CSS_SELECTOR,".result-data-large number.result-data-value.upload-speed")))
                print("Done")
                self.driver.close()
                break

            
            except (ElementClickInterceptedException,TimeoutException):
                back_to_test_results = self.driver.find_element(By.CSS_SELECTOR, value='.notification-dismiss.close-btn')
                self.driver.execute_script("arguments[0].click();",back_to_test_results)
            finally:
                self.download_speed = float(WebDriverWait(self.driver,25).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))).text)
                self.upload_speed = float(WebDriverWait(self.driver,25).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text)
                print("Done")
                self.driver.close()
                break
        if self.download_speed <  self.promised_down or self.upload_speed < self.promised_up:
            self.formatted_text = f"""Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when i pay for {self.promised_down}down/{self.promised_up}up ? """
        elif self.download_speed > self.promised_down or self.upload_speed > self.promised_up:
            self.formatted_text = f"""Hey Internet Provider, my internet speed {self.download_speed}down/{self.upload_speed} is satisfactory, especially when i pay for {self.promised_down}down/{self.promised_up}up 😀. """
        return
            
                
                
   
