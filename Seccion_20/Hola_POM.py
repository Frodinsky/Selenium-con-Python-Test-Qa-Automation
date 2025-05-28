from selenium import webdriver
from Aprendiendo_funciones_POM.POM_Funciones import LoginPage
import  unittest
import time

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.POM_Funciones = LoginPage(self.driver)


    def test1(self):
        self.POM_Funciones.login("standard_user", "secret_sauce")
        self.assertTrue(self.POM_Funciones.is_login_successful())
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




