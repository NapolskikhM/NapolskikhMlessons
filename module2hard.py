# Условия задачи довольно запутаны
# Моя программа выдает набор пар чисел в соответствии с условием задачи:
# "написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений"
# Почему-то в проверочных паролях отсутствуют пары одинаковых чисел, например 2,2 для числа 4.
# Чтобы сходилось с ответом, добавил в 14 строке условие: and i != j
# Кроме того, непонятно - имеет ли значение последовательность пар в ответе. У меня с проверочным ключом последовательность не сходится.
import random

a = random.randint(3, 20)
print('случайное число от 3 до 20: ', a)
raw_result = []
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if a % (i + j) == 0 and i != j:
            b = sorted([i, j])
            if b in raw_result:
                break
            else:
                raw_result.append(b)
result = []
t = 0
while t < len(raw_result):
    result.append(raw_result[t][0])
    result.append(raw_result[t][1])
    t = t + 1
print(*result, sep='')
