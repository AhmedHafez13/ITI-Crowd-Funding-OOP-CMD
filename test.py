# import json
#
# with open('users.json') as users_file:
#     text = users_file.read()
#
#
# data = json.loads(text)
#
# print(data[0]["first_name"])


# while input("Enter your password\n") != "10":
#     print("Password is wrong, try again!")

import uuid
print(uuid.uuid4())

# import re
#
# date_validation_regex = r'[0-9]{2}-[0-9]{2}-[0-9]{4}'
#
#
# def is_valid_date(text):
#     return re.fullmatch(date_validation_regex, text)
#
#
# if is_valid_date("22-12-201"):
#     print("matches")
# else:
#     print("Not")
