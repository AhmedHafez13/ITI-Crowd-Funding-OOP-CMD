import json


class StorageManager:
    @staticmethod
    def load_data_from_file(file_name):
        with open(f"data/{file_name}") as data_file:
            json_data = data_file.read()

        if not json_data:
            json_data = "[]"

        return json.loads(json_data)

    """ ----- ----- ----- Files ----- ----- ----- """

    @staticmethod
    def read_users_file():
        return StorageManager.load_data_from_file("users.json")

    @staticmethod
    def store_user(user_data):
        users_data = StorageManager.read_users_file()
        users_data.append(user_data)

        with open("data/users.json", "w") as users_file:
            json.dump(users_data, users_file)

    @staticmethod
    def get_user(email):
        users_data = StorageManager.read_users_file()
        for user in users_data:
            if user["email"] == email:
                return user

    """ ----- ----- ----- Projects ----- ----- ----- """

    @staticmethod
    def read_projects_file():
        return StorageManager.load_data_from_file("projects.json")

    @staticmethod
    def store_project(project_data):
        projects_data = StorageManager.read_projects_file()
        projects_data.append(project_data)

        with open("data/projects.json", "w") as projects_file:
            json.dump(projects_data, projects_file)

    @staticmethod
    def get_all_projects():
        return StorageManager.read_projects_file()

    @staticmethod
    def update_projects(projects_data):
        with open("data/projects.json", "w") as projects_file:
            json.dump(projects_data, projects_file)
