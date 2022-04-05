import uuid
import storage_manager
from utils.input_utils import InputUtils
from utils.output_utils import OutputUtils


class ProjectsMenu:
    def __init__(self, _user_data):
        self.user_data = _user_data

        self.menu = {
            "1": "Create a new Project",
            "2": "View All Projects",
            "3": "Edit a Project",
            "4": "Delete a Project",
            "5": "Search for a Project"
        }

    def show(self):
        OutputUtils.print_menu(self.menu, "Projects Menu")
        option = InputUtils.get_numeric_input("Choose an option")

        while option not in self.menu.keys():
            print("Choose a valid option")
            option = InputUtils.get_numeric_input("Choose an option")

        if option == "1":
            self.create()
        elif option == "2":
            self.view_all()
        elif option == "3":
            self.edit()
        elif option == "4":
            self.delete()
        elif option == "5":
            self.search()

    def create(self):
        OutputUtils.print_header("Create a new project")

        project_data = {
            "id": f"{uuid.uuid4()}",
            "user_id": self.user_data["id"],
            "title": InputUtils.get_text_input("Enter a title"),
            "details": InputUtils.get_text_input("Enter the details"),
            "target": InputUtils.get_numeric_input("Enter the total target"),
            "start_data": InputUtils.get_date_input("Enter start data"),
            "end_data": InputUtils.get_date_input("Enter end data")
        }

        storage_manager.store_project(project_data)

        OutputUtils.print_header("Successfully created")
        self.show()

    def view_all(self):
        projects = storage_manager.get_all_projects()
        OutputUtils.print_projects(projects)
        self.show()

    def edit(self):
        projects = storage_manager.get_all_projects()

        own_projects = list(filter(
            lambda project: project["user_id"] == self.user_data["id"],
            projects
        ))

        if own_projects:
            OutputUtils.print_projects(own_projects)

            project_order = int(InputUtils.get_numeric_input("Choose a project to edit"))
            target_project = own_projects[project_order-1]

            target_project["title"] = InputUtils.get_text_input(
                f"Enter a new title, current title: {target_project['title']}"
            )
            target_project["details"] = InputUtils.get_text_input(
                f"Enter a new details, current details: {target_project['details']}"
            )
            target_project["target"] = InputUtils.get_numeric_input(
                f"Enter a new target, current target: {target_project['target']}"
            )
            target_project["start_data"] = InputUtils.get_date_input(
                f"Enter a new start data, current start data: {target_project['start_data']}"
            )
            target_project["end_data"] = InputUtils.get_date_input(
                f"Enter a new end data, current end data: {target_project['end_data']}"
            )

            storage_manager.update_projects(projects)

            OutputUtils.print_header("Successfully updated!")
            self.show()
        else:
            OutputUtils.print_header("Can't find any projects")

    def delete(self):
        projects = storage_manager.get_all_projects()

        own_projects = list(filter(
            lambda project: project["user_id"] == self.user_data["id"],
            projects
        ))

        if own_projects:
            OutputUtils.print_projects(own_projects)

            project_order = int(InputUtils.get_numeric_input("Choose a project to delete"))
            target_project = own_projects[project_order - 1]

            projects = list(filter(
                lambda project: project["id"] != target_project["id"],
                projects
            ))

            storage_manager.update_projects(projects)

            OutputUtils.print_header("Successfully deleted!")
            self.show()
        else:
            OutputUtils.print_header("Can't find any projects")

    def search(self):
        pass
