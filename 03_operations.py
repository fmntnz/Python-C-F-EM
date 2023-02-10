set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Operator Union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Operator Intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#First Set without common elements with second set
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#Union without common elements
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)