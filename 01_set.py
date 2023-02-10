'''Conjuntos o Sets Diferente de Diccionarios'''
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
'''El Conjunto Nunca es Ordenado'''
set_types = {5, 'Hello', False, 13.23}
print(set_types)

set_from_string = set('Freddy Norberto')
print(set_from_string)

set_from_tuples = set(('abc', 'ase', 'assd', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)