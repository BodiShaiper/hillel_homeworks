'''
You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.
'''

casino_blacklist = {'John Doe', 'Bob Ross', 'Silvester Stallone', 'Sarah Konor'}
poker_blacklist = {'Bob Marley', 'Bob Ross', 'John Doe'}
alcohol_blacklist = {'Joseph Stewart', 'John Doe', 'Mark Smith', 'Bob Ross'}

in_all_blacklists = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(in_all_blacklists)
