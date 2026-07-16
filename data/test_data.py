POSITIVE_TEST_DATA = [
    {
        "name": "Иванов Иван",
        "email": "ivanov@example.com",
        "current_address": "460000 Оренбург, ул. Советская",
        "permanent_address": "460000 Оренбург, ул. Советская"
    },
    {
        "name": "А",
        "email": "a@b.com",
        "current_address": "1",
        "permanent_address": "2"
    }
]

INVALID_EMAILS = [
    "ivanov@%example.com",
    "ivanov@\"example.com",
    "ivanov@#example.com"
]

SQL_PAYLOADS = [
    "'; DROP TABLE users; --",
    "1' OR '1'='1",
    "1; SELECT * FROM users"
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x.jpg onerror=alert('XSS')>",
    "javascript:alert('XSS')"
]