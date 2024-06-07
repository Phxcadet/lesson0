my_dict = {'Vladimir': 1994, 'Lina': 1999, 'Lilith': 2024, 'Evelina': 2008}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Vladimir'])
print('Not existing value: ', my_dict.get('Kolya'))
my_dict.update({'Petya': 1976, 'Vasya': 1940})
a = my_dict['Lina']
del my_dict['Lina']
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
print()
my_set = { 1, 3, 5.34, 1, 5, 7, 'hi', 'bye', '72apple',  'hi', 5, (1,5,7)}
print('Set: ', my_set)
my_set.add(54)
my_set.add('eboy')
my_set.discard(1)
print('Modified set: ', my_set)
