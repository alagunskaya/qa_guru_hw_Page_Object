import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_box_page import TextBoxPage
from pages.login_form_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    """Фикстура для браузера"""
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def text_box_page(driver):
    """Фикстура для страницы TextBox"""
    page = TextBoxPage(driver)
    page.open()
    return page


@pytest.fixture
def login_page(driver):
    """Фикстура для страницы Login"""
    page = LoginPage(driver)
    page.open()
    return page


@pytest.fixture
def registration_page(driver):
    """Фикстура для страницы Registration"""
    page = RegistrationPage(driver)
    page.open()
    return page
