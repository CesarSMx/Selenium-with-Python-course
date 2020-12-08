import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DynamicControls(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get(r'https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        #Disabling and enablig checkboxes
        driver = self.driver
        checkbox = driver.find_element_by_xpath(r'//*[@id="checkbox"]/input[@type="checkbox"]')
        checkbox.click()
        remove_button = driver.find_element_by_xpath(r'//*[@id="checkbox-example"]/button')
        remove_button.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "message")))
        add_button = driver.find_element_by_xpath(r'//*[@id="checkbox-example"]/button')
        add_button.click()
        checkbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'checkbox')))
        checkbox.click()
        
        #enablid text input and disabilng it
        enable_button = driver.find_element_by_xpath(r'//*[@id="input-example"]/button')
        enable_button.click()
        WebDriverWait(self.driver, 5).until(lambda s: s.find_element_by_xpath(r'//*[@id="input-example"]/input').is_enabled() == True)
        text_field = driver.find_element_by_xpath('//*[@id="input-example"]/input')
        text_field.send_keys('Platzi')
        disable_button = driver.find_element_by_xpath(r'//*[@id="input-example"]/button')
        disable_button.click()
        WebDriverWait(self.driver, 5).until(lambda s: s.find_element_by_xpath(r'//*[@id="input-example"]/input').is_enabled() == False)
        print('Test finished succesfully')







    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)