first = int(input('Введите целое число: '))
second = int(input('Введите целое число: '))
third = int(input('Введите целое число: '))
if first == second and first == third:
    print (3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)