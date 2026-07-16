import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_box_page import TextBoxPage

BASE_URL = "https://qa-guru.github.io/one-page-form/text-box.html"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def text_box_page(driver):
    """Фикстура для страницы TextBox"""
    return TextBoxPage(driver)
