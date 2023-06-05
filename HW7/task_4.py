def custom_max(iterable, amount=1):
    sorted_values = sorted(iterable, reverse=True)
    return sorted_values[:amount]


def custom_min(iterable, amount=1):
    sorted_values = sorted(iterable)
    return sorted_values[:amount]


numbers = [7, 2, 9, 4, 1, 6, 8, 3, 5]
max_value = custom_max(numbers)
print(max_value)
min_value = custom_min(numbers)
print(min_value)
top_3_max = custom_max(numbers, amount=3)
print(top_3_max)
top_2_min = custom_min(numbers, amount=2)
print(top_2_min)
