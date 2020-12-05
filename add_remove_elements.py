import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

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
        driver.get('https://the-internet.herokuapp.com/')
		
    def test_add_remove(self):
        driver = self.driver
        driver.find_element_by_link_text('Add/Remove Elements').click()


        elements_to_add = int(input('How many elements do you want to create?: '))
        elements_to_delete = int(input('How many elements do you want to delete?: '))
        add_button = driver.find_element_by_xpath(r'//*[@id="content"]/div/button')

        for i in range(elements_to_add):
            add_button.click()
        sleep(2)
        for i in range(elements_to_delete):
            try:
                delete_button = driver.find_element_by_xpath(r'//*[@id="elements"]/button[1]')
                delete_button.click()
                sleep(0.5)
            except:
                print('There is no element to delete')

        if elements_to_add-elements_to_delete > 0 :
            print(f'There are {elements_to_add-elements_to_delete} elements left')
        else:
            print(f'There are {0} element left')
            


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)