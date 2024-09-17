from threading import Thread, Lock
from time import sleep

lock = Lock()


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали орки Саурона!')
        orcs = 100
        days = 0
        while orcs > 0:
            days += 1
            with lock:
                print(f'{self.name} сражается {days} дней..., осталось {orcs} орков. ')
            sleep(1)
            orcs -= self.power
        with lock:
            print(f"{self.name} одержал победу спустя {days} дней!")


# Создаем двух рыцарей
knight1 = Knight("Боромир", 10)
knight2 = Knight("Арагорн", 20)

# Начинаем сражение
knight1.start()
knight2.start()

# Ожидаем окончания сражения
knight1.join()
knight2.join()

print("Сражение окончилось!")
