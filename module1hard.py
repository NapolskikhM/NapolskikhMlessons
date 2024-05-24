grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
average_ball = {}
average_ball[students_list[0]] = sum(grades[0]) / len(grades[0])
average_ball[students_list[1]] = sum(grades[1]) / len(grades[1])
average_ball[students_list[2]] = sum(grades[2]) / len(grades[2])
average_ball[students_list[3]] = sum(grades[3]) / len(grades[3])
average_ball[students_list[4]] = sum(grades[4]) / len(grades[4])
# Надо бы цикл, но мы же их еще не изучали )))
print(average_ball)