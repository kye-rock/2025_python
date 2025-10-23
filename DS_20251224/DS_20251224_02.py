class BankAccount:
  
  def __init__(self, name, balance=0):
    self.name = name
    self.balance = balance
    print(f"{self.name} 계좌가 생성되었습니다.")

  def get_balance(self):
    return self.balance

  def set_balance(self, amount):
      self.balance = amount

  def deposit(self, amount):
        if self.balance >= 0:
            self.balance += amount
            print(f"통장에 {self.balance}원이 입금되었습니다.")
            print("입금 가능")
        else:
            print("입금 불가")
    
  def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"통장에 {self.balance} 원이 출금되었습니다.")
        else:
            print("잔액 부족")
        

a = BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액: ", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액: ", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수덩된 잔액: ", a.get_balance())