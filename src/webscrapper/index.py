from selenium import webdriver
import requests

# PATH = './chromedriver'

# driver = webdriver.Chrome(PATH)
# driver.get('https://www.worldometers.info/coronavirus/#countries')
# driver.quit()


country_name = 'canada'

try:
    res = requests.get(
        f'https://restcountries.eu/rest/v2/name/{country_name}')
    # print(res.json())

    for country in res.json():
        print('Name: ' + country['name'])
        print('Area: ' + str(country['area']))
        print('Population: ' + str(country['population']))
        print('Flag Link: ' + country['flag'])

except requests.exceptions.HTTPError as errHTTP:
    print(errHTTP)
except requests.exceptions.ConnectionError as errCon:
    print(errCon)
except requests.exceptions.Timeout as errTimeout:
    print(errTimeout)
except requests.exceptions.RequestException as errReqExceptions:
    print(errReqExceptions)
