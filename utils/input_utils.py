from utils.validation_utils import ValidationUtils


class InputUtils:
    @staticmethod
    def get_numeric_input(message):
        user_input = input("> " + message + ":\n")
        while not user_input.isdigit():
            print("Your input is invalid")
            user_input = input("> " + message + ":\n")
        return user_input

    @staticmethod
    def get_text_input(message):
        user_input = input("> " + message + ":\n")
        while not user_input:
            print("Your input is invalid")
            user_input = input("> " + message + ":\n")
        return user_input

    @staticmethod
    def get_mixed_input(message):
        user_input = input("> " + message + ":\n")
        while not user_input:
            print("Your input is invalid")
            user_input = input("> " + message + ":\n")
        return user_input

    @staticmethod
    def get_email_input(message):
        user_input = input("> " + message + ":\n")
        while not ValidationUtils.is_valid_email(user_input):
            print("Your input is invalid email")
            user_input = input("> " + message + ":\n")
        return user_input

    @staticmethod
    def get_date_input(message):
        user_input = input("> " + message + ":\n")
        while not ValidationUtils.is_valid_date(user_input):
            print("Your input is invalid date")
            user_input = input("> " + message + ":\n")
        return user_input
