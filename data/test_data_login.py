LOGIN_TEST_DATA = {
    "positive": [
        {"login": "abc", "password": "123456"}
    ],
    "negative_login": [
        {"login": "a", "password": "123456"},
        {"login": "ab", "password": "123456"},
        {"login": "", "password": "123456"},
    ],
    "negative_password": [
        {"login": "abc", "password": "1"},
        {"login": "abc", "password": "12345"},
        {"login": "abc", "password": ""}
    ],
    "safeness": [
        {"login": "<script>alert('XSS')</script>", "password": "<script>alert('XSS')</script>"},
        {"login": "1' OR '1'='1", "password": "1' OR '1'='1"},
    ],
}