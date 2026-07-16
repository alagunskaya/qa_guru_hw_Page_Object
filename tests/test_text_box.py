import pytest
from data.test_data import (POSITIVE_TEST_DATA, INVALID_EMAILS, SQL_PAYLOADS, XSS_PAYLOADS)


class TestTextBoxForm:

    @pytest.mark.positive
    @pytest.mark.parametrize("test_data", POSITIVE_TEST_DATA)
    def test_positive_valid_data(self, text_box_page, test_data):
        """Позитивный тест с валидными данными"""
        text_box_page.fill_form(test_data["name"], test_data["email"], test_data["current_address"], test_data["permanent_address"])
        text_box_page.submit_form()
        text_box_page.wait_for_result()
        result_text = text_box_page.get_result_text()

        assert test_data["name"] in result_text, "Имя не найдено"
        assert test_data["email"] in result_text, "Email не найден"
        assert test_data["current_address"] in result_text, "Адрес не найден"
        assert test_data["permanent_address"] in result_text, "Постоянный адрес не найден"

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
    def test_negative_email_special_chars(self, text_box_page, invalid_email):
        """Негативный тест с невалидными email"""
        text_box_page.fill_form("Иван Иванов", invalid_email, "Адрес 1", "Адрес 2")
        text_box_page.submit_form()

        assert not text_box_page.is_result_visible(), f"Output появился при невалидном email '{invalid_email}'"

    @pytest.mark.negative
    def test_negative_email_without_at(self, text_box_page):
        """Негативный тест: email без @"""
        text_box_page.fill_form("Иван Иванов", "ivanov.example.com", "Адрес 1", "Адрес 2")
        text_box_page.submit_form()

        assert not text_box_page.is_result_visible(), "Output появился при вводе email без @"

    @pytest.mark.negative
    def test_negative_empty_form(self, text_box_page):
        """Негативный тест: пустая форма"""
        text_box_page.submit_form()

        assert not text_box_page.is_result_visible(), "Output появился при отправке пустой формы"

    @pytest.mark.negative
    def test_negative_email_too_long(self, text_box_page):
        """Негативный тест: слишком длинный email"""
        long_local = "a" * 200
        long_domain = "b" * 50
        long_email = f"{long_local}@{long_domain}.com"

        text_box_page.fill_form("Иван Иванов", long_email, "Address 1", "Address 2")
        text_box_page.submit_form()

        assert not text_box_page.is_result_visible(), f"Output появился при слишком длинном email ({len(long_email)} символов)"

    @pytest.mark.security
    @pytest.mark.parametrize("payload", SQL_PAYLOADS)
    def test_security_sql_injection(self, text_box_page, payload):
        """Тест безопасности: SQL-инъекции"""
        text_box_page.fill_form(payload, "ivanov@example.com", payload, payload)
        text_box_page.submit_form()
        text_box_page.wait_for_result()

        page_source = text_box_page.driver.page_source.lower()
        assert "sql" not in page_source and "error" not in page_source, f"SQL-инъекция вызвала ошибку: {payload[:20]}..."

    @pytest.mark.security
    @pytest.mark.parametrize("payload", XSS_PAYLOADS)
    def test_security_xss_injection(self, text_box_page, payload):
        """Тест безопасности: XSS-инъекции"""
        text_box_page.fill_form(payload, "ivanov@example.com", payload, payload)
        text_box_page.submit_form()
        text_box_page.wait_for_result()

        page_source = text_box_page.driver.page_source.lower()
        assert "alert" not in page_source.lower() or "&lt;" in page_source, f"XSS-инъекция не экранирована: {payload[:20]}..."
