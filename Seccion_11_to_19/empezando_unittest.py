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
        self.driver.get("https://validaciones.rodrigovillanueva.com.mx/Campos_Uno_OK.html")
        time.sleep(t)  # Para fines visuales solamente

    def tearDown(self):  # ✅ Se ejecuta al final del test
        self.driver.quit()  # Mejor que .close() porque cierra toda la sesión

# ✅ Esto debe ir fuera de la clase
if __name__ == '__main__':
    unittest.main()
