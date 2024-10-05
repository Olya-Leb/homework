def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5, 'ola', False)
#print_params(5, 'ola', False, 6, 'kola', True)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [[6], 2.2, False]
values_dict = {'a' : 'smart', 'b' : 1, 'c' : False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['x', 0.2]
print_params(*values_list_2, 42)