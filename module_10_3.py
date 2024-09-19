from threading import Thread, Lock
from random import randint
from time import sleep


class Bank():
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        rand_rep = randint(50, 500)
        with self.lock:
            self.balance += rand_rep
            print(f'Зачисление средств: {rand_rep}. Баланс счета: {self.balance}')
            sleep(0.001)

    def take(self):
        rand_rep = randint(50, 500)
        print(f'Запрос на снятие: {rand_rep}')
        with self.lock:
            if rand_rep <= self.balance:
                self.balance -= rand_rep
                print(f'Списание: {rand_rep}. Баланс счета: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                sleep(0.001)


bank_acc = Bank()


def main():
    global bank_acc
    th1 = Thread(target=bank_acc.deposit)
    th2 = Thread(target=bank_acc.take)

    th1.start()
    th2.start()
    th1.join()
    th2.join()


for i in range(100):
    main()

print(f'Итоговый баланс: {bank_acc.balance}')

