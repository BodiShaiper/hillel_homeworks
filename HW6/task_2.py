def square(side: 'int'):
    """
        Function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
        the perimeter of the square, the area of the square, and the diagonal of the square
    """
    result = ((side * 4), (side ** 2), (side * 2 ** 0.5))
    return result


if __name__ == '__main__':
    square(6)
