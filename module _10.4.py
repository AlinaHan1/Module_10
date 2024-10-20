from queue import Queue  # для очередности
from threading import Thread  # для потоков
from time import sleep  # для имитации ожидания
from random import randint  # для случайного выбора ожидания


# Класс Стол (хранит информацию, о находящимся за ним гостем)
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


# Класс Гость (гость, поток, при запуске которого происходит задержка)
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


# Класс Кафе (кафе в котором определенное кол-во столов и происходит имитация прибытия и обслуживания гостей)
class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    # Метод прибытие гостей. Если все столы заняты, гость записывается в лист ожидания.
    def guest_arrival(self, *guests):
        free_tables = len(self.tables)
        for guest in guests:
            if not free_tables:
                self.queue.put(guest)
                print(f'{guest.name} в листе ожидания.')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} занял(а) стол № {table.number}.')
                    break
            free_tables -= 1

    # Метод обслуживания гостей. Когда стол освободился, его занимает следующий гость из листа ожидания.
    def discuss_quests(self):
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} закончил(а) и ушел(а).')
                    print(f'Стол № {table.number} свободен.')
                    table.guest = None
                    if not self.queue.empty() and table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} покинул лист ожидания и занял стол № {table.number}')
                        next_guest = table.guest
                        next_guest.start()


# Примеры для проверки:

tables = [Table(number) for number in range(1, 6)]

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria',
                'Nikita', 'Galina', 'Pavel', 'Arina', 'Alexander']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_quests()
