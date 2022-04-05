class OutputUtils:
    @staticmethod
    def print_header(message):
        print("----- ----- ----- ----- ----- -----")
        print(message)
        print("----- ----- ----- ----- ----- -----")

    @staticmethod
    def print_menu(menu_options, header_message):
        OutputUtils.print_header(header_message)
        for key, list_item in menu_options.items():
            print(f"{key}: {list_item['title']}")

    @staticmethod
    def print_projects(projects):
        print("#\tTitle\tTarget\tStart Date\tEnd Date".expandtabs(12))
        counter = 1
        for project in projects:
            row = [
                str(counter),
                project['title'],
                f"{project['target']} EGP",
                project['start_data'],
                project['end_data']
            ]
            print("\t".join(row).expandtabs(12))
            counter += 1
