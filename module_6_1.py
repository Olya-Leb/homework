# Домашнее задание по теме "Зачем нужно наследование".
# Задача "Съедобное, несъедобное":
# Пункты задачи:
# 1. Создайте классы Animal и Plant с соответствующими атрибутами и методами
# 2. Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
#    (При необходимости переопределите значения атрибутов).
# 4. Создайте объекты этих классов.

class Animal:
    alive = True # живой (да/нет)
    fed = False # накормленный (да/нет)
    def __init__(self, name):
        self.name = name # имя животного

class Mammal(Animal):
    def eat(self, food): # food - параметр, принимающий объекты классов растений.
        if food.edible:
            print(f'"{self.name}" съел "{food.name}".')
            self.fed = True
        else:
            print(f'"{self.name}" попытался съесть "{food.name}".')
            self.alive = False

class Predator(Animal):
    def eat(self, food): # food - параметр, принимающий объекты классов растений.
        if food.edible:
            print(f'"{self.name}" съел "{food.name}".')
            self.fed = True
        else:
            print(f'"{self.name}" попытался съесть "{food.name}".')
            self.alive = False

class Plant:
    edible = False # съедобность (да/нет)
    def __init__(self, name):
        self.name = name # имя растения

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

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
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.