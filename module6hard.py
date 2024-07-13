class Figure:
    sides_count = 0

    def __init__(self, __color, *new_sides):
        if self.sides_count != 12:      # проверка для кругов и треугольников
            if self.__is_valid_sides(*new_sides) is True:
                self.__sides = list(new_sides)
            else:
                self.__sides = [1] * self.sides_count # если не соответствует, создаем единичные стороны
        else:           # проверка для кубов
            new_sides_ = list(new_sides)
            if len(new_sides_) == 1 and new_sides_[0] > 0 and type(new_sides_[0]) is int:
                self.__sides = [new_sides_[0]] * 12
            else:
                self.__sides = [1] * 12     # если не соответствует, создаем единичные стороны

        self.__color = __color
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, new_colors):

        if all(0 < x < 256 for x in new_colors):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        new_colors = [r, g, b]
        if self.__is_valid_color(new_colors) is True:
            self.__color = new_colors

    def __is_valid_sides(self, *new_sides):
        new_sides_ = list(new_sides)
        if len(new_sides_) == self.sides_count:
            return all(x > 0 and type(x) is int for x in new_sides_)
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        new_sides_ = list(new_sides)

        if (len(new_sides_) == 1 and self.sides_count == 12  # для кубов
                and new_sides_[0] > 0 and type(new_sides_[0]) is int):
            self.__sides = [new_sides_[0]] * 12
            return self.__sides
        else:                                                 # для кругов и треугольников
            if self.__is_valid_sides(*new_sides) is True:
                self.__sides = new_sides_
                return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *new_sides):
        super().__init__(__color, *new_sides)
        self.__sides = self.get_sides()
        self.__radius = self.__sides[0] / 3.14159265359 / 2

    def get_square(self):                   # площадь круга
        circle_area = 3.14159265359 * (self.__radius ** 2)
        return circle_area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *new_sides):
        super().__init__(__color, *new_sides)
        self.__sides = self.get_sides()

        # высота треугольника по трем сторонам
        self.__height = 2 * ((self.__len__() / 2) * (self.__sides[0] + self.__sides[1])
                             * (self.__sides[1] + self.__sides[2]) * (self.__sides[0] +
                                                                      self.__sides[2])) ** 0.5 / self.__sides[2]

    def get_square(self):                           # площадь треугольника
        triangle_area = self.__height * self.__sides[2] / 2
        return triangle_area


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *new_sides):
        super().__init__(__color, *new_sides)
        self.__sides = self.get_sides()

    def get_volume(self):               # объем куба
        cube_volume = self.get_sides()[0] ** 3
        return cube_volume

# gроверочный код
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

'''[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216'''
