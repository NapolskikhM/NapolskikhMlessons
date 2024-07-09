class Animal:

    name = None
    alive = True
    fed = False

    def __init__(self, name, alive, fed):
        self.name = name
        self.alive = alive
        self.fed = fed


class Plant:

    name = None
    edible = False

    def __init__(self, name, edible):
        self.name = name
        self.edible = edible


class Mammal(Animal):

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            print(self.name, ' съел ', food.name)
            self.fed = True
        else:
            print(self.name, ' не стал есть ', food.name)
            self.alive = False


class Predator(Animal):

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            print(self.name, ' съел ', food.name)
            self.fed = True
        else:
            print(self.name, ' не стал есть ', food.name)
            self.alive = False


class Flower(Plant):

    def __init__(self, name, edible=False):
        super().__init__(name, edible)
        self.name = name
        self.edible = edible


class Fruit(Plant):

    def __init__(self, name, edible=True):
        super().__init__(name, edible)
        self.name = name
        self.edible = edible


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