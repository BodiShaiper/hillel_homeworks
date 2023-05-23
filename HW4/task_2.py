'''
you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it to a list of
variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
'''

camel_case_names = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_names = []

for name in camel_case_names:
    snake_case_name = ""
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            snake_case_name += "_"
        snake_case_name += char.lower()
    snake_case_names.append(snake_case_name)

print(snake_case_names)
