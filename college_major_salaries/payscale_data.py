from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
    #Scroll so that the table is visible
    html = driver.find_element(By.TAG_NAME, "html")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight * 0.1", html)

    table_rows = driver.find_elements(By.TAG_NAME,value="tr")
    for row in table_rows:
        row_data = []
        major_cell = row.find_element(By.CSS_SELECTOR, ".data-table__cell.csr-col--school-name")
        others  = row.find_elements(By.CSS_SELECTOR,value=".data-table__cell.csr-col--right ")
        non_rank_cells= [major_cell] + others #others is a list lol
        for non_rank_cell in non_rank_cells:
            cell_value = non_rank_cell.find_element(By.CSS_SELECTOR,value=".data-table__value")
            row_data.append(cell_value)
        data.append(row_data)
    
  
    
if __name__ == "__main__":
    main()