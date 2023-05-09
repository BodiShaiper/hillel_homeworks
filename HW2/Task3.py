'''
You have two groups of people. One group consists of omnivores, the other only vegetarians. An omnivore is
a vegetarian but a vegetarian is not an omnivore. Display a list of guests who can eat vegetables and herbs.
'''


omnivores = {'Bob', 'Anna', 'Alice', 'Frank', 'Eva', 'Bruce', 'Fred', 'Emmanuel'}
vegeterians = {'Anna', 'Emmanuel', 'Frank', 'Bruce'}

print(omnivores.intersection(vegeterians))
