set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update - We couild add more items than in an Add
set_countries.update({'ar', 'ec', 'pe'})
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)
#remove shows an error
set_countries.remove('ar')
#discard does not break the program
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)
#delete all items from a set
set_countries.clear()
print(set_countries)
print(len(set_countries))