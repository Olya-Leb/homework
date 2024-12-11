import threading
import time
import random
from queue import Queue

class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests): # прибытие
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self): # обслужить
        while not self.queue.empty or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest and table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables_ = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests_ = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables_)
# Приём гостей
cafe.guest_arrival(*guests_)
# Обслуживание гостей
cafe.discuss_guests()