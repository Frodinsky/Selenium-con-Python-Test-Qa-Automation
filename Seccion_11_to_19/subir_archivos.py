import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()
chrome.get("https://demoqa.com/upload-download")
chrome.maximize_window()
tiempo = 3

try:
    subir_imagen = WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.XPATH, "//input["
                                                                                              "@id='uploadFile']")))
    subir_imagen.send_keys("/home/frodinsky/Imágenes/forge_shortcuts_es.png")
    time.sleep(tiempo)

except TimeoutException as ex:
    print(ex.msg)
    print("Error en el xptah")


time.sleep(tiempo)
chrome.close()
