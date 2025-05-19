from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Crear instancias de los navegadores con WebDriver Manager automático
firefox = webdriver.Firefox(service=FirefoxService(), options=FirefoxOptions())
chrome = webdriver.Chrome(service=ChromeService(), options=ChromeOptions())

# Usar Firefox
firefox.get("https://www.xataka.com.mx/-habitaciones-como-red-ethernet-asi-puedes-hacerlo")
print(f"Firefox Title: {firefox.title}")

# Usar Chrome
chrome.get("https://geekytheory.com/como-instalar-google-chrome-en-manjaro-antergos-arch-linux/")
print(f"Chrome Title: {chrome.title}")

# Cerrar los navegadores
firefox.quit()
chrome.quit()
