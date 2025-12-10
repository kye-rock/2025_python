'''자동차 주행기록 프로그램
1. Car 클래스 정의
- 멤버: model, odometer(주행거리, 기본 0)
- 생성자에서 모델명 초기화, odometer=0
2. drive(km)로 주행거리 km만큼 증가
3. info()로 "모델: BMW, 주행거리: 120km" 형식 문자열 반환

c = Car("BMW")
c.drive(50)
c.drive(70)
print(c.info())  # 모델: BWM, 주행거리: 120km
'''

class Car:
  def __init__(self, model):
    self.model = model        # 자동차 모델명
    self.odometer = 0         # 주행거리 초기값 0

  def drive(self, km):
    self.odometer += km       # 주행거리 누적

  def info(self):
    return f"모델: {self.model}, 주행거리: {self.odometer}km"

# 실행 예시
c = Car("BMW")
c.drive(50)
c.drive(70)
print(c.info()) 