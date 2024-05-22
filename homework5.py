immutable_var = 77.5, 'старый город', True, 1980, 'Килауэа'
print('кортеж: ', immutable_var)
# immutable_var [1] = 10
# Изменение элементов кортежа не предусмотрено языком Python: 'tuple' object does not support item assignment
mutable_list = [77.5, 'старый город', True, 1980, 'Килауэа']
mutable_list [0] = 10.1
mutable_list [1] = 'downtown'
print('список: ', mutable_list)
