import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear las instancias de los navegadores manualmente
chrome = webdriver.Chrome()
chrome.get("https://demoqa.com/checkbox")
chrome.maximize_window()
chrome.implicitly_wait(10)
tiempo = 1

boton_1 = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, """
                                                                        //*[@id="tree-node"]/div/button[1]""")))
boton_1.click()

boton_2 = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, """
                                                            //*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[1]""")))
boton_2.click()

boton_3 = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, """
                                                            //*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[1]""")))
boton_3.click()
chrome.execute_script("window.scrollTo(0,250)")

time.sleep(tiempo)
chrome.close()
