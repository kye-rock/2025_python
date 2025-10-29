class BankAccount:
  def __init__(self):
    self.__balance = 0

#인출 메소드
  def withdraw(self, amount):
    self.__balance -= amount
    print("통장에",amount, "가 출금되었음")
    return self.__balance

#저축 메소드
  def deposit(self, amount):
    self.__balance += amount
    print("통장에", amount, "가 입금되었음")
    return self.__balance

a = BankAccount()

a.withdraw(10)
a.deposit(100)