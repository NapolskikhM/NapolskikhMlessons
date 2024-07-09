class Horse:

    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self, x_distance=0, sound='Frrr')
        Eagle.__init__(self, y_distance=0, sound='I train, eat, sleep, and repeat')

    def move(self, dx, dy):
        self.x_distance = self.run(dx)
        self.y_distance = self.fly(dy)
        return self.x_distance, self.y_distance

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

# проверочный код

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


# вывод на консоль
'''(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat'''