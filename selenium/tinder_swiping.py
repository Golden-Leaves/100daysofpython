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
def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)
    email  = os.getenv("EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")
    phone_number = os.getenv("PHONE_NUMBER")
    
    if os.path.exists("tinder_swipes.txt"):
        with open("tinder_swipes.txt","r") as f:
            number_of_swipes = int(f.read())
            print("ok")
    else:
        with open("tinder_swipes.txt","w") as f:
            f.write("0")
            number_of_swipes = 0
            print("no")
            
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://tinder.com/")
    main_window = driver.current_window_handle
    time.sleep(1)
    log_in = driver.find_element(By.XPATH,value='//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
    log_in.click()
    time.sleep(2)
    more_options = driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_options.click()
    time.sleep(2)
    
    try:
        facebook_login = WebDriverWait(driver, 12.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'))
    )
        time.sleep(1)
    except TimeoutException:
        exit_button = driver.find_element(By.XPATH,'//*[@id="q369688754"]/div/div[1]/div[2]/button')
        exit_button.click()
        time.sleep(0.5)
        log_in.click()
        time.sleep(2)
        more_options = driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
        more_options.click()
        time.sleep(2)
        facebook_login = WebDriverWait(driver, 12.5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'))
    )
        time.sleep(1)
        
    driver.execute_script("arguments[0].click();", facebook_login)
    time.sleep(1)

    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            login_window = window
    driver.switch_to.window(login_window)
    email_input = driver.find_element(By.ID,value="email")
    email_input.send_keys(email)
    password_input = driver.find_element(By.ID,value="pass")    
    password_input.send_keys(email_password)
    login_confirm = driver.find_element(By.NAME,"login")
    login_confirm.click()
    time.sleep(2.5)
    continue_as_username = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label^="Continue"]'))
)
    continue_as_username.click()
    time.sleep(2)
    driver.switch_to.window(main_window)
    time.sleep(2)
    allow_location_tracking = driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
    allow_location_tracking.click()
    turn_off_notifications = driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
    turn_off_notifications.click()
    time.sleep(1)
    
    accept_cookies = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="q2098069830"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'))
)

    accept_cookies.click()
    time.sleep(5)
    while number_of_swipes % 100 != 0 or number_of_swipes == 0:
        time.sleep(1)
        try:
            x_button =WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".gamepad-icon-wrapper"))
            )
            x_button.click()

        except ElementClickInterceptedException:
            print("Closing pop-up... occurred, retrying...")
            not_interested = driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div/div[2]/button[2]')
            not_interested.click()
            time.sleep(2)
            continue
        number_of_swipes += 1
    #Records number of swipes(total)
    with open("tinder_swipes.txt","w") as f:
        f.write(number_of_swipes)
        print("Reached 100 swipes...")
        
            
    
if __name__ == "__main__":
    main()