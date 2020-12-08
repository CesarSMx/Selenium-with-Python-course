import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
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
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        unsorted_list = driver.find_element_by_xpath(r'//*[@id="content"]/div/ul').find_elements_by_tag_name('li')
        counter = 1
        while(len(unsorted_list) != 5):
            sleep(1)
            counter+=1
            driver.refresh()
            unsorted_list = driver.find_element_by_xpath(r'//*[@id="content"]/div/ul').find_elements_by_tag_name('li')
        else:
            print(f'It was needed {counter} refreshes')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)