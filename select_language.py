import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select #this submodule is for properly inspect dropdown menu's

class LanguageOptions(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)

        driver.maximize_window()
        driver.get(r'http://demo-store.seleniumacademy.com')
		

    def test_select_language(self):
        driver = self.driver
        lang_options = ['English', 'French', 'German'] #list of languages in same order as the dropdown language list from webpage
        active_options = []

        select_language = Select(driver.find_element_by_id('select-language'))
        #Now we confirm that the amount of languages in the dropdown list is three.
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        #now we ensure that the language options obtained for the previous for statement are the same that the ones
        #we enlisted earlier before
        self.assertListEqual(lang_options, active_options)

        #We want to ensure that the selected language in the webpage is english, so
        self.assertEqual('English', select_language.first_selected_option.text)

        #To change the language in the webpage
        select_language.select_by_visible_text('German')

        #Now we verify that the page is in german. The one thing that change in the page is the url. 
        #After changing language to german, the url include this statement: 'store=german'
        self.assertTrue('store=german' in driver.current_url)

        #There is other way to change language through the index.
        select_language = Select(driver.find_element_by_id('select-language'))
        #We know that select_language now storage the dropdown menu as a list. Also we know that English is in
        #the first position, so we can select it through the index 0.
        select_language.select_by_index(0)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)