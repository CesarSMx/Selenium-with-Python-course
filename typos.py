import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Typos(unittest.TestCase):
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
        driver.find_element_by_link_text('Typos').click()
		
    def test_find_typos(self):  
        driver = self.driver
        correct_text = r"Sometimes you'll see a typo, other times you won't."
        text_to_check = driver.find_element_by_xpath(r'//*[@id="content"]/div/p[2]').text

        tries = 1
        while text_to_check != correct_text:
            driver.refresh()
            tries += 1
            text_to_check = driver.find_element_by_xpath(r'//*[@id="content"]/div/p[2]').text
        
        self.assertEquals(text_to_check, correct_text)
        print(f'It was needed {tries} tries to fix the typo.')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)