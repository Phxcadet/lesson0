def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5, 3, 7)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [4, 5.7, 'столбец']
values_dict = {'a': 7, 'b': 'привет', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [-7.6, 'пока']
print_params(*values_list_2, 42)
