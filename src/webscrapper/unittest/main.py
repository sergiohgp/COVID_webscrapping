import page
from selenium import webdriver
import unittest
import time


class CovidDataSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../../chromedriver')
        self.driver.get('https://www.worldometers.info/coronavirus/#countries')

    def close(self):
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
