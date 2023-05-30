def no_vowels(any_string: str):
    result = any_string
    vowels = ('a', 'o', 'u', 'e', 'i')
    for letter in any_string.lower():
        if letter in vowels:
            result = result.lower().replace(letter, '')
    return result


if __name__ == '__main__':
    no_vowels('Lorem Ipsum is simply dummy text of the printing and typesetting industry. ')
