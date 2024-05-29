import threading


class BankAccount:

  def __init__(self):
    self.balance = 0
    self.lock = threading.Lock()

  def deposit(self, amount):
    with self.lock:
      self.balance += amount
      print(f'После пополнения баланс: {self.balance}')

  def withdraw(self, amount):
    with self.lock:
      if self.balance >= amount:
        self.balance -= amount
        print(f'После снятия баланс: {self.balance}')
      else:
        print("Insufficient funds")


account = BankAccount()


def perform_operations():
  for _ in range(10):
    account.deposit(10)
    account.withdraw(5)


threads = []
for i in range(5):
  t = threading.Thread(target=perform_operations)
  t.start()
  threads.append(t)

for t in threads:
  t.join()

print("Final balance:", account.balance)
