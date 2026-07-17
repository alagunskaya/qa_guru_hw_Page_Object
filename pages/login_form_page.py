from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = "https://qa-guru.github.io/one-page-form/login.html"

    LOGIN_INPUT = (By.ID, "login-input")
    PASSWORD = (By.ID, "password-input")
    SUBMIT_BUTTON = (By.ID, "submit-button")
    ERROR_MESSAGE = (By.ID, "error-message")

    def open(self):
        """Открывает страницу Login"""
        self.driver.get(self.PAGE_URL)

    def login(self, login, password):
        self.type_text(self.LOGIN_INPUT, login)
        self.type_text(self.PASSWORD, password)
        self.click_element(self.SUBMIT_BUTTON)

    def get_error_text(self):
        """Получает текст ошибки"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self):
        """Проверяет видимость ошибки"""
        return self.is_visible(self.ERROR_MESSAGE)
