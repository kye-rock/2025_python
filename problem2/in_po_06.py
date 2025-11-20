from tkinter import*

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"
    
class Duck(Animal):
    def speak(self):
        return "꽥꽥!"
    
def make_sound(animal):
    sound = animal.speak()
    speak_label.config(text = sound)

    
root = Tk()
root.geometry("300x200")
root.title("동물 소리 듣기")

label = Label(root, text = "동물 버튼을 눌러 소리를 들어보세요.")

f = Frame(root)
b1 = Button(f, text = "강아지", command = lambda: make_sound(Dog()))
b2 = Button(f, text = "고양이", command = lambda: make_sound(Cat()))
b3 = Button(f, text = "오리", command = lambda: make_sound(Duck()))

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b3.pack(side = LEFT, padx = 10)

speak_label = Label(root, text = "(여기에 울음소리가 나옵니다)", font = ("Arial", 11, "bold"))

label.pack(pady=10)
f.pack(pady=10)
speak_label.pack(pady=10)

root.mainloop()
