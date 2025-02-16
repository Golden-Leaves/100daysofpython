from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
from dotenv import load_dotenv
import os
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    email  = os.getenv("EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    phone_number = os.getenv("PHONE_NUMBER")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(r"https://www.linkedin.com/")
    email_login_link  = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='login']")))#"[]" for attribute syntax, href*="{string}" find a href attribute with that substring in the link
    email_login_link.click()
    time.sleep(1.5)#Wait for website to load
    username = driver.find_element(By.ID,value="username")
    password = driver.find_element(By.ID,value="password")
    submit = driver.find_element(By.CSS_SELECTOR,value="button[type='submit']")
    username.send_keys(email)
    password.send_keys(email_password)
    submit.click()
    time.sleep(10)
    time.sleep(1)
    filtered_link = driver.get(r"https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
    time.sleep(2)
    SCROLL_PAUSE = 0.5
    scrollbar = driver.find_element(By.CSS_SELECTOR,value=".hIAMCqpFeYcVjeOPoulLoCCKJjLsx")
   

    while True:
        time.sleep(1)
        all_job_listings = driver.find_elements(By.CSS_SELECTOR,value=".rjmNTMLkNvPwnJnFTCybgSFpgYGQ li")
        print(all_job_listings)
        for job_listing in all_job_listings:
            time.sleep(SCROLL_PAUSE)
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", scrollbar)
               
                job_listing.click()
                easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
                easy_apply.click()
   
                phone_number_input = driver.find_element(By.CLASS_NAME,value="artdeco-text-input--input")
                phone_number_input.send_keys(phone_number)
                next = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))
)
                time.sleep(0.5)
                next.click()
                time.sleep(0.5)
                review_application = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")))
                review_application.click()
                submit_application = driver.find_element(By.CSS_SELECTOR,value=".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
                submit_application.click()    


            except (NoSuchElementException or ElementClickInterceptedException):
                print("Complex application process/already applied, switching to other applications...")
            
    while True:
        pass


   
if __name__ == "__main__":
    main()