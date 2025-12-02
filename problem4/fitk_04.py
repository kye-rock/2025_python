from tkinter import*
import os

base_dir = os.path.dirname(__file__)
log_path = os.path.join(base_dir, "drive_log.txt")

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
    
class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

def append_log(message):
    with open(log_path, "a", encoding = "utf-8") as file:
        file.write(message + "\n")

def clear_log_file():
    with open(log_path, "w", encoding = "utf-8") as file:
        pass

root = Tk()
root.geometry("400x320")
root.title("문제4")

label = Label(root, text = "차량 이름을 입력하세요: ")
label.pack(pady = 10)

name_entry = Entry(root, width = 20)
name_entry.pack()

result = Label(root, text = "결과가 여기에 표시됩니다.")
result.pack()

def show_car():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    car = Car(name)
    message = car.drive()
    append_log(message)
    result.config(text = message)

def show_truck():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    truck = Truck(name)
    message = truck.drive()
    append_log(message)
    result.config(text = message)

def clear_log():
    clear_log_file()
    result.config(text = "로그 파일을 비웠습니다.")

f = Frame(root)
f.pack(pady = 10)

b1 = Button(f, text = "자동차 주행", width = 15, command = show_car)
b2 = Button(f, text = "트럭 주행", width = 15, command = show_truck)
b3 = Button(f, text = "로그 비우기", width = 15, command = clear_log)

b1.pack(padx = 5)
b2.pack(padx = 5)
b3.pack(padx = 5)

label2 = Label(root, textvariable = result)
label2.pack()

root.mainloop()