import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://demoqa.com/text-box")
tiempo = 1




time.sleep(tiempo)
chrome.close()
