from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    first_name = driver.find_element(By.NAME,"fName")
    last_name = driver.find_element(By.NAME,"lName")
    email = driver.find_element(By.NAME,"email")
    submit = driver.find_element(By.CSS_SELECTOR,value=".form-signin button")
    first_name.send_keys("Cinders")
    last_name.send_keys("Golden_Leaves")
    email.send_keys("letuongminh10@gmail.com")
    submit.click()
    
    while True:
        quit_ = input()
        return
if __name__ == "__main__":
    main()