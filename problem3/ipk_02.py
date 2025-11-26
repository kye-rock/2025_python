from tkinter import*

class Pet:
    def speak(self):
        return "..."
    
class Dog(Pet):
    def speak(self):
        return "멍멍!"
    
class Cat(Pet):
    def speak(self):
        return "야옹!"
    
class Person:
    def __init__(self, name, pet = None):
        self.name = name
        self.pet = pet

root = Tk()
root.title("문제2")
root.geometry("400x200")

label = Label(root, text = "동물을 선택해 주세요.")
label.pack(pady = 10)

person = Person("홍길동")

def select_dog():
    person.pet = Dog() 
    result.set("강아지를 선택했습니다.")

def select_cat():
    person.pet = Cat()
    result.set("고양이를 선택했습니다.")

def speak():
    result.set(f"{person.name}의 반려동물 → {person.pet.speak()}")

f = Frame(root)
f.pack(pady = 10)

b1 = Button(f, text = "강아지 선택", command = select_dog)
b2 = Button(f, text = "고양이 선택", command = select_cat)
b3 = Button(root, text = "말하기", command = speak)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b3.pack()

result = StringVar(value = "")
speak_label = Label(root, textvariable = result, fg = "blue")  #textvariable = StringVar : 값 변경시 자동으로 글자 갱신
speak_label.pack(pady = 10)

root.mainloop()