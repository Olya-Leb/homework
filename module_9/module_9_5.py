class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start # число, с которого начинается итерация
        self.stop = stop # число, на котором заканчивается итерация
        self.step = step # шаг, с которым совершается итерация
        self.pointer = start # указывает на текущее число в итерации (изначально start)

    def __iter__(self):
        """метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора"""
        self.pointer = self.start
        return self

    def __next__(self):
        """метод, увеличивающий атрибут pointer на step.
        В зависимости от знака атрибута step итерация завершится
        либо когда pointer станет больше stop, либо меньше stop"""
        if self.step > 0 and self.pointer > self.stop or self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()