from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from exceptions import IncorrectPassword
from internet_speed_twitter_bot import InternetSpeedTwitterBot
from urllib3.exceptions import ReadTimeoutError
import time
from dotenv import load_dotenv, set_key
import os
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    email  = os.getenv("EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    phone_number = os.getenv("PHONE_NUMBER")
    account_username = os.getenv("ACCOUNT_USERNAME")
    internet_speed_twitter_bot = InternetSpeedTwitterBot()
    internet_speed_twitter_bot.get_internet_speed()

    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(r"https://x.com/i/flow/login")
    except ReadTimeoutError:
        time.sleep(15)
    time.sleep(10)
    

    
    enter_email = WebDriverWait(driver,25).until(EC.presence_of_element_located((By.NAME,"text")))    
    enter_email.click()
    enter_email.send_keys(email)
    
    
    time.sleep(1)
    next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
    next_button.click()
    time.sleep(1)
    #Handles potential captcha/verification interruptions, or wrong passwords
    while True:
        time.sleep(2)
        try:
            #Try to log in
            while True:
                enter_password = driver.find_element(By.NAME,value="password")
                enter_password.send_keys(email_password)
                login = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
                
                login.click()
                time.sleep(1)
                #Handles wrong passwords
                try:
                    if login.get_attribute("aria-disabled") == "true":
                        new_password = input("Your current password seems to be wrong, please enter a new one.")
                        confirm_password = input(f"Are you sure your new password is {new_password}?('y' for yes; anything else for no)").lower()
                        if confirm_password == "y":
                            set_key(env_path,"EMAIL_PASSWORD",new_password)
                        else:
                            continue
                except StaleElementReferenceException:
                    break
                
            break
        except NoSuchElementException:#Unusual login acc
            time.sleep(1)
            enter_username = driver.find_element(By.NAME,value="text")
            enter_username.send_keys(account_username)
            next_button_1 = driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            next_button_1.click()
            
    #X obfuscation shenanigans
    #Post a tweet
    time.sleep(5)
    compose_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
    compose_click.click()
    compose_text = driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')
    compose_text.send_keys(internet_speed_twitter_bot.formatted_text)
    post_button  = driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    post_button.click()
    print("Done!")
    driver.close()
    return
        
        
    
    
    
    
if __name__ == "__main__":
    main()