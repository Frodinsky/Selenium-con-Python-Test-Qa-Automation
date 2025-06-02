import unittest
from selenium import webdriver
from Manejar_Excel.login_page import LoginPage
from Manejar_Excel.Excel_funciones import ExcelUtils
import os
import time
import gc
import warnings
warnings.simplefilter("ignore", ResourceWarning)  # Forzar mostrar si aún existe


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")

    def test(self):
        path = os.path.join(os.path.dirname(__file__), "datos.xlsx")
        sheet = "Hoja 1"

        # Leer datos desde Excel
        nombre = ExcelUtils.read_data(path, sheet, 2, 1)
        email = ExcelUtils.read_data(path, sheet, 2, 2)
        direccion = ExcelUtils.read_data(path, sheet, 2, 3)
        direccion_permanente = ExcelUtils.read_data(path, sheet, 2, 4)

        # Interactuar con la página usando el POM
        login_page = LoginPage(self.driver)
        login_page.ingresar_usuario(nombre)
        login_page.ingresar_email(email)
        login_page.ingresar_direccion1(direccion)
        login_page.ingresar_direccion2(direccion_permanente)
        login_page.hacer_login()
        #time.sleep(2)

        # Puedes agregar aserciones si hay resultados visibles
        self.assertTrue(True)  # Placeholder


    def tearDown(self):
        self.driver.quit()
        gc.collect()

    if __name__ == "__main__":
        unittest.main()