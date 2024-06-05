my_dict = {'Nastya': 2000, 'Daniel': 2001, 'Nadya': 1976, 'Yulia': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Daniel'))
print('Not existing value:', my_dict.get('Sveta'))
my_dict.update({'Renata': 2005, 'Vlad': 1980})
a = my_dict.pop('Nadya')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {34, 34, 65, True, False, 'Sun', 'Cloud', 1.4, 'Sun', 42, True}
print('Set:', my_set)
my_set.add(8)
my_set.add(3.5)
my_set.discard((1))
print('Modified set:', my_set)



