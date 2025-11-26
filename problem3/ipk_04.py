from tkinter import*

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.course = []

    def enrollCourse(self, subject):
        self.subject = subject
        self.course.append(subject)

    def clearCourses(self):
        self.course.clear()

root = Tk()
root.title("문제4")
root.geometry("380x280")
label = Label(root, text = "학생: 홍길동")
label.pack()

frame = Frame(root)
frame.pack(pady=10, anchor="center")

var_py  = IntVar(value=0)
var_ai  = IntVar(value=0)
var_ds  = IntVar(value=0)

c1 = Checkbutton(frame, text="Python",      variable=var_py)
c2 = Checkbutton(frame, text="AI",          variable=var_ai)
c3 = Checkbutton(frame, text="DataScience", variable=var_ds)

c1.grid(row=0, column=0, padx=8, pady=4)
c2.grid(row=0, column=1, padx=8, pady=4)
c3.grid(row=0, column=2, padx=8, pady=4)

result = StringVar(value = "과목을 선택하고 [등록하기]를 누르세요.")
label2 = Label(root, textvariable = result, wraplength = 300, justify="left")
label2.pack(pady = 10)

s = Student("홍길동")

def register_courses():
    s.clearCourses()
    if var_py.get(): s.enrollCourse("Python")
    if var_ai.get(): s.enrollCourse("AI")
    if var_ds.get(): s.enrollCourse("DataScience")

    # 결과 표시
    if s.course:
        result.set(f"등록된 과목: {', '.join(s.course)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0); var_ai.set(0); var_ds.set(0)
    s.clearCourses()
    result.set("모든 선택을 해제했습니다.")

# 버튼 영역
bframe = Frame(root)
bframe.pack(pady = 6)

Button(bframe, text = "등록하기", command = register_courses).pack(side = "left", padx = 8)
Button(bframe, text = "초기화",   command = reset_all).pack(side = "left", padx=8)

root.mainloop()