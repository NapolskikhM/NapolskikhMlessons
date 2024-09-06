from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):

    def test_walk(self):
        walker_1 = Runner('J. Walker')
        a = 1
        while a != 11:
            Runner.walk(walker_1)
            a += 1
        self.assertEqual(walker_1.distance, 50)

    def test_run(self):
        ranner_1 = Runner('U. Bolt')
        a = 0
        while a != 10:
            Runner.run(ranner_1)
            a += 1
        self.assertEqual(ranner_1.distance, 100)

    def test_challenge(self):
        ranner_2 = Runner('U. Bolt Jr')
        walker_2 = Runner('J. Walker Jr')
        a = 1
        while a != 11:
            Runner.run(ranner_2)
            Runner.walk(walker_2)
            a += 1
        self.assertNotEqual(ranner_2.distance, walker_2.distance)


RunnerTest()


