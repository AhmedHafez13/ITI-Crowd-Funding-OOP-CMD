import re
from datetime import datetime


class ValidationUtils:
    email_validation_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    date_validation_regex = r'\d{2}-\d{2}-\d{4}'

    @classmethod
    def is_valid_email(cls, text):
        return re.fullmatch(cls.email_validation_regex, text)

    @classmethod
    def is_valid_date(cls, text):
        if bool(re.fullmatch(cls.date_validation_regex, text)):
            try:
                return bool(datetime.strptime(text, "%d-%m-%Y"))
            except ValueError:
                return False
        else:
            return False
