class Horse: # класс описывающий лошадь
    x_distance = 0 # пройденный путь
    sound = 'Frrr' # звук, который издаёт лошадь

    def run(self, dx): # dx - изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx

class Eagle: # класс описывающий орла
    y_distance = 0 # высота полёта
    sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл

    def fly(self, dy): # dy - изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy

class Pegasus(Horse, Eagle): # Класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования
# Также обладает методами:
    def move(self, dx, dy): # dx и dy это изменения дистанции
        self.run(dx)
        self.fly(dy)

    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке
        return self.x_distance, self.y_distance

    def voice(self): # печатает значение унаследованного атрибута sound
        print(self.sound)

print(Pegasus.mro())
p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()