class Vehicle: # транспортное средство
    __COLOR_VARIANTS = ['RED', 'BLUE', 'YELLOW', 'WHITE', 'BLACK', 'GREEN']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color).upper()

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\n'
              f'Цвет: {self.__color}\nВладелец: {self.owner}\n')

    def set_color(self, new_color):
        if isinstance(new_color, str):
            if new_color.upper() in self.__COLOR_VARIANTS:
                self.__color = new_color.upper()
            else:
                print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров

vehicle1 = Vehicle('Petrov', 'Focus', 150, 'white')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()