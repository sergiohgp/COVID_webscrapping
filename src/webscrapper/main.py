from os import name
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# from country import Country
import requests

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


PATH = './chromedriver'
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get(
    'https://news.google.com/covid19/map?hl=en-CA&mid=%2Fm%2F02j71&gl=CA&ceid=CA%3Aen')

actions = ActionChains(driver)

country_name = 'canada'


def api_get(country_name):
    try:
        res = requests.get(
            f'https://restcountries.eu/rest/v2/name/{country_name}')

        for country in res.json():
            if not isinstance(country, str):
                return country['name'], country['area'], country['population'], country['flag']
                # print('Name: ' + country['name'])
                # print('Area: ' + str(country['area']))
                # print('Population: ' + str(country['population']))
                # print('Flag Link: ' + country['flag'])
                # print()
            else:
                pass

    except requests.exceptions.HTTPError as errHTTP:
        print(errHTTP)
    except requests.exceptions.ConnectionError as errCon:
        print(errCon)
    except requests.exceptions.Timeout as errTimeout:
        print(errTimeout)
    except requests.exceptions.RequestException as errReqExceptions:
        print(errReqExceptions)


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
            print(api_get(i[0]))
            # print(i[0])

        print(f'Number of scrapped countries: {str(counter)}.')

        # for country in countries_list:
        #     print(country.display())

    finally:
        driver.quit()


# for country in find_country_data():
#     api_get(country[0])
find_country_data()
# api_get(country_name)
