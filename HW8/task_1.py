def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' was called. Result: {result}")
        return result

    return wrapper


@print_function_name
def add_numbers(a, b):
    return a + b


my_result = add_numbers(3, 4)
