import os
import time
from selenium.webdriver.support import expected_conditions as EC

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
    PICTURE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    CITY_INPUT = (By.CSS_SELECTOR, "#city")
    STATE_INPUT = (By.CSS_SELECTOR, "#state")
    CITY_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#formError")
    RESULT_BODY = (By.CSS_SELECTOR, "#resultBody")

    # Календарь
    DAY_OPTION = (By.CSS_SELECTOR,
                  "div.react-datepicker__day--0{padded_day}:not(.react-datepicker__day--outside-month)")
    YEAR_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    MONTH_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    CALENDAR = (By.CSS_SELECTOR, "div[class='react-datepicker__month-container']")

    def open(self):
        self.driver.get(self.PAGE_URL)

    def close_banner(self):
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

    def input_subjects(self, subjects: list | str):
        subjects_list = subjects if isinstance(subjects, list) else [subjects]
        input_subject = self.find_element(self.SUBJECTS_INPUT)

        for subject in subjects_list:
            input_subject.send_keys(subject)

            # Ждем появления варианта в списке
            first_option = (By.XPATH,
                            f"//div[contains(@class, 'subjects-auto-complete__option') and text()='{subject}']")
            self.wait.until(EC.visibility_of_element_located(first_option))

            self.click_element(first_option)

        self.driver.execute_script("arguments[0].blur();", input_subject)

    def select_hobbies(self, hobbies: list | str):
        hobbies_list = hobbies if isinstance(hobbies, list) else [hobbies]

        for hobby in hobbies_list:
            hobby_normalized = hobby.strip().capitalize()

            locator = (By.XPATH, f"//label[contains(text(), '{hobby_normalized}')]")
            self.click_element(locator)

    def upload_picture(self):
        """Загрузить файл"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("Image data")

        self.upload_file(self.PICTURE_INPUT, temp_file_path)

    def select_state(self, state_name: str):
        self.click_element(self.STATE_INPUT)
        self.wait.until(EC.visibility_of_element_located(self.STATE_DROP_DOWN))

        state_option = (By.XPATH, f"//div[@class='state-city-option' and text()='{state_name}']")
        state = self.wait.until(EC.element_to_be_clickable(state_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state)
        self.driver.execute_script("arguments[0].click();", state)

    def select_city(self, city_name: str):
        self.click_element(self.CITY_INPUT)
        self.wait.until(EC.visibility_of_element_located(self.CITY_DROP_DOWN))

        city_option = (By.XPATH, f"//div[@class='state-city-option' and text()='{city_name}']")
        city = self.wait.until(EC.element_to_be_clickable(city_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city)
        self.driver.execute_script("arguments[0].click();", city)

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
        self.wait_for_visible(self.RESULT_BODY)
        return self.get_text(self.RESULT_BODY)

    def get_error_message(self) -> str:
        """Получить текст ошибки"""
        self.wait_for_visible(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    def fill_form(self, data: dict):
        self.close_banner()
        self.input_first_name(data["first_name"])
        self.input_last_name(data["last_name"])
        self.input_email(data["email"])
        self.select_gender(data["gender"])
        self.input_mobile_number(data["mobile"])
        self.select_date_of_birth()
        self.input_subjects(data["subjects"])
        self.select_hobbies(data["hobbies"])
        self.upload_picture()
        self.input_current_address(data["current_address"])
        self.select_state(data["state"])
        self.select_city(data["city"])

    def fill_form_partial(self, data: dict):
        self.close_banner()
        if "first_name" in data:
            self.input_first_name(data["first_name"])

        if "last_name" in data:
            self.input_last_name(data["last_name"])

        if "email" in data:
            self.input_email(data["email"])

        if "gender" in data:
            self.select_gender(data["gender"])

        if "mobile" in data:
            self.input_mobile_number(data["mobile"])

        if "subjects" in data:
            self.input_subjects(data["subjects"])

        if "hobbies" in data:
            self.select_hobbies(data["hobbies"])

        if "current_address" in data:
            self.input_current_address(data["current_address"])

        if "state" in data:
            self.select_state(data["state"])

        if "city" in data:
            self.select_city(data["city"])
