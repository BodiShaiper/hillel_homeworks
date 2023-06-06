def generate_even_squares():
    for num in range(0, 1000000001, 2):
        while num < 1000000001:
            yield num ** 2
            print(num ** 2)


my_custom_gen = generate_even_squares()
if __name__ == '__main__':
    print(my_custom_gen)
