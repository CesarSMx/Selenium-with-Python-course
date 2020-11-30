import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        #Now we looking for the "create user" button
        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        #Now we do a quick assertion to verify that the button is displayed and enabled.
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        #before identify and fill the textboxes, we verify that we are located in the right page with 
        #an assertion
        self.assertTrue('Create New Customer Account', driver.title)
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password') 
        confirm_password = driver.find_element_by_id('confirmation')
        newsletters = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        #Now we need to confirm that the elements are enabled to proceed to fill them.

        self.assertTrue(first_name.is_enabled() and
        middle_name.is_enabled() and
        last_name.is_enabled() and
        email_address.is_enabled() and
        password.is_enabled() and
        confirm_password.is_enabled() and
        newsletters.is_enabled() and
        submit_button.is_enabled())

        #With the method 'send_keys()' we can write text into the textboxes.
        first_name.send_keys('fname_test')
        #driver.implicitly_wait(2)
        middle_name.send_keys('mname_test')
        #driver.implicitly_wait(2)
        last_name.send_keys('lname_test')
        #driver.implicitly_wait(2)
        email_address.send_keys('email@testingemail.com')
        #driver.implicitly_wait(2)
        password.send_keys('password_test')
        #driver.implicitly_wait(2)
        newsletters.click()
        #driver.implicitly_wait(100)
        driver.implicitly_wait(30)
        submit_button.click()


if __name__ == "__main__":
	unittest.main(verbosity = 2)