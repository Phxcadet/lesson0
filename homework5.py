immutable_var = (12, 4.5, 'hello', True)
print('Immutable tuple: ' + str(immutable_var))
# immutable_var[0] = 1 нельзя менять элементы кортежа, потому что кортеж изначально НЕИЗМЕНЯЕМЫЙ
mutable_list = [24, 5,56, 'bye', False]
mutable_list[0] = 42
mutable_list[1] = -5.56
mutable_list[2] = 'hi'
mutable_list[3] = True
print('Mutable list: ' + str(mutable_list))
