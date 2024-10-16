from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.sir = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.sir}, на вас напали!')
        enemies = 100
        days = 0
        for i in range(enemies):
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies == 0:
                print(f'{self.sir} сражается {days} дней, осталось 0 врагов')
                break
            if enemies < 0:
                enemies = 0
            print(f'{self.sir} сражается {days} дней, осталось {enemies} врагов')
        print(f'{self.sir} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все сражения окончены!')
