import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

t = 5

class BaseTest(unittest.TestCase):

    def setUp(self):  # ✅ Nombre correcto
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test1(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()


    def tearDown(self):  # ✅ Se ejecuta al final del test
        time.sleep(t)
        self.driver.quit()





if __name__ == '__main__':
    unittest.main()
