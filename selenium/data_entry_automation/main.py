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
from zillow_house_search import ZillowHouseSearch
def main():
    print(os.getcwd())
    current_directory = os.path.dirname(os.path.abspath(__file__))        
    env_path = current_directory + r"\.env"
    load_dotenv(env_path)

    zillow_house_search = ZillowHouseSearch()
    #zillow_house_search.login()
    zillow_house_search.get_buildings_info()
    zillow_house_search.fill_in_form()
    zillow_house_search.open_sheet()
#
if __name__ == "__main__":
    main()