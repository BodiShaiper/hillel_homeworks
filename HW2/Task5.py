'''
You have a group of people with non-unique names. Generate a list of non-duplicate names (you cannot use set for this
task. If there are 2 johns in the list, you need to take only one of them.
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")
'''

group_of_people = ['John', 'Erica', 'Sam', 'John', 'John', 'John', 'Ben', 'Ben']

'''
for name in group_of_people:
    if group_of_people.count(name) == 1:
        unique_names_list.append(name)

print(unique_names_list)
'''

unique_names_list = []
group_of_people.sort()
print(group_of_people)
unique_names_list.append(group_of_people[0])
unique_names_list.append(group_of_people[2])
unique_names_list.append(group_of_people[3])
unique_names_list.append(group_of_people[-1])
print(unique_names_list)
