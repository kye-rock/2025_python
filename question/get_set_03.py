class Friend:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

x = Friend("홍길동", 20)
x.setAge(-5)
print(x.getAge())