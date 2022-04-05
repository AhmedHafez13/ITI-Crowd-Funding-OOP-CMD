import uuid
import storage_manager
from projects_menu import ProjectsMenu
from utils.input_utils import InputUtils
from utils.output_utils import OutputUtils


class AuthMenu:
    def __init__(self):
        self.menu = {
            "1": "Register",
            "2": "Login"
        }

    def show(self):
        OutputUtils.print_menu(self.menu, "Auth Menu")
        option = InputUtils.get_numeric_input("Choose an option")

        while option not in self.menu.keys():
            print("Choose a valid option")
            option = InputUtils.get_numeric_input("Choose an option")

        if option == "1":
            self.register()
        elif option == "2":
            user = self.login()
            project_menu = ProjectsMenu(user)
            project_menu.show()

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

        return user_data
