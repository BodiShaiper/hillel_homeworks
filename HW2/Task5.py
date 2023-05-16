'''
You have a group of people with non-unique names. Generate a list of non-duplicate names (you cannot use set for this
task. If there are 2 johns in the list, you need to take only one of them.
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
'''

group_of_people = frozenset(['John', 'Erica', 'Sam', 'John', 'John', 'John', 'Ben', 'Ben'])
print(group_of_people)

'''
for name in group_of_people:
    if group_of_people.count(name) == 1:
        unique_names_list.append(name)

print(unique_names_list)
'''
