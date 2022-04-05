import uuid
import storage_manager
from cmd_menu import CMDMenu
from projects_menu import ProjectsMenu
from utils.input_utils import InputUtils
from utils.output_utils import OutputUtils


class AuthMenu(CMDMenu):
    def __init__(self):
        self.menu = {
            "title": "Auth Menu",
            "options": {
                "1": {
                    "title": "Register",
                    "handler": self.register
                },
                "2": {
                    "title": "Login",
                    "handler": self.login
                }
            }
        }

    def register(self):
        OutputUtils.print_header("Register new user")

        user_data = {
            "id": f"{uuid.uuid4()}",
            "first_name": InputUtils.get_text_input("Enter your first name"),
            "last_name": InputUtils.get_text_input("Enter your last name"),
            "email": InputUtils.get_email_input("Enter your email"),
            "password": InputUtils.get_mixed_input("Enter password")
        }

        while InputUtils.get_mixed_input("Confirm password") != user_data["password"]:
            print("Password confirmation doesn't match password")

        storage_manager.store_user(user_data)

        OutputUtils.print_header("Successfully registered, you can login now")
        self.show()

    def login(self):
        email = InputUtils.get_email_input("Enter your email")
        user_data = storage_manager.get_user(email)
        while not user_data:
            print("This username doesn't exist")
            email = InputUtils.get_email_input("Enter your email")
            user_data = storage_manager.get_user(email)

        while InputUtils.get_mixed_input("Enter your password") != user_data["password"]:
            print("Password is wrong, try again!")

        project_menu = ProjectsMenu(user_data)
        project_menu.show()
