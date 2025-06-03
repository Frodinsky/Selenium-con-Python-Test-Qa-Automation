from Manejar_Excel.Excel_funciones import ExcelUtils
from Manejar_Excel.login_page import LoginPage


def ejecutar_test_con_datos(driver, path, sheet):
    print(f"Leyendo archivo en: {path}")
    print(f"Usando hoja: {sheet}")

    filas = ExcelUtils.get_row_count(path, sheet)
    print(f"Filas detectadas: {filas}")

    for r in range(2, filas + 1):
        # Leer datos desde Excel
        nombre = ExcelUtils.read_data(path, sheet, r, 1)
        email = ExcelUtils.read_data(path, sheet, r, 2)
        direccion = ExcelUtils.read_data(path, sheet, r, 3)
        direccion_permanente = ExcelUtils.read_data(path, sheet, r, 4)

        print(f"Fila {r}: nombre={nombre}, email={email}, direccion={direccion}, permanente={direccion_permanente}")

        # Si todos los campos están vacíos, terminamos el bucle
        if not any([nombre, email, direccion, direccion_permanente]):
            print(f"Fin de datos detectado en fila {r}. Terminando la ejecución del bucle.")
            break

        # Usar el Page Object para interactuar con la página
        login_page = LoginPage(driver)
        login_page.ingresar_usuario(nombre)
        login_page.ingresar_email(email)
        login_page.ingresar_direccion1(direccion)
        login_page.ingresar_direccion2(direccion_permanente)
        login_page.hacer_login()

        # Verificar si el formulario se envió correctamente
        existe = login_page.existe_por_id("output")

        if existe:
            print("✅ El elemento se insertó correctamente.")
            ExcelUtils.write_data(path, sheet, r, 5, "insertado")
        else:
            print("❌ No se insertó.")
            ExcelUtils.write_data(path, sheet, r, 5, "Error")
