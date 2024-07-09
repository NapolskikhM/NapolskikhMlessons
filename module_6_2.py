class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def  get_model(self, __model):
        return f'Модель: {self.__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self, __color):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(self))
        print(self.get_horsepower(self))
        print(self.get_color(self))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__(owner, __model, __engine_power, __color)


# проверочный код

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


# вывод на консоль
'''Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Невозможно покрасить в Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok'''