import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()

chrome.get("https://demoqa.com/text-box")
chrome.maximize_window()
chrome.implicitly_wait(15)

tiempo = 0.0
time.sleep(tiempo)

#primera extracion de un xpath
extraccion_xpath = chrome.find_element(By.XPATH, "//input[@id='userName']")
extraccion_xpath.send_keys("Holas")
time.sleep(tiempo)
chrome.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("pruebas@mail.com")
time.sleep(tiempo)
chrome.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(f"Pruebias {extraccion_xpath}")
time.sleep(tiempo)
chrome.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Pues sin novedades")
time.sleep(tiempo)
chrome.execute_script("window.scrollTo(0,500)")
time.sleep(tiempo)
chrome.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(tiempo)

chrome.close()
