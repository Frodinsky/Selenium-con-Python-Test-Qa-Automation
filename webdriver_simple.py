from selenium import webdriver

# Crear las instancias de los navegadores manualmente
firefox = webdriver.Firefox()
chrome = webdriver.Chrome()

# Usar Firefox
firefox.get("https://www.xataka.com.mx/home/poca-gente-sabe-que-usando-enchufes-electricos-puede-llevar-internet-a"
            "-habitaciones-como-red-ethernet-asi-puedes-hacerlo")
print(f"Firefox Title: {firefox.title}")

# Usar Chrome
chrome.get('https://geekytheory.com/como-instalar-google-chrome-en-manjaro-antergos-arch-linux/')
print(f"Chrome Title: {chrome.title}")

# Cerrar los navegadores manualmente
firefox.quit()
chrome.quit()
