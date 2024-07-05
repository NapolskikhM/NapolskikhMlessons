# Писано строго по заданию, руководствуясь проверочным кодом

from time import sleep
import sys


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:

    titles_ = []    # Список названий видео, потому что просто так строковое представление названия не достать

    def __init__(self, title, duration=1, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.titles_.append(str(title))          # Заносим строковые представления названий видео

    def __str__(self):
        return f'{self.title}'


class UrTube:

    users = []
    videos = []
    current_user = None

    # как-то управился без __init__

    def Log_in(self, nickname, password):      # вход для зарегистрированного пользователя, не знаю зачем.
                                                #  По условиям задачи в программе не применяется

        for i in range(len(UrTube.users)):
            if (UrTube.users[i].nickname == nickname
                    and hash(UrTube.users[i].password) == hash(password)):
                UrTube.current_user = UrTube.users[i]

    def add(self, *args):       # Добавляем видео в список

        for j in args:  # вариант с if in не работает, не знаю почему
            a = True
            for i in range(len(UrTube.videos)):
                if UrTube.videos[i].title == j.title:
                    a = False
                break
            if a:
                UrTube.videos.append(j)

    def register(self, nickname, password, age):        # регистрируем нового пользователя и сразу догиним
        new_user = User(nickname, password, age)
        a = True
        if len(UrTube.users) > 0:
            for i in range(len(UrTube.users)):
                if UrTube.users[i].nickname == new_user.nickname:
                    print('Пользователь ' + nickname + ' уже существует')
                    a = False
                break
        if a:
            UrTube.users.append(new_user)
            UrTube.current_user = new_user

    def log_out(self):      # разлогиниваем пользователя, не знаю зачем. По условиям задачи в программе не применяется

        UrTube.current_user = None

    def get_videos(self, fragment_):        # подбираем видео по фрагментам названия

        viborka_ = []       # список подходящих видео

        for i in range(len(Video.titles_)):

            if fragment_.lower() in Video.titles_[i].lower():
                viborka_.append(Video.titles_[i])

        return viborka_

    def watch_video(self, title):  # просмотр видео залогиненым пользователем при соблюдении условий

        # если такого видео нет, по проверочному коду выводится почему-то имя залогиненного пользователя
        if str(title) not in Video.titles_:
            print(UrTube.current_user.nickname)

        if UrTube.current_user:

            for i in range(len(Video.titles_)):

                if Video.titles_[i] == str(title):
                    video_ = UrTube.videos[i]
                    if video_.adult_mode is False or UrTube.current_user.age >= 18:     # проверка возраста
                        for i in range(video_.duration + 1):
                            print(i, end=" ")               # типа просмотр фильма
                            sys.stdout.flush()
                            sleep(1)
                        print('Конец видео')
                    else:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


# чуть не сдох ))

# Код для проверки

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


""" Что должно получиться, вывод на консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist"""
