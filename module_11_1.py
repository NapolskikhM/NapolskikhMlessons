import requests
import pandas
import numpy

# requests
print()
print('Применение  requests:\n')

file_ = 'txt.txt'

url = f'https://raw.githubusercontent.com/NapolskikhM/NapolskikhMlessons/main/{file_}'

My_file = requests.get(url)
# проверяем наличие файла в папке на GitHub:
if My_file.status_code == 200:
    print(f'Файл {file_} имеется')
    print()
    # скачиваем файл
    with open(file_, 'wb') as file:
        file.write(My_file.content)
    # выводим содержимое файла на консоль:
    print('Содержимое файла:\n')
    with open((file_)) as file:
        print(My_file.content)
    print()
else:
    print(f'Файла {file_} нет\n')

# pandas
print('pandas:\n')

# скачиваем файл csv c GitHub:

url = 'https://raw.githubusercontent.com/NapolskikhM/NapolskikhMlessons/main/exelfile_4.csv'

file_ = 'exelfile_4.csv'

My_file = requests.get(url)

if My_file.status_code == 200:
    with open(file_, 'wb') as file1:
        file1.write(My_file.content)

    # считываем содержимое файла:
    file_csv = pandas.read_csv(file_)

    # создаем объект DataFrame
    df = pandas.DataFrame(file_csv)
    print(f'Объект  DataFrame из файла {file_}:\n')
    print(df, '\n')

    # возводим элементы объекта df в квадрат:
    df = df.transform(lambda x: x ** 2)
    print('Элементы объекта df возведены в квадрат:\n')
    print(df)
else:
    print('Файл не обнаружен!')

# numpy
print()
print('numpy:\n')

# создаем двумерный массив из файла exelfile_4.csv

file_csv = 'exelfile_4.csv'
array_ = numpy.genfromtxt(file_csv, delimiter=',', dtype=int)
print(array_, '\n')

# суммируем строки массива
sum_ = numpy.sum(array_,axis=1).tolist()
print('Суммы строк масссива: ', sum_, '\n')

# вычисляем среднее по массиву
av_ = numpy.mean(array_)
print('Среднее по массиву: ', av_)







