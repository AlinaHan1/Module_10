import threading
import time
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = randint(50, 500)
            self.balance += x
            print(f'Пополнение: {x}. Текущий баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            y = randint(50, 500)
            print(f'Запрос на {y}')
            if self.balance >= y:
                self.balance -= y
                print(f'Снятие: {y}. Текущий баланс: {self.balance}')
            if y > self.balance:
                print('Запрос отклонен. Недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

t1 = threading.Thread(target=Bank.deposit, args=(bk,))
t2 = threading.Thread(target=Bank.take, args=(bk,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'Итоговый баланс: {bk.balance}')
