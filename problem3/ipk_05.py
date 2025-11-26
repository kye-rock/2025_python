from tkinter import*

class Pet:
    def __init__(self, name):
        self.name = name

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
root.title("문제 5")
root.geometry("700x300")
label = Label(root, text = "반려동물 등록하기")
label.pack()

s = Person("홍길동")

frame_main = Frame(root)
frame_main.pack(pady=10)

Label(frame_main, text="반려동물 이름:", width = 15, anchor = "e").grid(row = 0, column = 0, padx = 5, pady = 5)
pet_name_entry = Entry(frame_main, width = 25)
pet_name_entry.grid(row = 0, column = 1, columnspan = 3, padx = 5, pady = 5, sticky = "w")

# 종류 선택 (Radiobutton)
Label(frame_main, text="종류:", width=15, anchor="e").grid(row=1, column=0, padx=5, pady=5)
pet_type = StringVar(value = "Dog")
Radiobutton(frame_main, text = "강아지", value = "Dog", variable = pet_type).grid(row = 1, column = 1, padx = 5, sticky = "w")
Radiobutton(frame_main, text = "고양이", value = "Cat", variable = pet_type).grid(row = 1, column = 2, padx = 5, sticky = "w")

# 옵션 선택 (Checkbutton)
Label(frame_main, text="옵션:", width=15, anchor="e").grid(row=2, column=0, padx=5, pady=5)
vaccinated = IntVar(value=0)
neutered = IntVar(value=0)
Checkbutton(frame_main, text="예방접종 완료", variable=vaccinated).grid(row=2, column=1, padx=5, sticky="w")
Checkbutton(frame_main, text="중성화 완료", variable=neutered).grid(row=2, column=2, padx=5, sticky="w")

# 결과 라벨
result_var = StringVar(value="등록 정보를 확인하세요.")
Label(frame_main, textvariable=result_var, fg="blue", wraplength=500, justify="left").grid(row=3, column=0, columnspan=4, pady=15)

# 버튼 기능
def register():
    pet_name = pet_name_entry.get() or "이름없음"
    kind = pet_type.get()
    pet = Dog(pet_name) if kind == "Dog" else Cat(pet_name)
    s.pet = pet

    vac = "O" if vaccinated.get() else "X"
    neu = "O" if neutered.get() else "X"
    kind_kor = "강아지" if kind == "Dog" else "고양이"

    msg = (f"{s.name}의 반려동물 등록 완료!\n"
           f"이름: {pet.name} ({kind_kor})\n"
           f"소리: {pet.speak()}\n"
           f"예방접종: {vac}, 중성화: {neu}")
    result_var.set(msg)

def reset():
    pet_name_entry.delete(0, END)
    pet_type.set("Dog")
    vaccinated.set(0)
    neutered.set(0)
    s.pet = None
    result_var.set("등록 정보를 확인하세요.")

# 버튼 프레임
frm_btn = Frame(root)
frm_btn.pack(pady=5)
Button(frm_btn, text="등록하기", width=12, command=register).pack(side="left", padx=15)
Button(frm_btn, text="초기화", width=12, command=reset).pack(side="left", padx=15)

root.mainloop()