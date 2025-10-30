class Inventory:
    def __init__(self, stock):
        self.stock = stock
        print(f"새 상품이 등록되었습니다.")

    # 접근자 (Getter)
    def get_stock(self):
        return self.__stock

    # 설정자 (Setter)
    def set_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            print("재고는 음수가 될 수 없습니다.")

    # 입금 메서드
    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"{self.stock} {amount} 개가 입고되었습니다.")
        else:
            print(f"{self.stock} 잘못된 재고입니다.")
        return self.__stock

    # 출금 메서드
    def remove_stock(self, amount):
        if 0 < amount <= self.__stock:
            self.__stock -= amount
            print(f"{self.stock} {amount} 개가 출고되었습니다.")
        else:
            print(f"{self.stock} 출고 불가능한 수량입니다.")
        return self.__stock


# 실행 예시
a = Inventory(7)

a.add_stock(10)
a.remove_stock(3)

print(f"현재 재고수량: {a.stock} ")
print(f"{a.stock} 계좌의 현재 잔액:", a.get_stock())

a.set_stock(500)
print(f"{a.stock} 수정된 재고 수량", a.get_stock())