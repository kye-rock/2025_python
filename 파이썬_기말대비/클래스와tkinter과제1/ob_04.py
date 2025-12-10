'''과목 성적 관리 클래스
1. Course 클래스 정의
- 멤버: name(과목명), scores(리스트, 기본값 빈 리스트)
- 생성자에서 과목명 초기화, scores는 빈 리스트로 시작
2. add_score(s)로 점수 추가
3. avg()로 평균점수 반환
4. info()로 "과목: 파이썬, 평균: 85.0" 형식 문자열 반환

c = Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())  # 과목: 파이썬, 평균: 85.0
'''
class Course:
  def __init__(self, name):
    self.name = name          # 과목명
    self.scores = []          # 점수 리스트 초기화

  def add_score(self, s):
    self.scores.append(s)     # 점수 추가

  def avg(self):
    if len(self.scores) > 0:
      return sum(self.scores) / len(self.scores) #scores가 비어있지 않은 경우에만 
    else:
      return 0   

  def info(self):
    return f"과목: {self.name}, 평균: {self.avg():.1f}"

c = Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())  # 과목: 파이썬, 평균: 85.0