def sum_of_n_numbers(*args: int):
    result = sum(args)
    return result


if __name__ == '__main__':
    sum_of_n_numbers(1, 5, 6, 2)
