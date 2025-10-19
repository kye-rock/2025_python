class Bank:
    def __init__(self):
        self.__balance = 0

#class Bank:
    #def __init__(self, balance = 1000):
        #self.balance = balance

    def withdraw(self, m1):
        self.__balance -= m1
        print(f"통장에서 {m1}가 출금되었음")
        return self.__balance
    
    def deposit(self, m1):
        self.__balance += m1
        print(f"통장에 {m1}가 입금되었음")
        return self.__balance
    
pe = Bank()
pe.withdraw(100)
pe.deposit(10)
