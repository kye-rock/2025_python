'''상품 할인 계산 클래스
1. Product 클래스를 정의한다.
- 멤버 변수: name, price
- 생성자에서 상품명과 가격을 초기화한다.
2. discount(rate) 메서드를 작성하여 할인율(rate)만큼 가격을 낮춘다.
(예: rate가 0.1이면 10% 할인)
3. get_info() 메서드는 "상품명: ○○, 가격: ○○원"을 출력한다.
4. 다음 코드를 실행하면 예시처럼 동작해야 한다.
p1 = Product("운동화", 30000)
p1.discount(0.1)
p1.get_info()  # 상품명: 운동화, 가격: 27000원
'''
class Product:
  def __init__(self, name, price):
    self.name = name       # 상품명
    self.price = price     # 가격

  def discount(self, rate):
    self.price = int(self.price * (1 - rate))

  def get_info(self):
    print(f"상품명: {self.name}, 가격: {self.price}원")

# 실행 예시
p1 = Product("운동화", 30000)
p1.discount(0.1)
p1.get_info()  