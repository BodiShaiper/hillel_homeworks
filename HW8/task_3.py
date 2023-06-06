def divisible_by_seven():
    for num in range(1, 1001):
        if num % 7 == 0:
            yield num


divisible_by_seven_generator = divisible_by_seven()

for number in divisible_by_seven_generator:
    print(number)
