'''
문제 5. 반려동물 등록 프로그램 (Person–Pet–Dog/Cat)
1. 클래스 정의
- class Pet(name): 이름을 받아 저장하고 speak()는 "..." 반환 (부모 클래스)
- class Dog(Pet): speak()는 "멍멍!" 반환
- class Cat(Pet): speak()는 "야옹!" 반환
- class Person(name, pet=None): 사람의 이름과 반려동물(Pet)을 속성으로 가짐 (has-a 관계)
2. Tkinter UI 구성
- 창 제목: "문제 5"
- 창 크기: 700×300
- 제목 라벨: "반려동물 등록하기"
- 입력창: 반려동물 이름을 입력
- Radiobutton: "강아지", "고양이" 중 선택 (종류 선택)
- Checkbutton: "예방접종 완료", "중성화 완료" (옵션 선택)
- Label: 결과 메시지 표시
- "등록하기" 버튼 클릭 시 → 입력 내용과 선택 항목을 반영하여 결과 출력
- "초기화" 버튼 클릭 시 → 모든 선택과 입력 초기화
3. 동작 요구
- 이름이 비어 있으면 "이름없음"으로 처리한다.
- 종류에 따라 Dog 또는 Cat 객체를 생성하여 person.pet에 저장한다.
- speak()의 반환값을 포함해 다음 형식으로 결과를 표시한다.
   출력 예시:
   홍길동의 반려동물 등록 완료!
   이름: 뽀삐 (강아지)
   소리: 멍멍!
   예방접종: O, 중성화: X
4. 학습 포인트
- is-a 상속 관계: Dog, Cat은 Pet의 하위 클래스
- has-a 구성 관계: Person은 Pet 객체를 속성으로 가짐
- 다형성: speak() 메서드를 오버라이딩하여 종류별로 다른 울음소리 출력
- Tkinter GUI 이벤트 처리: Radiobutton, Checkbutton, Entry, Label, Button 활용
'''
import tkinter as tk

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
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet  # has-a 관계

root = tk.Tk()
root.title("문제 5")
root.geometry("700x300")

person = Person("홍길동")

# 제목
tk.Label(root, text="반려동물 등록하기", font=("맑은 고딕", 13, "bold")).pack(pady=8)

# 메인 프레임 (줄 정렬용)
frm_main = tk.Frame(root)
frm_main.pack(pady=10)

# 이름 입력
tk.Label(frm_main, text="반려동물 이름:", width=15, anchor="e").grid(row=0, column=0, padx=5, pady=5)
pet_name_entry = tk.Entry(frm_main, width=25)
pet_name_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="w")

# 종류 선택 (Radiobutton)
tk.Label(frm_main, text="종류:", width=15, anchor="e").grid(row=1, column=0, padx=5, pady=5)
pet_type = tk.StringVar(value="Dog")
tk.Radiobutton(frm_main, text="강아지", value="Dog", variable=pet_type).grid(row=1, column=1, padx=5, sticky="w")
tk.Radiobutton(frm_main, text="고양이", value="Cat", variable=pet_type).grid(row=1, column=2, padx=5, sticky="w")

# 옵션 선택 (Checkbutton)
tk.Label(frm_main, text="옵션:", width=15, anchor="e").grid(row=2, column=0, padx=5, pady=5)
vaccinated = tk.IntVar(value=0)
neutered = tk.IntVar(value=0)
tk.Checkbutton(frm_main, text="예방접종 완료", variable=vaccinated).grid(row=2, column=1, padx=5, sticky="w")
tk.Checkbutton(frm_main, text="중성화 완료", variable=neutered).grid(row=2, column=2, padx=5, sticky="w")

# 결과 라벨
result_var = tk.StringVar(value="등록 정보를 확인하세요.")
tk.Label(frm_main, textvariable=result_var, fg="blue", wraplength=500, justify="left").grid(row=3, column=0, columnspan=4, pady=15)

# 버튼 기능
def register():
    pet_name = pet_name_entry.get() or "이름없음"
    kind = pet_type.get()
    pet = Dog(pet_name) if kind == "Dog" else Cat(pet_name)
    person.pet = pet

    vac = "O" if vaccinated.get() else "X"
    neu = "O" if neutered.get() else "X"
    kind_kor = "강아지" if kind == "Dog" else "고양이"

    msg = (f"{person.name}의 반려동물 등록 완료!\n"
           f"이름: {pet.name} ({kind_kor})\n"
           f"소리: {pet.speak()}\n"
           f"예방접종: {vac}, 중성화: {neu}")
    result_var.set(msg)

def reset():
    pet_name_entry.delete(0, tk.END)
    pet_type.set("Dog")
    vaccinated.set(0)
    neutered.set(0)
    person.pet = None
    result_var.set("등록 정보를 확인하세요.")

# 버튼 프레임
frm_btn = tk.Frame(root)
frm_btn.pack(pady=5)
tk.Button(frm_btn, text="등록하기", width=12, command=register).pack(side="left", padx=15)
tk.Button(frm_btn, text="초기화", width=12, command=reset).pack(side="left", padx=15)

root.mainloop()