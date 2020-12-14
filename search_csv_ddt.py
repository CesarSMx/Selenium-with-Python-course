import csv, unittest
from ddt import ddt, data, unpack #installation of this library is required 'pip install ddt'
from pyunitreport import HTMLTestRunner
from selenium import webdriver

#this function was writen to read the csv file and return the data
#as a list of tuples
def csvRead():
        data = []
        counter = 0
        with open('testdata.csv', newline='') as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',')
            for row in dataReader:
                if counter == 0:
                    pass
                else:
                    data.append((f'{row[0]}', int(row[1])))
                counter+=1
        return data


@ddt
class searchDDT(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get('http://demo-store.seleniumacademy.com/')
	
    #The * before the method csvRead() tells the interpreter to read each one of tuples 
    # returned as an individual argument instead of a list of tuples
    @data(*csvRead()) 
    @unpack

    def test_search_ddt(self, search_value, expected_count):  
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        items = driver.find_elements_by_xpath('//li[@class="item last"]')
        print(f'Items found: {len(items)}')

        self.assertEqual(len(items), expected_count)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)