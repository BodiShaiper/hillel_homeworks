'''
You have two groups of people. One group consists of omnivores, the other only vegetarians. An omnivore is
a vegetarian but a vegetarian is not an omnivore. Display a list of guests who can eat vegetables and herbs.
'''

omnivores = {'Mark', 'Alice', 'Eva', 'Fred'}
vegetarians = {'Anna', 'Emmanuel', 'Frank', 'Bruce'}

print(f'Those are omnivores: {omnivores}')
print(f'And those are vegetarians: {vegetarians}')
print(f'The following people can eat both vegetables and herbs => {vegetarians.union(omnivores)}')
