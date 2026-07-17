import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    PAGE_URL = "https://qa-guru.github.io/one-page-form/text-box.html"

    USER_NAME = (By.ID, "userName")
    USER_EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    OUTPUT = (By.ID, "output")

    def open(self):
        """Открывает страницу TextBox"""
        self.driver.get(self.PAGE_URL)

    def fill_form(self, name, email, current_address, permanent_address):
        """Заполняет форму"""
        self.type_text(self.USER_NAME, name)
        self.type_text(self.USER_EMAIL, email)
        self.type_text(self.CURRENT_ADDRESS, current_address)
        self.type_text(self.PERMANENT_ADDRESS, permanent_address)

    def submit_form(self):
        """Отправляет форму"""
        self.click_element(self.SUBMIT)

    def scroll_to_result(self):
        """Прокручивает до результата"""
        element = self.find_element(self.OUTPUT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_result_text(self):
        """Получает текст результата"""
        return self.get_text(self.OUTPUT)

    def is_result_visible(self):
        """Проверяет видимость результата"""
        self.scroll_to_result()
        time.sleep(2)
        return self.is_visible(self.OUTPUT)

    def wait_for_result(self):
        """Ожидает появления результата"""
        self.scroll_to_result()
        time.sleep(2)
        self.wait_for_visible(self.OUTPUT)
