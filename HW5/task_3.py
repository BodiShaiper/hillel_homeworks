import collections

file_path = "./test/data/text.txt"
letter_counts = collections.Counter()

with open(file_path, "r") as file:
    for line in file:
        letter_counts.update(filter(str.isalpha, line.lower()))

for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}")
