import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

t = 5

with webdriver.Chrome() as driver:
    #Alerta sencilla
    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#alertButton").click()
    alerta = driver.switch_to.alert
    alerta.accept()

    #Alerta que tarda un tiempo indefinido
    driver.find_element(By.CSS_SELECTOR, "#timerAlertButton").click()
    espera = WebDriverWait(driver, 10)
    alerta_tardia = espera.until(EC.alert_is_present())
    alerta_tardia.accept()

    # Alerta que puede ser rechazada
    driver.find_element(By.CSS_SELECTOR, "#confirmButton").click()
    alerta2 = driver.switch_to.alert
    alerta2.accept()

    # Alerta que pide llenar un campo
    driver.find_element(By.CSS_SELECTOR, "#promtButton").click()
    alerta_prompt = driver.switch_to.alert
    alerta_prompt.send_keys("Hola")
    alerta_prompt.accept()

    time.sleep(t)