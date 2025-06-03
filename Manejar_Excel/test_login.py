import unittest
from selenium import webdriver
from Manejar_Excel.login_page import LoginPage
from Manejar_Excel.Excel_funciones import ExcelUtils
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
        filas = ExcelUtils.get_row_count(path, sheet)
        print(f"Leyendo archivo en: {path}")
        print(f"Usando hoja: {sheet}")
        print(f"Filas detectadas: {filas}")


        for r in range(2, filas+1):
            # Leer datos desde Excel
            nombre = ExcelUtils.read_data(path, sheet, r, 1)
            email = ExcelUtils.read_data(path, sheet, r, 2)
            direccion = ExcelUtils.read_data(path, sheet, r, 3)
            direccion_permanente = ExcelUtils.read_data(path, sheet, r, 4)

            print(f"Fila {r}: nombre={nombre}, email={email}, direccion={direccion}, permanente={direccion_permanente}")

            # Si todos los campos están vacíos, romper el bucle
            if not any([nombre, email, direccion, direccion_permanente]):
                print(f"Fin de datos detectado en fila {r}. Terminando la ejecución del bucle.")
                break

            # Interactuar con la página usando el POM
            login_page = LoginPage(self.driver)
            login_page.ingresar_usuario(nombre)
            login_page.ingresar_email(email)
            login_page.ingresar_direccion1(direccion)
            login_page.ingresar_direccion2(direccion_permanente)
            login_page.hacer_login()
            #time.sleep(1)

            existe = login_page.existe_por_id("output")

            if existe:
                print("El elemento se inserto correctamente")
                ExcelUtils.write_data(path,sheet,r,5,"insterado")
            else:
                print("No se inserto")
                ExcelUtils.write_data(path,sheet,r,5,"Error")

        # Puedes agregar aserciones si hay resultados visibles
        self.assertTrue(True)  # Placeholder


    def tearDown(self):
        self.driver.quit()
        gc.collect()

    if __name__ == "__main__":
        unittest.main()