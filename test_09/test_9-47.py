class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age
        
s1 = Student("Hong", 20)
print(f"{s1.get_name()} 학생의 나이는 {s1.get_age()}살 입니다.")

s1.set_age(-5)
print(f"{s1.get_name()} 학생의 나이는 {s1.get_age()}살 입니다.")

s1.set_age(25)
print(f"{s1.get_name()} 학생의 나이는 {s1.get_age()}살 입니다.")