'''
you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop. The element with an
odd index is put into a new list of tuples where the first element is the index and the second is the value. [(index,
value)]. accordingly, elements with an even index are placed in another list of tuples with the same format as in the
case with odd indices.
'''

list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]

odd_list_of_tuples = [(i, elem) for i, elem in enumerate(list_of_elements) if i % 2 != 0]
even_list_of_tuples = [(i, elem) for i, elem in enumerate(list_of_elements) if i % 2 == 0]

"""
odd_list_of_tuples = []
even_list_of_tuples = []
index = 0

for number in list_of_elements:
    if index % 2 != 0:
        odd_list_of_tuples.append((index, number))
    else:
        even_list_of_tuples.append((index, number))
    index += 1
"""

print(odd_list_of_tuples)
print(even_list_of_tuples)
