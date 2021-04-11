from os import name
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


PATH = './chromedriver'
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get(
    'https://news.google.com/covid19/map?hl=en-CA&mid=%2Fm%2F02j71&gl=CA&ceid=CA%3Aen')

actions = ActionChains(driver)


class Country():
    def __init__(self, name, totalcases, deaths) -> None:
        self.name = name
        self.totalcases = totalcases
        self.deaths = deaths

    def display(self):
        return self.name, self.totalcases, self.deaths


def find_country_data():
    try:
        country_totalcases_found = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'l3HOY'))
        )

        array = []
        countries_list = []

        for country in country_totalcases_found:
            array.append(country.text)

        chunks = [array[x:x+6] for x in range(0, len(array), 6)]
        counter = 0
        for i in chunks:
            country = Country(i[0], i[1], i[5])
            countries_list.append(country)
            counter += 1

        for country in countries_list:
            print(country.display())

        # print(chunks)
        # print(country_table_found[3].text.split(' '))

        # country_found = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, 'pH8O4c'))
        # )

        # for country in country_found:

        # country_found.click()
        # driver.back()

    finally:
        # pass
        # time.sleep(5)
        driver.quit()


# for country in countries:
#     find_country_data(country)


find_country_data()
