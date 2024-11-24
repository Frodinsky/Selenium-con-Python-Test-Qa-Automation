import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()
chrome.get("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html")
chrome.maximize_window()
tiempo = 0.1

try:
    variable_selector = WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.XPATH, "//select["
                                                                                                   "@id='comboBox1']")))
    #variable_selector = chrome.find_element(By.XPATH, "//select[@id='comboBox1']")

    #Se ocupa vs porque no se como nombrar esta variable, es una referencia a la de arriba
    vs = Select(variable_selector)

    vs.select_by_index(4)
    time.sleep(tiempo)

    vs.select_by_value("3")

except TimeoutException as ex:
    print(ex.msg)
    print("Error en el xptah")

multi_seccion = Select(chrome.find_element(By.ID, "comboBox2"))

multi_seccion.select_by_index(0)
time.sleep(tiempo)

multi_seccion.select_by_index(2)
time.sleep(tiempo)

multi_seccion.select_by_index(4)
time.sleep(tiempo)

time.sleep(tiempo)
chrome.close()
