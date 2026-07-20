import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    PAGE_URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    USER_EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")
    DATE_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")
    SUBJECTS_MENU = (By.CSS_SELECTOR, "div[class='subjects-auto-complete__option']")
    PICTURE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    CITY_INPUT = (By.CSS_SELECTOR, "#city")
    STATE_INPUT = (By.CSS_SELECTOR, "#state")
    CITY_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    MODAL_DIALOG = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#formError")
    MODAL_DIALOG_RESULT = (By.CSS_SELECTOR, "#resultBody")

    # Календарь
    DAY_OPTION = (By.CSS_SELECTOR,
                  "div.react-datepicker__day--0{padded_day}:not(.react-datepicker__day--outside-month)")
    YEAR_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    MONS_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    CALENDAR = (By.CSS_SELECTOR, "div[class='react-datepicker__month-container']")

    # Хобби
    HOBBIES_MUSIC_INPUT = (By.ID, "hobbies-checkbox-3")
    HOBBIES_SPORTS_INPUT = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_INPUT = (By.ID, "hobbies-checkbox-2")
    HOBBY_LABEL_LOCATOR = (By.XPATH, "//label[contains(text(), '{hobby_name}')]")
    HOBBIES_MUSIC_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    HOBBIES_SPORTS_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING_LABEL = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")

    def open(self):
        """Открывает страницу"""
        self.driver.get(self.PAGE_URL)

    def close_banner(self):
        """Закрывает баннер"""
        self.click_element((By.CSS_SELECTOR, "button[aria-label='Close']"))

    def input_first_name(self, first_name: str):
        self.type_text(self.FIRST_NAME, first_name)

    def input_last_name(self, last_name: str):
        self.type_text(self.LAST_NAME, last_name)

    def input_email(self, email: str):
        self.type_text(self.USER_EMAIL, email)

    def select_gender(self, gender: str):
        allowed_genders = ["Male", "Female", "Other"]
        if gender not in allowed_genders:
            raise ValueError(f"Недопустимый гендер: '{gender}'. Допустимо: {allowed_genders}")

        locator = (By.XPATH, f"//label[.//input[@type='radio' and @value='{gender}']]")
        self.click_element(locator)

    def input_mobile_number(self, mobile_number: str):
        self.type_text(self.MOBILE_NUMBER, mobile_number)

    def select_date_of_birth(self):
        """Временно, пока нет элемента - календарь"""
        self.click_element(self.DATE_INPUT)
        self.wait_for_visible(self.CALENDAR)
        month_select = self.find_element((By.CLASS_NAME, "react-datepicker__month-select"))
        month_select.click()
        month_select.find_element(By.XPATH, "//option[@value='11']").click()

        year_select = self.find_element((By.CLASS_NAME, "react-datepicker__year-select"))
        year_select.click()
        year_select.find_element(By.XPATH, "//option[@value='1989']").click()

        day_element = self.find_element(
            (By.CSS_SELECTOR, ".react-datepicker__day--020:not(.react-datepicker__day--outside-month)"))
        day_element.click()

    def input_subjects(self, subject: str):
        """Пока без выбора из списка"""
        self.type_text(self.STATE_INPUT, subject)

    def input_current_address(self, current_address: str):
        self.type_text(self.CURRENT_ADDRESS, current_address)

    def scroll_to_submit(self):
        element = self.find_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_submit_button(self):
        self.scroll_to_submit()
        time.sleep(2)
        self.click_element(self.SUBMIT_BUTTON)

    def get_result_form(self) -> str:
        """Получить форму с результатом"""
        self.wait_for_visible(self.MODAL_DIALOG_RESULT)
        return self.get_text(self.MODAL_DIALOG_RESULT)

    def get_error_message(self) -> str:
        """Получить текст ошибки"""
        self.wait_for_visible(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

