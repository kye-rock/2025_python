class Person:
    def __init__(self, name, height, age, weight):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight

    def show_info(self):
        print(f"이름: {self.name}, 키: {self.height}, 나이: {self.age}, 몸무게: {self.weight}")


class Student(Person):
    def __init__(self, name, height, age, weight, student_id, grade, year):
        super().__init__(name, height, age, weight)
        self.student_id = student_id
        self.grade = grade
        self.year = year

    def show_student_info(self):
        self.show_info()
        print(f"학번: {self.student_id}, 학점: {self.grade}, 학년: {self.year}")


class Teacher(Person):
    def __init__(self, name, height, age, weight, teaacher_id, salary, years):
        super().__init__(name, height, age, weight)
        self.teacher_id = teaacher_id
        self.salary = salary
        self.years = years

    def show_teacher_info(self):
        self.show_info()
        print(f"교직원번호: {self.teacher_id}, 월급: {self.salary}, 년차: {self.years}")

stu1 = Student("홍길동", 170, 20, 60, "2023001", "A+", 2)
stu1.show_student_info()

tea1 = Teacher("김선생", 175, 40, 70, "T1001", 300, 10)
tea1.show_teacher_info()