def contains_3_digit():
    for num in range(1, 1001):
        if '3' in str(num):
            yield num


divisible_by_seven_generator = contains_3_digit()

for number in divisible_by_seven_generator:
    print(number)
