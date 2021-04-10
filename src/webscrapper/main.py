from selenium import webdriver
# from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

driver.get(
    'https://www.worldometers.info/coronavirus/#countries')

# actions = ActionChains(driver)


def find_country(link_text):
    try:
        countryUSA = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text))
        )

        countryUSA.click()
    finally:
        time.sleep(5)
        driver.quit()


find_country('Brazil')
