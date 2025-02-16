from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#mp-topbanner #articlecount a").text
    print(f"There are {number_of_articles} articles on Wikipedia. ")
    featured_article = driver.find_element(By.CSS_SELECTOR, value="#mp-tfa p b")
    featured_article.click()
    if driver.current_url  != "https://en.wikipedia.org/wiki/Main_Page":
        search_icon = driver.find_element(By.CSS_SELECTOR,value="#p-search a") #Clicks twice because the search bar minimizes when you are reading an article
        search_icon.click()
    
        
    search_box = driver.find_element(By.NAME,value="search") 
    search_box.send_keys("python", Keys.ENTER)
    print(driver.get_cookies())

    while True:
        quit_ = input("Type anything to exit the program: ")
        return
if __name__ == "__main__":
    main()