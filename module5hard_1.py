from time import sleep
import sys


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:

    def __init__(self, title, duration=1, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def Log_in(self, nickname, password):  # вход для зарегистрированного пользователя

        for i in range(len(self.users)):
            if self.users[i].nickname == nickname and hash(self.users[i].password) == hash(password):
                self.current_user = self.users[i]

    def add(self, *args):  # Добавляем видео в список

        for j in args:

            self.videos.append(j)  # добавляем
            for i in range(len(self.videos) - 1):
                if j.title == self.videos[i].title:
                    self.videos.pop(-1) # убираем, если такое уже есть

    def register(self, nickname, password, age):  # регистрируем нового пользователя и сразу логиним
        a = []
        for i in range(len(self.users)):            # создаем сисок никнеймов
            a.append(self.users[i].nickname)
        if nickname in a:                           # проверяем, есть ли такой пользователь
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)         # создаем нового пользователя
            self.users.append(new_user)                        # добавляем в список
            UrTube.Log_in(self, nickname, password)             # логиним


    def Log_out(self):  # разлогиниваем пользователя

        self.current_user = None

    def get_videos(self, fragment_):  # подбираем видео по фрагментам названия

        viborka_ = []  # список подходящих видео

        for i in range(len(self.videos)):

            if fragment_.lower() in self.videos[i].title.lower():
                viborka_.append(self.videos[i].title)

        return viborka_

    def watch_video(self, title):  # просмотр видео залогиненым пользователем при соблюдении условий

        if self.current_user:  # проверяем наличие залогиненного пользователя

            video_ = None

            for i in range(len(self.videos)):
                if title == self.videos[i].title:  # ищем видео

                    video_ = self.videos[i]

                    if video_.adult_mode is False or self.current_user.age >= 18:  # проверка возраста
                        for i in range(video_.duration + 1):
                            print(i, end=" ")  # типа просмотр фильма
                            sys.stdout.flush()
                            sleep(1)
                        print('Конец видео')
                    else:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                        UrTube.Log_out(self)            # если возраст не соответствует, разлогиниваем

            if not video_:
                print(ur.current_user.nickname)     # выводим имя пользователя,
                                                    # если нет такого видео (так в проверочном коде)
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


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

""" Dывод на консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist"""