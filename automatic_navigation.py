import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
#the module sleep from time library allows to add a delay timer in our script.
from time import sleep

class NavigationTest(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get(r'https://google.com')

    def test_browser_navigation(self):
        driver = self.driver
        #In the google.com page we identify the search field by it's name, then we type the searching text and submit it
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('soskil se la come')
        search_field.submit()

        #the sleep module it's not recommended because it makes longer the execute time of the script.
        #it only be used when we need to see how the scripts works.
        #Never use it in production
        sleep(3)
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)