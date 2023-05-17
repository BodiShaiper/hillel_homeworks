'''
there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}
'''

my_string = ' name=Amanda=sssss&age=32&&salary=1500&currency=euro '
updated_string = my_string.strip().replace('=sssss', '').split('&')

# Method 1:
'''
new_list = []

for el in updated_string:
    if len(el) > 0:
        new_list.append(el.split('='))
        
converted_string = dict(new_list)
print(converted_string)
'''

# Method 2:
converted_string = dict([element.split('=') for element in updated_string if len(element) > 0])
print(converted_string)
