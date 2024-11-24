import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Crear la instancia del navegador
chrome = webdriver.Chrome()
chrome.get("https://demoqa.com/text-box")
chrome.maximize_window()
time.sleep(1)

# Lista de datos a rellenar
lista = ['Holas', '2@2.com', 'Calle Ficticia 123', 'Ciudad Imaginaria']

# Encuentra el primer campo (userName) y rellénalo
campo = chrome.find_element(By.XPATH, "//input[@id='userName']")
campo.send_keys(lista[0])  # Rellenar con 'Holas'
time.sleep(0.3)

# Usa TAB para mover al siguiente campo
campo.send_keys(Keys.TAB)

# Ahora recorremos el resto de los campos con un for
for i in range(1, len(lista)):
    # Encontramos el siguiente campo con el siguiente TAB
    campo = chrome.switch_to.active_element  # El campo actualmente activo

    # Enviar el siguiente valor de la lista
    campo.send_keys(lista[i])
    time.sleep(0.3)

    # Mover al siguiente campo con TAB
    campo.send_keys(Keys.TAB)

time.sleep(0.4)
chrome.execute_script("window.scrollTo(0,500)")
time.sleep(0.5)
campo.send_keys(Keys.TAB + Keys.ENTER)

# Esperar para ver los resultados antes de cerrar
time.sleep(6)

chrome.close()
