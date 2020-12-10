import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Tables(unittest.TestCase):
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
        driver.find_element_by_link_text('Sortable Data Tables').click()
		
    def test_sort_tables(self):  
        driver = self.driver

        data_table = [[] for i in range(5)]
        for i in range(5):
            data_table[i].append(driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span').text) 

            for j in range(4):
                raw_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                data_table[i].append(raw_data.text)
        print(data_table)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)