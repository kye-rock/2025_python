'''도서 대출 관리 프로그램
1. Book 클래스를 정의한다.
- 멤버 변수: title, author, borrowed (대출 상태: 기본값 False)
- 생성자에서 책 제목과 저자를 초기화한다.
2. borrow() 메서드를 작성하여 책이 대출 중이 아닐 때 borrowed=True로 바꾸고 "○○이(가) 대출되었습니다." 출력한다.
3. return_book() 메서드를 작성하여 "○○이(가) 반납되었습니다." 출력하고 borrowed=False로 변경한다.
4. 다음 코드를 실행했을 때 예시처럼 출력되도록 하시오.
b1 = Book("파이썬 프로그래밍", "홍길동")
b1.borrow()
b1.return_book()
'''
class Book:
  def __init__(self, title, author):
    self.title = title          # 책 제목
    self.author = author        # 저자
    self.borrowed = False       # 대출 여부 

  def borrow(self):
    if not self.borrowed:
      self.borrowed = True
      print(f"{self.title}이(가) 대출되었습니다.")
    else:
      print(f"{self.title}은(는) 이미 대출 중입니다.")

  def return_book(self):
    if self.borrowed:
      self.borrowed = False
      print(f"{self.title}이(가) 반납되었습니다.")
    else:
      print(f"{self.title}은(는) 대출되지 않은 상태입니다.")

# 실행 예시
b1 = Book("파이썬 프로그래밍", "홍길동")
b1.borrow()
b1.borrow()
b1.return_book()