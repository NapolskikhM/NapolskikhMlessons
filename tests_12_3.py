import unittest


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


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker_1 = Runner('J. Walker')
        a = 1
        while a != 11:
            Runner.walk(walker_1)
            a += 1
        self.assertEqual(walker_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        ranner_1 = Runner('U. Bolt')
        a = 0
        while a != 10:
            Runner.run(ranner_1)
            a += 1
        self.assertEqual(ranner_1.distance, 100)

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


class Runner_1:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(unittest.TestCase):

    is_frozen = True
    # создаем пеерменную - атрибут класса
    all_results = None

    @classmethod
    def setUpClass(cls):

        # создаем пустой список результатов забегов
        TournamentTest.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain_ = Runner_1('Усэйн', 10)
        self.andry_ = Runner_1('Андрей', 9)
        self.nick_ = Runner_1('Ник', 3)

    @classmethod
    def tearDownClass(cls):

        # вывод результатов забегов
        for i in TournamentTest.all_results:
            print(i)

    def test_1(self):
        # создаем забег
        tournament_1 = Tournament(90, self.usain_, self.nick_)
        # создаем словарь по результатам забега
        results_1 = Tournament.start(tournament_1)
        # в словаре меняем значения - объекты "бегун" на имена бегунов
        for i in results_1:
            results_1[i] = results_1[i].name
        # добавляем результаты забега в список результатов забегов
        TournamentTest.all_results.append(results_1)
        # сравниваем последний объект из all_results по наибольшему ключу и предполагаемое имя последнего бегуна
        self.assertTrue(TournamentTest.all_results[-1].get(max(results_1.keys())) == 'Ник')


    def test_2(self):
        tournament_2 = Tournament(90, self.andry_, self.nick_)
        results_2 = Tournament.start(tournament_2)
        for i in results_2:
            results_2[i] = results_2[i].name
        TournamentTest.all_results.append(results_2)
        max_place = max(results_2.keys())
        self.assertTrue(results_2.get(max_place) == 'Ник')

    def test_3(self):
        tournament_3 = Tournament(90, self.usain_, self.andry_, self.nick_)
        results_3 = Tournament.start(tournament_3)
        for i in results_3:
            results_3[i] = results_3[i].name
        TournamentTest.all_results.append(results_3)
        max_place = max(results_3.keys())
        self.assertTrue(results_3.get(max_place) == 'Ник')

    # по доп. заданию
    # Если в цикле медленный бегун идет раньше быстрого и оба они достигают финиша в пределах одного цикла,
    # слабый бегун получает более высокое место.
    # на любой дистанции быстрее на финиш приходит бегун с наибольшей скоростью, поэтому на всех дистанциях первым
    # будет Усэйн, если участвует, или Андрей

    def first_speed_first_place(self):
        a = True
        for i in TournamentTest.all_results:
            # проверяем, бежал ли Усэйн и первое ли у него место
            if self.usain_.name in list(i.values()) and i[1] != self.usain_.name:
                a = False
                break
            # проверяем, бежал ли Андрей без Усэйна и первое ли у него место
            elif (self.usain_.name not in list(i.values()) and self.andry_.name in list(i.values())
                  and i[1] != self.andry_.name):
                a = False
                break
        return a

    def test_4(self):

        self.assertTrue(self.first_speed_first_place())
