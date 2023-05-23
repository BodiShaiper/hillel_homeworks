'''
You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba. Show it in code.
Keep in mind that people with the same name can be in both companies!
'''

eleks = ['Sam', 'Eva', 'Erika', 'David', 'Simon']
toshiba = ['David', 'Alex', 'Bob', 'Eva', 'Felix']
print(eleks)
print(toshiba)

toshiba.extend(eleks.copy())
eleks.clear()
print(eleks)
print(toshiba)
