import os
import pytest
from data.test_data_registration import (
    REGISTRATION_TEST_DATA,
    PARTIAL_TEST_DATA,
    RegistrationData,
    PartialRegistrationData
)


class TestRegistrationForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("data", REGISTRATION_TEST_DATA, ids=["maria_ivanova", "ivan_ivanov"])
    def test_fill_form_positive(self, registration_page, data: RegistrationData):
        registration_page.fill_form(data)
        registration_page.click_submit_button()

        result = registration_page.get_result_form()
        assert data.first_name in result
        assert data.last_name in result
        assert data.email in result
        assert data.mobile in result
        assert data.current_address in result
        assert data.state in result
        assert data.city in result

        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")

    @pytest.mark.negative
    def test_negative_empty_form(self, registration_page):
        registration_page.close_banner()
        registration_page.click_submit_button()

        assert registration_page.get_error_message() == "Please fill required fields and enter a valid 10-digit mobile number."

    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", PARTIAL_TEST_DATA,
                             ids=["missing_first_name", "missing_last_name", "missing_gender", "missing_mobile"])
    def test_required_fields(self, registration_page, test_data: PartialRegistrationData):
        registration_page.fill_form_partial(test_data)
        registration_page.scroll_to_submit()
        registration_page.click_submit_button()

        error = registration_page.get_error_message()
        assert "Please fill required fields and enter a valid 10-digit mobile number." in error
