class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getName(self):
        return self.__name
    
    def setName(self, n):
        self.__name = n

    def getAge(self):
        return self.__age
    
    def setAge(self, a):
        self.__name = a

c1 = Cat("Missy", 3)
c2 = Cat("Lucky", 5)

print(c1.getName(), c1.getAge())
print(c2.getName(), c2.getAge())