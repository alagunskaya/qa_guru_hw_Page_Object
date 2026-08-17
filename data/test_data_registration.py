from dataclasses import dataclass
from typing import List


@dataclass
class RegistrationData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    day: int
    month: int
    year: int
    subjects: List[str]
    hobbies: List[str]
    current_address: str
    state: str
    city: str


REGISTRATION_TEST_DATA = [
    RegistrationData(
        first_name="Мария",
        last_name="Иванова",
        email="maria.ivanova@test.com",
        gender="Female",
        mobile="0987654321",
        day=1,
        month=7,
        year=2008,
        subjects=["Chemistry", "Biology"],
        hobbies=["Music"],
        current_address="г. Санкт-Петербург",
        state="Uttar Pradesh",
        city="Agra"
    )
]
