def is_prime(number: 'int'):
    """
        Function takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number, and False if not.
    """
    if 2 <= number <= 1000:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
    else:
        print("Number is not in range 2 - 1000.")
        return False


if __name__ == '__main__':
    is_prime(1000)
