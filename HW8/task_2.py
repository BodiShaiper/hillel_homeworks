def even_squares():
    num = 0
    while num <= 1000000000:
        yield num ** 2
        num += 2


even_squares_generator = even_squares()

for square in even_squares_generator:
    print(square)
