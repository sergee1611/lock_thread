from threading import Thread, Lock
from pprint import pprint
from time import sleep

lock = Lock()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.amount = 0

    def deposit_task(self, amount):
        with lock:
            for _ in range(5):
                sleep(1)
                self.balance += amount
                pprint(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw_task(self, amount):
        with lock:
            for _ in range(5):
                sleep(1)
                self.balance -= amount
                pprint(f'Wihdrew {amount}, new balance is {self.balance}')


account = BankAccount(1000)

deposit_thread = Thread(target=account.deposit_task(100))
withdraw_thread = Thread(target=account.withdraw_task(150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
