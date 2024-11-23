import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()

chrome.get("https://demoqa.com/text-box")
chrome.maximize_window()

#primera extracion de un xpath
extraccion_xpath = chrome.find_element(By.CSS_SELECTOR, "#userName")
extraccion_xpath.send_keys("Holas")
chrome.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("pruebas@mail.com")
chrome.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(f"Dejka de hacer eso xD pichi cacas")
chrome.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("Pues sin novedades")
chrome.execute_script("window.scrollTo(0,500)") #funcion de js para que se desplace la pagina
time.sleep(1)
chrome.find_element(By.CSS_SELECTOR, "#submit").click()

time.sleep(10)

chrome.close()
