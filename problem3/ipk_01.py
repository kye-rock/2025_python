from tkinter import*

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
    
class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

car = Car("car1")
truck = Truck("truck1")

root = Tk()
root.geometry("400x300")
root.title("문제1")
label = Label(root, text = "버튼을 눌러보세요.")
label.pack(pady = 10)

def show_car():
    result.set(car.drive())

def show_truck():
    result.set(truck.drive())

f = Frame(root)
f.pack(pady = 10)
result = StringVar(value="")

#lambda
#b1 = Button(f, text = "자동차 주행", command = lambda: result.set(car.drive()))
#b2 = Button(f, text = "트럭 주행", command = lambda: result.set(truck.drive()))
b1 = Button(f, text = "자동차 주행", command = show_car)
b2 = Button(f, text = "트럭 주행", command = show_truck)


b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)

label2 = Label(root, textvariable = result)
label2.pack()

root.mainloop()
