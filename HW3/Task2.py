'''
You have the number 2 as a variable. Multiply it by 2 in two ways.
Accordingly, you need to divide it in 2 different ways by 2.
'''

x = 2

multiple_1 = x * 2
multiple_2 = x << 1

print(multiple_1, multiple_2)

divide_1 = x / 2
divide_2 = x // 2
divide_3 = x >> 1

print(divide_1, divide_2, divide_3)
