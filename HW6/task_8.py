def display_box(width: int, height: int, character="*"):
    if width == 1:
        for el in range(height):
            print(character)
    else:
        horizontal_line = character * width
        print(horizontal_line)
        for el in range(height - 2):
            vertical_line = character + ' ' * (width - 2) + character
            print(vertical_line)
        if height > 1:
            print(horizontal_line)


if __name__ == '__main__':
    display_box(30, 8)
