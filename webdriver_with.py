from selenium import webdriver

with webdriver.Firefox() as firefox:
    firefox.get("https://www.xataka.com.mx/home/poca-gente-sabe-que-usando-enchufes-electricos-puede-llevar-internet-a-habitaciones-como-red-ethernet-asi-puedes-hacerlo")
    print(f"Firefox \n{firefox.title}")
with webdriver.Chrome() as chrome:
    chrome.get("https://geekytheory.com/como-instalar-google-chrome-en-manjaro-antergos-arch-linux/")
    print(f"Chrome \n{chrome.title}")

