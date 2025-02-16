from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    english_language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#promptContentChangeLanguage #langSelect-EN"))
    )
    english_language.click()
    try:
        cookie = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#cookieAnchor #bigCookie"))
        )
        bakery_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bakeryName"))
        )
       
    except Exception:
          cookie = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#cookieAnchor #bigCookie"))
        )
          bakery_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bakeryName"))
        )
    finally:
        bakery_name.click()
        bakery_name_input = driver.find_element(By.ID,"bakeryNameInput")
        bakery_name_input.send_keys("Stupid lol XDDDDD")
        bakery_name_confirm = driver.find_element(By.ID,value="promptOption0")
        bakery_name_confirm.click()
        timeout = time.time() + 5 #5 seconds from current time
        
    
    while True:
    
        cookie.click()
        if time.time() >= timeout:
        
            first_upgrade = driver.find_element(By.CSS_SELECTOR,value="#upgrades crate.upgrade.enabled") #Purchases the cheapest upgrade every 5 seconds
            all_products_enabled = driver.find_elements(By.CSS_SELECTOR,"#products product.unlocked.enabled")
            first_upgrade.click()
            
            timeout += 5
        
      
    
   
if __name__ == "__main__":
    main()