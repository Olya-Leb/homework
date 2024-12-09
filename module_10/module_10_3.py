import threading, random, time

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += (random_num:=random.randint(50, 500))
            time.sleep(0.001)
            print(f"Пополнение: {random_num}. Баланс: {self.balance}")

    def take(self):
        for _ in range(100):
            print(f"Запрос на {(random_num:=random.randint(50, 500))}")
            if random_num <= self.balance:
                self.balance -= random_num
                print(f"Снятие: {random_num}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')