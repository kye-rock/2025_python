'''문제 4. 과목 선택 프로그램 (Person–Student–Teacher)
1. 클래스 구조
1-1 class Person(name): 이름(name)을 속성으로 초기화한다.
1-2 class Student(Person): Person 클래스를 상속받는다 (is-a 관계).
- 속성: classes (수강 과목 리스트) — has-a 관계
- enrollCourse(subject): 과목을 리스트에 추가한다.
- clearCourses(): 과목 리스트를 초기화한다.
2. Tkinter UI 구성
- 제목: "문제 4"
- 창 크기: 380×280
- 상단 라벨: “학생: 홍길동”
- Checkbutton 3개: “Python”, “AI”, “DataScience”
- 버튼 2개:
  - “등록하기”: 선택된 과목을 Student 객체의 리스트에 저장하고, 결과를 Label에 출력
  - “초기화”: 모든 체크박스를 해제하고, 과목 리스트를 비움
- 하단 라벨: 현재 등록된 과목을 표시 (“등록된 과목: ...”)
3. 동작 요구
- 여러 과목을 동시에 선택할 수 있다.
- 등록 버튼 클릭 시 Student 객체의 has-a 리스트(classes)에 반영된다.
- 초기화 버튼 클릭 시 모든 선택이 해제되고 “모든 선택을 해제했습니다.” 출력.
4. 학습 포인트
- is-a 관계 (상속): Student는 Person의 하위 클래스이다.
- has-a 관계 (구성): Student는 과목 리스트(classes)를 속성으로 가진다.
- Tkinter Checkbutton 활용: 다중 선택 UI 구성 방법을 학습한다.
- 이벤트 처리와 객체 연동: GUI 입력값을 객체의 상태(classes 리스트)에 반영하는 방법을 익힌다.
- 캡슐화와 책임 분리: 데이터 관리(Student 클래스)와 인터페이스 처리(Tkinter GUI)를 구분하여 설계한다.
'''

import tkinter as tk

class Person:
    def __init__(self, name: str):
        self.name = name

class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []  # has-a: 수강 과목 리스트

    def enrollCourse(self, subject: str):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

root = tk.Tk()
root.title("문제 4")
root.geometry("380x280")

stu = Student("홍길동") #객체 생성
title = tk.Label(root, text=f"학생: {stu.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm = tk.Frame(root)
frm.pack(pady=8, anchor="center")

# Checkbutton 상태 변수, 모두 해제되어 있는 상태
var_py  = tk.IntVar(value=0)
var_ai  = tk.IntVar(value=0)
var_ds  = tk.IntVar(value=0)

# Checkbutton 3개
cb1 = tk.Checkbutton(frm, text="Python",      variable=var_py)
cb2 = tk.Checkbutton(frm, text="AI",          variable=var_ai)
cb3 = tk.Checkbutton(frm, text="DataScience", variable=var_ds)

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

# 결과 표시 라벨
result = tk.StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

# 동작 함수들
def register_courses():# 현재 체크 상태를 기준으로 과목 리스트 갱신
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    # 결과 표시
    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0); var_ai.set(0); var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

# 버튼 영역
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="등록하기", command=register_courses).pack(side="left", padx=8)
tk.Button(btn_frame, text="초기화",   command=reset_all).pack(side="left", padx=8)

root.mainloop()