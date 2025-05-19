import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()
#chrome.maximize_window()
chrome.get("https://validaciones.rodrigovillanueva.com.mx/Tiempos_Ok.html")

espera = WebDriverWait(chrome, timeout=10)
espera.until(EC.visibility_of_element_located((By.ID, "field1")))

chrome.find_element(By.ID, "field1").send_keys("Rodolfo")
chrome.find_element(By.ID, "field2").send_keys("Lara")
combobox = chrome.find_element(By.ID, "comboBox")
#Se ocupa algo como nombre de la variante porque no se que poner, pregunte a chatgpt y me dio cosas en ingles
algo = Select(combobox)
algo.select_by_index(2)
chrome.find_element(By.ID, "checkbox").click()
chrome.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

time.sleep(3)


chrome.close()
