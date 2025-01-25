import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled=bool):
        self.__color = list(color) # список цветов в формате RGB
        self.__sides = list(sides) # список сторон
        self.filled = filled # закрашенный (да/нет)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self): # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides , filled=bool):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, *sides, filled=filled)
        self.__sides = sides
        l = self.__sides[0]
        self.__radius = l / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2 # S площадь круга (можно рассчитать как через длину, так и через радиус)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides, filled=bool):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(color, *sides, filled=filled)
        self.__sides = sides

    def get_square(self):
        a, b, c = self.__sides
        p = 1 / 2 * (a + b + c)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s # S площадь треугольника (можно рассчитать по формуле Герона)

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides, filled=bool):
        if len(sides) != self.sides_count:
            sides = [*sides] * self.sides_count
        super().__init__(color, *sides, filled=filled)
        self.__sides = sides

    def get_volume(self):
        v = self.__sides[0] ** 3
        return v # V объём куба

def main():
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

if __name__ == "__main__":
    main()