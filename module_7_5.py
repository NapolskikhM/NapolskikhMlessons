import os, time

tree_ = os.walk(r'C:\Users\User\PycharmProjects\+3 Модуль')

for i in tree_:
    print(i)
    for j in i[2]:
        filename_ = j
        filepath_ = os.path.join(i[0], j)
        formatted_time_ = time.ctime(os.path.getmtime(filepath_))
        filesize_ = os.path.getsize(filepath_)
        parent_dir_ = os.path.dirname(filepath_)
        print(f'Обнаружен файл: {filename_}, Путь: {filepath_}, Размер: {filesize_} байт, Время изменения: '
              f'{formatted_time_}, Родительская директория: {parent_dir_}')
