team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.5
team2_time = 2153.3
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time)/tasks_total, 1)

if score_1 >= score_2 and team1_time < team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 <= score_2 and team1_time > team2_time:
    result = 'победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print("В команде %s участников: %s! " % (team1, team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда {} решила задач: {}!".format(team2, score_2))
print("Волшебники данных решили задачи за {} с!".format(team2_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")