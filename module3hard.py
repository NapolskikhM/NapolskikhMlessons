data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_ = 0 # общая сумма

def calculate_structure_sum(x):


    global sum_

    if isinstance(x[0], (int, float, str)): # если первый объект общего списка число или строка, он прибавляется к общей сумме
        if isinstance(x[0], (int, float)):
        	sum_ += x[0]
        else:
            sum_ += len(x[0])
        x = x[1:] # удаляем первый объект из общего списка
    elif isinstance(x[0], (tuple, list, set)): # если первый объект - кортеж, список или множество, его элементы добавляются в конец общего списка и первый объект удаляется
        for j in x[0]:
        	x.append(j)
        if len(x) != 1: # проверка, если в общем списке один элемент, чтобы не удалить последний объект с элементами
        	x = x[1:]
    elif isinstance(x[0], dict): # если первый элемент - словарь
        x[0] = list(x[0].keys()) + list(x[0].values())
        for j in x[0]:
            x.append(j)
        if len(x) != 1:
        	x = x[1:]
    if len(x) > 0: #  проверка, есть ли элементы в  общем списке
        calculate_structure_sum(x) # рекурсия по общему списку

    return sum_

result = calculate_structure_sum(data_structure)
print(result)
