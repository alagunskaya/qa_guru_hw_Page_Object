class TestRegistrationForm:
    def test_positive_valid_data(self, registration_page):
        registration_page.close_banner()
        registration_page.input_first_name("Ivan")
        registration_page.input_last_name("Ivanov")
        registration_page.input_email("ivanov@mail.com")
        registration_page.select_gender("Male")
        registration_page.input_mobile_number("12345678910")
        registration_page.select_date_of_birth()
        registration_page.input_current_address("Moscow")
        registration_page.click_submit_button()

        result_text = registration_page.get_result_form()
        print(result_text)
        assert "Ivan Ivanov" in result_text, "Имя не найдено"
        assert "ivanov@mail.com" in result_text, "Email не найден"

    def test_negative_empty_form(self, registration_page):
        """Негативный тест: пустая форма"""
        registration_page.close_banner()
        registration_page.click_submit_button()

        assert registration_page.get_error_message() == "Please fill required fields and enter a valid 10-digit mobile number."
