from login_page_pytests import LoginPage

def test_login_valido(driver):
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    assert "inventory" in driver.current_url

def test_login_sin_usuario_ni_password(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.click_login()
    assert "Username is required" in login_page.obtener_error()

def test_login_sin_usuario(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.ingresar_password("secret_sauce")
    login_page.click_login()
    assert "Username is required" in login_page.obtener_error()

def test_login_sin_password(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.ingresar_usuario("standard_user")
    login_page.click_login()
    assert "Password is required" in login_page.obtener_error()

def test_login_con_credenciales_invalidas(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com")
    login_page.ingresar_usuario("wrong_user")
    login_page.ingresar_password("wrong_pass")
    login_page.click_login()
    assert "Username and password do not match" in login_page.obtener_error()



