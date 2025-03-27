from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
    time.sleep(2)
    data = []
    table_headers = driver.find_elements(By.TAG_NAME,value="th")
    print([th.text for th in table_headers])
    with open("test.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([th.text for th in table_headers])
    print("Success")
    
if __name__ == "__main__":
    main()