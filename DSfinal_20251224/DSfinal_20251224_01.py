'''문제 3. Shape 계층(사각형·원) 오버라이딩 + Canvas에 그리기
1. 클래스 구조
1-1. class Shape(x, y)
  - 생성자에서 좌표 (x, y)를 초기화한다.
  - area(), perimeter(), draw(canvas)는 추상 메서드로 정의한다.
1-2. class Rectangle(Shape)
  - 생성자에서 (x, y, w, h)를 받아 초기화한다.
  - area(): w * h
  - perimeter(): 2 * (w + h)
  - draw(canvas): create_rectangle()을 이용하여 사각형을 그림. (색상 tomato)
1-3. class Circle(Shape)
  - 생성자에서 (x, y, r)을 받아 초기화한다.
  - area(): πr²
  - perimeter(): 2πr
  - draw(canvas): create_oval()을 이용하여 원을 그림. (색상 skyblue)
2. Tkinter UI 구성
- 제목: "문제3"
- 창크기: 300×220 (배경 흰색)
- Radiobutton 2개: "사각형", "원"
- “그리기” 버튼 클릭 시
  ① Canvas를 초기화한다.
  ② 선택된 도형(Rectangle 또는 Circle)을 생성하여 draw(canvas) 호출
  ③ 하단 Label에 “면적=값, 둘레=값” 형식으로 표시한다.
- 좌표 및 크기 값은 고정:
  - 사각형: (50, 50), 폭=100, 높이=60
  - 원: 중심 (150, 110), 반지름 r=40
3. 학습 포인트
- is-a 관계: Shape → Rectangle, Circle (상속)
- 오버라이딩: area(), perimeter(), draw()
- 다형성: 동일한 draw() 호출로 다른 도형이 그려짐
- Tkinter: Canvas 위젯과 Radiobutton 활용
'''

import tkinter as tk
import math

class Shape:
    def __init__(self, x, y): self.x, self.y = x, y
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError
    def draw(self, canvas): raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y); self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="tomato")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y); self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="skyblue")

root = tk.Tk()
root.title("문제3")
canvas = tk.Canvas(root, width=300, height=220, bg="white")
canvas.pack(pady=6)

var = tk.StringVar(value="rect")
info = tk.StringVar(value="도형을 선택하고 그리기를 누르세요.")
tk.Label(root, textvariable=info).pack()

frm = tk.Frame(root); frm.pack(pady=6, anchor="center")
tk.Radiobutton(frm, text="사각형", value="rect", variable=var).pack(side="left", padx=6)
tk.Radiobutton(frm, text="원", value="circle", variable=var).pack(side="left", padx=6)

def draw_shape():
    canvas.delete("all")
    if var.get() == "rect":
        s = Rectangle(50, 50, 100, 60)
    else:
        s = Circle(150, 110, 40)
    s.draw(canvas)
    info.set(f"면적={s.area():.2f}, 둘레={s.perimeter():.2f}")

tk.Button(root, text="그리기", command=draw_shape).pack(pady=6)
root.mainloop()