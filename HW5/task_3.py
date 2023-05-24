file_path = "./test/data/text.txt"

letter_counts = {}

with open(file_path, "r") as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

for letter, count in sorted(letter_counts.items()):
    print(f"{letter} => {count}")
