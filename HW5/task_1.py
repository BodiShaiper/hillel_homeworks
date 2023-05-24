import random
import os

tuples_list = []
operations = [1, 2, 3]

for item in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.choice(operations)
    tuples_list.append((left_operand, right_operand, operation))

print(tuples_list)

directory_path = "./test/data"
os.makedirs(directory_path)

file_path = os.path.join(directory_path, "tuples.txt")
with open(file_path, "w") as file:
    for my_tuple in tuples_list:
        line = " ".join(str(element) for element in my_tuple)
        file.write(line + "\n")

print("All 100 tuples were successfully saved in", file_path)
