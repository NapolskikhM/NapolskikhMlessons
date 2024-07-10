class Animal:

    alive = True
    fed = False

    def __init__(self, name, alive, fed):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(self.name, ' съел ', food.name)
            self.fed = True
        else:
            print(self.name, ' не стал есть ', food.name)
            self.alive = False


class Plant:

    edible = False

    def __init__(self, name, edible):
        self.name = name


class Mammal(Animal):

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)


class Predator(Animal):

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)


class Flower(Plant):

    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):

    edible = True

    def __init__(self, name):
        super().__init__(name, edible=True)


# Проверочный код
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# вывод на консоль

'''Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True'''