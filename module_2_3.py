my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = len(my_list) - 1
while a <= b and my_list[a] >= 0:
    if my_list[a] > 0:
        print(my_list[a])
    a = a + 1

