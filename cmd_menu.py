from utils.input_utils import InputUtils
from utils.output_utils import OutputUtils


class CMDMenu:
    menu = {}

    def show(self):
        if self.menu:
            OutputUtils.print_menu(self.menu["options"], self.menu["title"])
            option = InputUtils.get_numeric_input("Choose an option")

            while option not in self.menu["options"].keys():
                print("Choose a valid option")
                option = InputUtils.get_numeric_input("Choose an option")

            self.menu["options"][option]["handler"]()
