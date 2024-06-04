print(' ')
print('Задача 1')
print(' ')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print(' ')
print('Задача 2')
print(' ')

values_list = ['Москва', (7, 12, 32), True]
values_dict = {'a': 12, 'b': 'Питер', 'c': False}

print_params(*values_list)
print_params(**values_dict)

print(' ')
print('Задача 3')
print(' ')

values_list_2 = [False, [1,2]]
print_params(*values_list_2, 42)