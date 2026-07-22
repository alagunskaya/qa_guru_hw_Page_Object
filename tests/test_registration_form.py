import os

import pytest


class TestRegistrationForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("data", [
        {
            "first_name": "Иван",
            "last_name": "Петров",
            "email": "ivan.petrov@test.com",
            "gender": "Male",
            "mobile": "1234567890",
            "subjects": ["Maths", "Physics"],
            "hobbies": ["Sports", "Reading"],
            "current_address": "г. Москва, ул. Ленина, д. 1",
            "state": "NCR",
            "city": "Delhi"
        },
        {
            "first_name": "Мария",
            "last_name": "Иванова",
            "email": "maria.ivanova@test.com",
            "gender": "Female",
            "mobile": "0987654321",
            "subjects": ["Chemistry", "Biology"],
            "hobbies": ["Music"],
            "current_address": "г. Санкт-Петербург, ул. Невский, д. 10",
            "state": "Uttar Pradesh",
            "city": "Agra"
        }
    ])
    def test_fill_form_positive(self, registration_page, data):
        registration_page.fill_form(data)
        registration_page.click_submit_button()

        result = registration_page.get_result_form()
        assert data["first_name"] in result
        assert data["last_name"] in result
        assert data["email"] in result
        assert data["mobile"] in result
        assert data["current_address"] in result
        assert data["state"] in result
        assert data["city"] in result

        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")

    @pytest.mark.negative
    def test_negative_empty_form(self, registration_page):
        registration_page.close_banner()
        registration_page.click_submit_button()

        assert registration_page.get_error_message() == "Please fill required fields and enter a valid 10-digit mobile number."

    @pytest.mark.parametrize("test_data", [
        {
            "last_name": "Петров",
            "email": "ivan@test.com",
            "gender": "Male",
            "mobile": "1234567890",
        },
        {
            "first_name": "Иван",
            "email": "ivan@test.com",
            "gender": "Male",
            "mobile": "1234567890",
        },
        {
            "first_name": "Иван",
            "last_name": "Петров",
            "email": "ivan@test.com",
            "mobile": "1234567890",
        },
        {
            "first_name": "Иван",
            "last_name": "Петров",
            "email": "ivan@test.com",
            "gender": "Male",
        }
    ], ids=["missing_first_name", "missing_last_name", "missing_gender", "missing_mobile"])
    def test_required_fields(self, registration_page, test_data):
        registration_page.fill_form_partial(test_data)
        registration_page.scroll_to_submit()
        registration_page.click_submit_button()

        error = registration_page.get_error_message()
        assert "Please fill required fields and enter a valid 10-digit mobile number." in error
