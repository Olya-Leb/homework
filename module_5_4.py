class House:
    houses_history = [] # атрибут хранит названия созданных объектов

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self): # возвращает кол-во этажей
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.')

    def __eq__(self, other): # равенсво (x == y)
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

    def __iadd__(self, value):  # сложение (x += y)
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f'Нужен аргумент типа "int".')

    def __radd__(self, value): # сложение (x = y + x)
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            print(f'Нужен аргумент типа "int".')

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории.')

    def go_to(self, new_floor):
        print(f'Кол-во этажей в здании "{self.name}": {self.number_of_floors}.\n'
              f'Необходимо подняться на {new_floor}-й этаж.')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Ошибка: {new_floor}-ый этаж, в здании "{self.name}" - отсутствует.\n')
        else:
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Эльбрус', 30)
h2 = House('Частный дом', 2)
h3 = House('ЖК Горский', 9)
h4 = House('ЖК Умный дом', 20)
del h1, h2, h3
print(House.houses_history)
