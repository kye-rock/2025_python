'''문제 4. Vehicle–Car/Truck 상속 + 운행 기록 파일 저장 프로그램
1. Vehicle 상속 구조
- class Vehicle(name) : 생성자에서 차량 이름을 self.name에 저장한다.
  - drive() 메서드는 기본 구현에서 NotImplementedError를 발생시키고, 자식 클래스에서 오버라이딩하여 사용한다.
- class Car(Vehicle)
  - drive() 호출 시 "승용차 {이름}가 주행합니다." 형식의 문자열을 반환한다.
- class Truck(Vehicle)
  - drive() 호출 시 "트럭 {이름}가 화물을 싣고 주행합니다." 형식의 문자열을 반환한다.
2. 파일 처리 함수
- append_log(message)
  - "drive_log.txt" 파일에, 한 줄씩(message + "\n") 운행 기록을 추가한다.
- clear_log_file()
  - "drive_log.txt" 파일 내용을 모두 지우고 빈 파일로 만든다.
3. Tkinter UI 구성
- 창 제목: "문제4"
- 창 크기: 400×320
- 안내 라벨: 상단에 "차량 이름을 입력하세요:" 문구를 표시한다.
- Entry 위젯: 차량 이름을 입력받는다. (비어 있을 경우 "이름없음"으로 처리)
- 결과 라벨: "결과가 여기에 표시됩니다."를 기본 문구로 두고, 버튼 클릭 시 운행 결과나 안내 문구를 표시한다.
- 버튼 영역(Frame):
  - "자동차 주행" 버튼: drive_car() 함수와 연결
  - "트럭 주행" 버튼: drive_truck() 함수와 연결
  - "로그 비우기" 버튼: clear_log() 함수와 연결
4. 동작 요구
- 자동차 주행 버튼 클릭 시
  - Entry에 입력된 이름을 읽어 공백을 제거하고, 비어 있으면 "이름없음"으로 설정한다.
  - 해당 이름으로 Car 객체를 생성하고, drive()의 반환값(운행 문구)을 message에 저장한다.
  - append_log(message)를 호출하여 "drive_log.txt"에 한 줄 기록한다.
  - 결과 라벨에 message를 출력한다.
- 트럭 주행 버튼 클릭 시 Truck 객체를 생성한 뒤, drive() 결과를 파일에 기록하고 라벨에 표시한다.
- 로그 비우기 버튼 클릭 시, clear_log_file()을 호출하여 "drive_log.txt" 내용을 모두 삭제한다.
  - 결과 라벨에 "로그 파일을 비웠습니다."라는 문구를 표시한다.
5. 학습 포인트
- is-a 관계: Car와 Truck은 Vehicle 클래스를 상속받는 하위 타입이다.
- 메서드 오버라이딩과 다형성: 동일한 drive() 메서드를 가지지만, Car와 Truck에서 서로 다른 문자열을 반환한다.
- 파일 입출력: a 모드(추가 쓰기)와 w 모드(내용 초기화)의 차이를 이해하고, UTF-8 인코딩으로 한글을 안전하게 저장한다.
- Tkinter 이벤트 처리: 버튼 클릭 시 함수를 호출하여 Entry 입력값을 읽고, Label을 갱신하며, 바깥의 파일 처리 로직과 연동하는 GUI 프로그래밍 흐름을 익힌다.
'''
from tkinter import *

# 1. Vehicle 상속 구조 정의
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("drive()는 자식 클래스에서 구현해야 합니다.")

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

# 2. 파일 처리 함수
def append_log(message):
    with open("drive_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def clear_log_file():
    with open("drive_log.txt", "w", encoding="utf-8") as f:
        pass  # 기록 초기화

# 3. Tkinter GUI
root = Tk()
root.title("문제4")
root.geometry("400x320")

Label(root, text="차량 이름을 입력하세요:").pack(pady=5)

# 차량 이름 입력 Entry
name_entry = Entry(root, width=20)
name_entry.pack(pady=5)

result_label = Label(root, text="결과가 여기에 표시됩니다.")
result_label.pack(pady=10)

# 4. 버튼 이벤트 함수
def drive_car():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    car = Car(name)  # Entry로 객체 생성
    message = car.drive()
    append_log(message)
    result_label.config(text=message)

def drive_truck():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    truck = Truck(name)  # Entry로 객체 생성
    message = truck.drive()
    append_log(message)
    result_label.config(text=message)

def clear_log():
    clear_log_file()
    result_label.config(text="로그 파일을 비웠습니다.")

# 버튼 프레임
frame = Frame(root)
frame.pack(pady=15)

Button(frame, text="자동차 주행", width=15, command=drive_car).pack(pady=3)
Button(frame, text="트럭 주행", width=15, command=drive_truck).pack(pady=3)
Button(frame, text="로그 비우기", width=15, command=clear_log).pack(pady=3)

root.mainloop()