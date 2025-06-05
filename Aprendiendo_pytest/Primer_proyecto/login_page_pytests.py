from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def ingresar_usuario(self, username):
        campo_usuario = self.wait.until(EC.visibility_of_element_located(self.username_input))
        campo_usuario.clear()
        campo_usuario.send_keys(username)

    def ingresar_password(self, password):
        campo_password = self.wait.until(EC.visibility_of_element_located(self.password_input))
        campo_password.clear()
        campo_password.send_keys(password)

    def click_login(self):
        boton_login = self.wait.until(EC.element_to_be_clickable(self.login_button))
        boton_login.click()

    def obtener_error(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return error_element.text
