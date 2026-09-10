class BankAccount:

  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance


account = BankAccount(owner="Alice", balance=100)
print(f"New Balance: ${account.deposit(50)}")