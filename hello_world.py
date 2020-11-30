# sudo apt update
# apt install python3-pip
# pip3 install selenium
# pip3 install pyunitreport
# apt install chromium-chromedriver

# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HelloWorld(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
        driver_path = r'/mnt/c/Users/cesar/Documents/desarrollo/Selenium/chromedriver.exe'
        brave_path = r'C:\program Files\braveSoftware\brave-browser\application\brave.exe'

        option = webdriver.ChromeOptions()
        option.binary_location = brave_path

        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        driver = cls.driver
		# esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
		
	# Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))