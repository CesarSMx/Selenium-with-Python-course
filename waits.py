import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
#'By'class helps to reference elements of a website through it's 'selectors', not only for identify it but
#for interact with it in a different way from regular find_element_by.. methods.
from selenium.webdriver.common.by import By
#WebdriverWait allows us to use expectedConditions and explicit waits, for that we need import expectedConditions
#as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class explicitWaitTest(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get(r'http://demo-store.seleniumacademy.com')

    def test_account_link(self):
        #We are going to reference webdriver into webdriverwait and also tell him that waits 10 seconds maximum
        #until our espected conditions match. The conditions is implemented through a lambda function.
        #in this case, the function is to match as 3 the number(length attribute) of  options in the dropdown menu for selecting language.
        #English, French and German
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Now we define the account variable as the webdriver element identified by its Link Text, through an
        #expected condition 'visibility_of_element_located()', only if the webdriver find the element within 10 seconds. 
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self):
        #In this script we are going to made our way through the Create New Customer Account webpage, like in new_user.py file.
        #The difference is that now we are taking notice of time and giving an maximum of seconds for some lines to execute.

        
        self.driver.refresh()
        #this will open the menu
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #now we identify the option element 'My Account' from the previous identified menu and click it
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()
        #Now we wait a maximum of 20 seconds until we identify the button with its Link Text 'CREATE AN ACCOUNT' and click it
        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()
        #Now we wait 10 Seconds maximum until the webpage tittle displays the text 'Create New Customer Account'
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)