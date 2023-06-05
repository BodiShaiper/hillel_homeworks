def custom_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True


numbers = [2, 4, 6, 8, 10]
strings = ["hello", "world", ""]
mixed = [True, False, 1, 0]
print(custom_all(numbers))
print(custom_all(strings))
print(custom_all(mixed))
