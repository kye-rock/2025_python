'''문제2. Person–Pet 관계 (has-a) + Tkinter Listbox 선택으로 speak() 호출
1. class Pet
- class Pet: speak()는 기본 구현으로 "..."을 반환한다.
- class Dog(Pet): speak() 호출 시 "멍멍!" 반환
- class Cat(Pet): speak() 호출 시 "야옹!" 반환
- class Person(name, pet=None): 사람은 pet 속성(반려동물)을 가진다(has-a).
2. Tkinter UI구성
- 창 제목: "문제2"
- 창 크기: 400×200
- 안내 라벨: 기본 문구는 반려동물을 선택하고 '말하기'를 누르세요.
- 버튼 3개
"강아지 선택": Dog()를 생성해 person.pet에 할당하고, 선택 완료 메시지를 출력
"고양이 선택": Cat()을 생성해 person.pet에 할당하고, 선택 완료 메시지를 출력
"말하기": 현재 person.pet.speak() 결과를 하단 라벨에 표시
3. 동작 요구
- 반려동물을 선택한 뒤 "말하기" 버튼을 누르면 하단 라벨에
- "{사람이름}의 반려동물 → {speak() 결과}" 형식으로 출력한다. 예) 홍길동의 반려동물 → 멍멍!
4. 학습포인트
- has-a 관계: Person 클래스는 Pet 객체를 속성(pet) 으로 가짐
- Dog와 Cat은 Pet 클래스로부터 상속(is-a)
- speak() 메서드를 오버라이딩하여 같은 메서드 이름으로 다른 동작(출력 문자열) 을 수행
Dog.speak() → "멍멍!", Cat.speak() → "야옹!"
- person.pet.speak() 호출시 객체의 실제 타입에 따라 결과가 달라짐
'''

import tkinter as tk

# 클래스 정의
class Pet:
    def speak(self):
        return "..."

class Dog(Pet): # is-a 관계
    def speak(self):
        return "멍멍!"

class Cat(Pet): # is-a 관계
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet  # has-a 관계

# Tkinter 구성
root = tk.Tk()
root.title("문제2")
root.geometry("400x200")

# 고정 안내 라벨
tk.Label(root, text="동물을 선택해 주세요.", font=("맑은 고딕", 12)).pack(pady=10)

# 현재 사람 객체
person = Person("홍길동")

# 버튼 기능 정의
def select_dog():
    person.pet = Dog() 
    result.set("강아지를 선택했습니다.")

def select_cat():
    person.pet = Cat()
    result.set("고양이를 선택했습니다.")

def speak():
    result.set(f"{person.name}의 반려동물 → {person.pet.speak()}")

# 버튼 배치
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="강아지 선택", command=select_dog).pack(side="left", padx=8)
tk.Button(frame, text="고양이 선택", command=select_cat).pack(side="left", padx=8)
tk.Button(root, text="말하기", command=speak).pack(pady=10)

# 동물 선택 결과 표시
result = tk.StringVar(value="")
speak_label = tk.Label(root, textvariable=result, font=("맑은 고딕", 12), fg="blue")
speak_label.pack(pady=10)


root.mainloop()