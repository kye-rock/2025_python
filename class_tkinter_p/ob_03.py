class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def discount(self, rate):
        self.rate = rate
        self.price = self.price * (1 - self.rate)
        return self.price
    
    def get_info(self):
        print(f"상품명: {self.name}, 가격: {int(self.price)}원")

p1 = Product("운동화", 30000)
p1.discount(0.1)
p1.get_info()