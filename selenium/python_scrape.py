from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def main():
    #TODO: find a way to bypass the capcha lol
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    print("siuuu")
    driver.get("https://python.org")
#     driver_whole =  WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
# )

#     driver_cents = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction"))
# )
#     print(f"{driver_whole.text}.{driver_cents.text}$")
    # query = driver.find_element(By.NAME, "q")
    # button = driver.find_element(By.ID,"submit")
    # link = driver.find_element(By.CSS_SELECTOR,".small-widget.documentation-widget p a")
    # xpath = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[2]')
    # lol = driver.find_element(By.CSS_SELECTOR, value="p")
    # print(lol)
    events_list = driver.find_element(By.CSS_SELECTOR, value=".medium-widget.event-widget.last .shrubbery .menu").text.split(f"\n")
    events_dict = {index:{events_list[i]:events_list[i+1]} for index,i in enumerate(range(0,len(events_list),2))}
    news_list = driver.find_element(By.CSS_SELECTOR, value=".medium-widget.blog-widget .shrubbery .menu").text.split(f"\n")
    news_dict = {index:{news_list[i]:news_list[i+1]} for index,i in enumerate(range(0,len(news_list),2))}
    
    print(f"Latest Events: {events_dict}\n")
    print(f"Latest News: {news_dict}\n")
    
    pass
    
if __name__ == "__main__":
    main()