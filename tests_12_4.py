import traceback
import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walker_1 = Runner('J. Walker', -5)
            if walker_1.speed < 0:
                raise ValueError('скорость не может быть отрицательной')
            else:
                logging.info('"test_walk" выполнен успешно')
                a = 1
                while a != 11:
                    Runner.walk(walker_1)
                    a += 1
                self.assertEqual(walker_1.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_1 = Runner({1, 1})
            a = 0
            while a != 10:
                Runner.run(runner_1)
                a += 1
            self.assertEqual(runner_1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        ranner_2 = Runner('U. Bolt Jr')
        walker_2 = Runner('J. Walker Jr')
        a = 1
        while a != 11:
            Runner.run(ranner_2)
            Runner.walk(walker_2)
            a += 1
        self.assertNotEqual(ranner_2.distance, walker_2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='UTF-8',
                        format='%(asctime)s , %(lineno)d , %(levelname)s , %(message)s')

