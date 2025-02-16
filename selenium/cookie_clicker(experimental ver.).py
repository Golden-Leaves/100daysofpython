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
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID,value="cookie")
    store = [item.text for item in driver.find_elements(By.CSS_SELECTOR,value="#store b")]
  
    item_names_list = reversed([item.split(" - ")[0] for item in store if len(item) != 0  ])
    item_prices_list = reversed([item.split(" - ")[1].replace(",","") for item in store if len(item) != 0 ]) #Empty strings are falsy
    item_info_dictionary  = {name:int(price) for name,price in zip(item_names_list,item_prices_list)}#Important for price check logic
    print(item_info_dictionary)
    

        
    wait_time = 6.5
    timeout = time.time() + wait_time
    five_mins = time.time() + 300
    
    while time.time() < five_mins:
        cookie.click()
        if time.time() >= timeout:
            current_money = int(driver.find_element(By.ID,value="money").text.replace(",",""))
            for item in item_info_dictionary:
                #If price is lower than or equal to current funds
                if item_info_dictionary[item] <= current_money:
                    print("Buying...")
                    formatted_item_name = "buy" + item #Proper fomatting to match the one in source code
                    item_to_buy = driver.find_element(By.ID,value=f"{formatted_item_name}")
                    try:
                        item_to_buy.click()
                    except Exception:
                        print("Yes.")
                        
                
                
            timeout += wait_time
    print(f" Your final cookies/second value was {(driver.find_element(By.ID,value="cps").text.replace(",",""))} cookies/s")
        
    
            
if __name__ == "__main__":
    main()