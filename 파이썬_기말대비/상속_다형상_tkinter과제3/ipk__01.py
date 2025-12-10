'''문제 1. Vehicle 계층과 다형적 drive() (is-a) + Tkinter 버튼
1. 부모 클래스 Vehicle
- 생성자에서 name 속성을 초기화한다.
- drive() 메서드는 추상 메서드 역할을 하며, 자식 클래스에서 반드시 오버라이드해야 한다.
2. 자식 클래스
- Car 클래스: drive() 실행 시 "승용차 {name}가 주행합니다." 반환
- Truck 클래스: drive() 실행 시 "트럭 {name}가 화물을 싣고 주행합니다." 반환
3. 객체 생성
- Car("car1"), Truck("truck1") 두 객체를 생성한다.
4. Tkinter 구성
- 제목: "문제1"
- 창 크기: 400×300
- 안내 라벨: "버튼을 눌러보세요."
- 버튼 2개
- "자동차 주행" 클릭 시 → Car의 drive() 결과를 출력
- "트럭 주행" 클릭 시 → Truck의 drive() 결과를 출력
- 하단 Label 위젯에 결과가 표시되도록 한다.
5. 학습포인트
- is-a 관계(상속): Car와 Truck은 Vehicle의 하위 클래스
- 오버라이딩: Car.drive() → "승용차 ... 주행합니다.", Truck.drive() → "트럭 ... 화물을 싣고 주행합니다."
- 다형성: drive()라는 동일한 메서드명을 통해 객체의 종류(Car, Truck)에 따라 다르게 동작
- Tkinter: button 활용
'''
import tkinter as tk

#클래스 정의
class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        raise NotImplementedError("이것은 추상메소드입니다.")  # 오버라이딩 필수

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

#객체 생성
car = Car("car1")
truck = Truck("truck1")

#Tkinter UI 구성
root = tk.Tk()
root.title("문제1")
root.geometry("400x300")

#안내 라벨 (고정)
label1 = tk.Label(root, text="버튼을 눌러보세요.", font=("맑은 고딕", 11))
label1.pack(pady=10)

#버튼 프레임
frame = tk.Frame(root)
frame.pack(pady=10)

#버튼 기능 정의

def show_car():
    result.set(car.drive())

def show_truck():
    result.set(truck.drive())

# 버튼 배치
tk.Button(frame, text="자동차 주행", command=show_car).pack(side="left", padx=10)
tk.Button(frame, text="트럭 주행", command=show_truck).pack(side="left", padx=10)

#결과 라벨 (내용 바뀜)
result = tk.StringVar(value="")
label2 = tk.Label(root, textvariable=result, font=("맑은 고딕", 11))
label2.pack(pady=10)

root.mainloop()