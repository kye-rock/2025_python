'''
음식 배달 시스템 (오버라이딩 + 조건처리)
1. Food 클래스 : name, price
- __str__() → "메뉴: 김밥, 가격: 3000원"
2. DeliveryFood 클래스 : delivery_fee(배달비) 속성 추가.
- __str__() 오버라이딩 → "메뉴: 김밥, 총 가격: 4000원(배달비 포함)"
3. Order 클래스 
- add_food()로 음식 객체를 리스트에 추가
- show_order()로 전체 주문 출력.
4. DeliveryFood와 Food가 섞여 있어도 다형성으로 각각의 __str__() 호출
'''
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price}원"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = delivery_fee

    def __str__(self):
        total = self.price + self.delivery_fee
        return f"메뉴: {self.name}, 총 가격: {total}원(배달비 포함)"

class Order:
    def __init__(self):
        self.foods = []

    def add_food(self, food):
        self.foods.append(food)

    def show_order(self):
        print("=== 주문 내역 ===")
        for f in self.foods:
            print(f)  # __str__() 자동 호출 (다형성)

f1 = Food("김밥", 3000)
f2 = DeliveryFood("짜장면", 6000, 2000)

order = Order()
order.add_food(f1)
order.add_food(f2)
order.show_order()