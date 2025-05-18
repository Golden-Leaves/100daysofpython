from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://github.com/Golden-Leaves/100daysofpython/tree/master")
    sleep(1)
    repo_links = driver.find_elements(By.CSS_SELECTOR,".Link--primary")#Selectors also need quotes
    print([f"{repo_link.get_attribute('href')}"  for repo_link in repo_links])
if __name__ == "__main__":
    main()