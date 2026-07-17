import pytest
from data.test_data_login import (LOGIN_TEST_DATA)


class TestLoginForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("test_data", LOGIN_TEST_DATA["positive"])
    def test_login_form_valid_credentials(self, login_page, test_data):
        """Позитивный тест: валидные данные"""
        login_page.login(test_data["login"], test_data["password"])

        assert not login_page.is_error_visible(), "Ошибка не должна появиться"

    @pytest.mark.negative
    def test_login_form_empty_fields(self, login_page):
        """Негативный тест: пустые поля"""
        login_page.login("", "")

        assert login_page.is_error_visible()
        assert login_page.get_error_text() == "Login and password are required (minimum 3 and 6 characters)"

    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", LOGIN_TEST_DATA["negative_login"])
    def test_login_form_invalid_login(self, login_page, test_data):
        """Негативный тест: невалидный логин"""
        login_page.login(test_data["login"], test_data["password"])

        assert login_page.is_error_visible(), "Ошибка должна появиться"
        assert login_page.get_error_text() == "Login is required minimum 3 characters" or "Login is required (minimum 3 characters)"

    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", LOGIN_TEST_DATA["negative_password"])
    def test_login_form_invalid_password(self, login_page, test_data):
        """Негативный тест: невалидный пароль"""
        login_page.login(test_data["login"], test_data["password"])

        assert login_page.is_error_visible(), "Ошибка должна появиться"
        assert login_page.get_error_text() == "Password must be at least 6 characters" or "Password is required (minimum 6 characters)"

    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", LOGIN_TEST_DATA["safeness"])
    def test_login_form_invalid_password(self, login_page, test_data):
        """Негативный тест: невалидный пароль"""
        login_page.login(test_data["login"], test_data["password"])

        assert login_page.is_error_visible(), "Ошибка должна появиться"
        assert login_page.get_error_text() == "Wrong login or password"
