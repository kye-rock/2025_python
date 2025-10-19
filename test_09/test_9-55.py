class Car:
    def __init__(self, color="white", gear=1, speed=0):
        self.__color = color
        self.__gear = gear
        self.__speed = speed
    
    def setColor(self, c):
        self.__color = c
    
    def setGear(self, g):
        self.__gear = g

    def setSpeed(self, s):
        self.__speed = s

    #def show(self):
        #print(self.__speed, self.__gear, self.__color)
    
    def __str__(self):
        return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)
    
myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.setColor("white")
#myCar.show()
print(myCar)