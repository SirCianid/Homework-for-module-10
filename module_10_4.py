from random import randint
from threading import Thread
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    th_list = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        guests_list = len(list(guests))
        guests_tables = min(guests_list, len(self.tables))
        for i in range(guests_tables):
            self.tables[i].guest = guests[i]
            th1 = guests[i]
            th1.start()
            Cafe.th_list.append(th1)
            print(f'{list(guests)[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if guests_list > guests_tables:
            for i in range(guests_tables, guests_list):
                self.queue.put(guests[i])
                print(f'{list(guests)[i].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    th1 = table.guest
                    th1.start()
                    Cafe.th_list.append(th1)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False



tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Mariya', 'Oleg', 'Svyatoslav', 'Sergey', 'Darya', 'Vladimir',
'Viktoriya', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()
for th in Cafe.th_list:
    th.join()