def remove_numbers(file_name):
    with open(file_name, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            modified_line = ''.join(char for char in line if not char.isdigit())
            file.write(modified_line)