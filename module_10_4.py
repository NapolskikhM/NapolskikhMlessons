from threading import Thread
from time import sleep
from queue import Queue
from random import randint


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):

        sleep(randint(3, 10))


class Cafe(Queue):

    def __init__(self, *tables):
        super().__init__()
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:

            # проверка заполненности столов
            if not [x.guest for x in tables if x.guest is None]:
                # все столы заполнены, ставим в очередь
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    guest.join()
                    break

    def discuss_guests(self):

        # Конец работы программы после ухода последнего посетителя (все столы пустые)
         while  not all([x.guest is None for x in tables]):

            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get(self)
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()
                            table.guest.join()

        print('Все покушали')


# Проверочный код
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
