import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class CompareProducts(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        
        driver.maximize_window()
        driver.get(r'http://demo-store.seleniumacademy.com')

    def test_alert_manage(self):
        #In this lesson we learn how to accept or cancel an alert pop-up.
        #
        driver = self.driver
        search_field = driver.find_element_by_id('search')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

        self.assertEqual(r"Search results for: 'tee'", driver.title)
        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)