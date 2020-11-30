
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)
		

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)