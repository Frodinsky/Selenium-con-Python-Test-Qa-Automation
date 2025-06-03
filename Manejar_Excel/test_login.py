import unittest
from selenium import webdriver
from Manejar_Excel.login_page import LoginPage
from Manejar_Excel.Excel_funciones import ExcelUtils
from runner_excel import ejecutar_test_con_datos
import os
import time
import gc

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")

    def test(self):
        path = os.path.join(os.path.dirname(__file__), "datos.xlsx")
        sheet = "Hoja 1"
        ejecutar_test_con_datos(self.driver, path, sheet)
        self.assertTrue(True)  # Puedes agregar aserciones reales si hay validaciones visuales

    def tearDown(self):
        self.driver.quit()
        gc.collect()

    if __name__ == "__main__":
        unittest.main()