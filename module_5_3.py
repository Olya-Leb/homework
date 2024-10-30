class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self): # возвращает кол-во этажей
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.')

    def __eq__(self, other): # равенство (x == y)
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')

    def  __lt__(self, other): # сравнение (x < y)
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')


    def __le__(self, other): # сравнение (x <= y)
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')

    def __gt__(self, other): # сравнение (x > y)
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')

    def __ge__(self, other): # сравнение (x >= y)
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')

    def __ne__(self, other): # сравнение (x != y)
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False
        else:
            print(f'Нужен аргумент класса "House".')

    def __add__(self, value): # сложение (x = x + y)
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print(f'Нужен аргумент типа "int".')

    def __iadd__(self, value):  #сложение (x += y)
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Нужен аргумент типа "int".')

    def __radd__(self, value): #сложение (x = y + x)
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            print(f'Нужен аргумент типа "int".')

    def go_to(self, new_floor):
        print(f'Кол-во этажей в здании "{self.name}": {self.number_of_floors}.\n'
              f'Необходимо подняться на {new_floor}-й этаж.')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Ошибка: {new_floor}-ый этаж, в здании "{self.name}" - отсутствует.\n')
        else:
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Эльбрус', 30)
# h1.go_to(10)
# print(len(h1))
# print(str(h1))
h2 = House('Частный дом', 2)
# h2.go_to(5)
# print(len(h2))
# print(str(h2))
h3 = House('ЖК Горский', 9)
# h3.go_to(0)
# print(len(h3))
# print(str(h3))
h4 = House('ЖК Умный дом', 20)
# h4.go_to(-1)
# print(len(h4))
# print(str(h4))

print(h1)
print(h2)
print(h1 == h2) # __eq__
h2 = h2 + 28 # __add__
print(h1)
print(h1 == h2)
h1 += 5 # __iadd__
print(h1)
h2 = 5 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
