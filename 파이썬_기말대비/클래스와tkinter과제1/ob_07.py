'''환율 계산 프로그램 만들기
1. ExchangeRate 클래스를 정의한다.
- 멤버 변수: currency(통화명), rate(환율)
- 생성자(__init__)에서 통화명과 환율(rate)을 초기화한다.

2. 다음 메서드를 작성한다.
- to_won(amount): 입력한 달러 금액(amount)을 원화로 변환하여 반환한다.  
  (공식: 원화 = 금액 × 환율)
- to_dollar(amount): 입력한 원화 금액(amount)을 달러로 변환하여 반환한다.  
  (공식: 달러 = 금액 ÷ 환율)
- update_rate(new_rate): 환율을 새로운 값으로 변경하고,  “USD 환율이 ○○원으로 변경됨”를 출력한다.
- info(): “통화: USD, 현재 환율: 1440원” 형식으로 출력한다.

3. 다음 코드를 실행했을 때 예시와 같이 출력되도록 하시오.
usd = ExchangeRate("USD", 1440)
usd.info()
print("100달러 =", usd.to_won(100), "원")
print("270000원 =", round(usd.to_dollar(270000), 2), "달러")

usd.update_rate(1440)
print("100달러 =", usd.to_won(100), "원")
'''
class ExchangeRate:
  def __init__(self, currency, rate):
    # 생성자: 통화명과 환율 초기화
    self.currency = currency   # 예: USD, JPY 등
    self.rate = rate           # 1달러당 원화 환율

  def to_won(self, amount):    # 달러 → 원화 환산
    return amount * self.rate

  def to_dollar(self, amount): # 원화 → 달러 환산
    return amount / self.rate

  def update_rate(self, new_rate): # 환율 변경
    self.rate = new_rate
    print(f"{self.currency} 환율이 {new_rate}원으로 변경됨.")

  def info(self):
    print(f"통화: {self.currency}, 현재 환율: {self.rate}원")

usd = ExchangeRate("USD", 1440)
usd.info()
print("100달러 =", usd.to_won(100), "원")
print("270000원 =", round(usd.to_dollar(270000), 2), "달러")

usd.update_rate(1400)
print("100달러 =", usd.to_won(100), "원")