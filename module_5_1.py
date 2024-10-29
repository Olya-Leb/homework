class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Кол-во этажей в здании "{self.name}": {self.number_of_floors}.\n'
              f'Необходимо подняться на {new_floor}-й этаж.')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Ошибка: {new_floor}-ый этаж, в здании "{self.name}" - отсутствует.\n')
        else:
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Эльбрус', 30)
h1.go_to(10)
h2 = House('Частный дом', 2)
h2.go_to(5)
h3 = House('ЖК Горский', 9)
h3.go_to(0)
h4 = House('ЖК Умный дом', 20)
h4.go_to(-1)