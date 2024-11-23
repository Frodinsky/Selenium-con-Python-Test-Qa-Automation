import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Crear las instancias de los navegadores manualmente
#firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

chrome.get("https://demoqa.com/text-box")
chrome.maximize_window()

#primera extracion de un xpath
extraccion_xpath = chrome.find_element(By.XPATH, "//input[@id='userName']")
extraccion_xpath.send_keys("Holas")
chrome.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("pruebas@mail.com")
chrome.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(f"Pruebias {extraccion_xpath}")
chrome.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Pues sin novedades")

chrome.execute_script("window.scrollTo(0,500)")
time.sleep(2)
chrome.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(6)

chrome.close()