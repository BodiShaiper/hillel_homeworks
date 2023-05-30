import os

with open('./test/data/tuples.txt') as file:
    data = file.readlines()

for item in data:
    new_data = item.replace('\n', '').split(' ')
    if new_data[2] == '1':
        print(f'{int(new_data[0])} + {int(new_data[1])} = {int(new_data[0]) + int(new_data[1])}')
    elif new_data[2] == '2':
        print(f'{int(new_data[0])} - {int(new_data[1])} = {int(new_data[0]) - int(new_data[1])}')
    else:
        print(f'{int(new_data[0])} * {int(new_data[1])} = {int(new_data[0]) * int(new_data[1])}')
