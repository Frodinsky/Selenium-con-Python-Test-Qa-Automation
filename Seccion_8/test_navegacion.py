import time
from selenium import webdriver

chrome = webdriver.Chrome()

tiempo = 2

chrome.get("https://demoqa.com/text-box")
chrome.maximize_window()
time.sleep(tiempo)
chrome.get("https://www.youtube.com/")
time.sleep(tiempo)
chrome.get("https://pypi.org/project/webdriver-manager/")
time.sleep(tiempo)

#Para moverse en el historial hacia atras
chrome.execute_script("window.history.go(-1)")
time.sleep(tiempo)

chrome.execute_script("window.history.go(-1)")
time.sleep(tiempo)

#Para moverse sobre el historial hacia adelante
chrome.execute_script("window.history.go(2)")
time.sleep(tiempo)


chrome.close()
