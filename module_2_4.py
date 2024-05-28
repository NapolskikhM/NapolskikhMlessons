numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # убираем единицу, которая не нужна
primes = []
not_primes = []
for i in numbers1:                     # перебираем элементы
    for j in numbers1:                 # перебираем делители
        if i < j:                      # прерываем, если делитель больше делимого
            break
        elif i % j == 0 and i > j:     # если делится нацело и не сам на себя
            is_prime = False
            break
        else:                          # остальные
            is_prime = True
    if is_prime == True:
        primes.append(i)               # вносим в список простых чисел
    else:
        not_primes.append(i)           # вносим в список не простых чисел
print('Primes:', primes)
print('Not_primes:', not_primes)