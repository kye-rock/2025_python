'''온도 변환기 클래스 만들기
1. Temperature 클래스를 정의한다.
- 멤버 변수: celsius (섭씨온도)
- 생성자에서 섭씨 값을 초기화한다.
2. to_fahrenheit() 메서드를 작성하여 화씨로 변환한 값을 반환한다.
(공식: 화씨 = 섭씨 × 1.8 + 32)
3. 다음 코드를 실행하면 예시처럼 출력되도록 하시오.
t = Temperature(25)
print("섭씨:", t.celsius)
print("화씨:", t.to_fahrenheit())
'''
class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius  # 섭씨 온도 초기화

  def to_fahrenheit(self):
    # 화씨로 변환 (공식: F = C × 1.8 + 32)
    return self.celsius * 1.8 + 32

# 실행 예시
t = Temperature(25)
print("섭씨:", t.celsius)
print("화씨:", t.to_fahrenheit())