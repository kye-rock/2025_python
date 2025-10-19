class Student:
    def __init__(self, name = None, age = 0):
        self.__name  = name
        self.__age = age

    def get_age(self):  #gettet 메소드
        return self.__age
    
    def get_name(self):
        return self.__name

obj = Student()
print(obj.get_name())   #None
print(obj.get_age())    #0