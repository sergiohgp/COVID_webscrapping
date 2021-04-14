from os import name
from sys import api_version
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import requests
import pymongo
from bson.objectid import ObjectId

# Browser options
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


PATH = './chromedriver'
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get(
    'https://news.google.com/covid19/map?hl=en-CA&mid=%2Fm%2F02j71&gl=CA&ceid=CA%3Aen')

actions = ActionChains(driver)

# Connect to mongodb
client = pymongo.MongoClient('mongodb://localhost:27017/')
if client:
    DB = client['termproject']


def insert_documents_into_countries_country(document):
    col = DB['countries_country']
    if col:
        document_exists = col.find_one({'name': document['name']})
        if document_exists:
            col.delete_one({'name': document['name']})

        col.update_one(document, {'$set': document}, upsert=True)


def insert_documents_into_countries_covid_cases(document):
    col = DB['countries_covid_cases']
    if col:
        document_exists = col.find_one(
            {'country_name': document['country_name']})
        if document_exists:
            col.delete_one({'country_name': document['country_name']})

        col.update_one(document, {'$set': document}, upsert=True)


def api_get(country_name):
    try:
        res = requests.get(
            f'https://restcountries.eu/rest/v2/name/{country_name}').json()

        if type(res) is list:
            if len(res) > 1:
                return res[1]['population'], res[1]['flag'], res[1]['area']
            else:
                return res[0]['population'], res[0]['flag'], res[0]['area']
        else:
            return False

    except requests.exceptions.HTTPError as errHTTP:
        print(errHTTP)
    except requests.exceptions.ConnectionError as errCon:
        print(errCon)
    except requests.exceptions.Timeout as errTimeout:
        print(errTimeout)
    except requests.exceptions.RequestException as errReqExceptions:
        print(errReqExceptions)


def find_country_data():
    try:
        country_totalcases_found = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'l3HOY'))
        )

        array = []

        for country in country_totalcases_found:
            array.append(country.text)

        chunks = [array[x:x+6] for x in range(0, len(array), 6)]
        counter = 0
        for i in chunks:
            api_object = api_get(i[0])

            if api_get(i[0]):
                document_country = {
                    'id': i[0] + '_' + str(counter),
                    'name': i[0],
                    'population': api_object[0],
                    'flag': api_object[1],
                    'area': api_object[2]
                }

                document_covid_cases = {
                    'id': i[0] + '_' + str(counter),
                    'country_name': i[0],
                    'total_cases': i[1],
                    'new_cases': i[2],
                    'total_deaths': i[5]
                }

                insert_documents_into_countries_country(document_country)

                insert_documents_into_countries_covid_cases(
                    document_covid_cases)

                print(document_country)
                print(document_covid_cases)
                print()
                counter += 1

        print(f'Number of scrapped countries: {str(counter)}.')

    finally:
        driver.quit()


find_country_data()
