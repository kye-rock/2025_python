from tkinter import *

# 도형을 그리는 함수
def draw_shape():
    canvas.delete("all")  # 이전 그림 지우기
    choice = shape_var.get()

def button_clicked1():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red")

def button_clicked2():
    canvas.delete("all")
    canvas.create_oval(200, 80, 300, 180, fill="blue")

def button_clicked3():
    global img

    img = PhotoImage(file="DS_20251224\moon.gif")

    canvas.create_image(20, 20, anchor=NW, image=img)

def button_clicked4():
    canvas.delete("all")


# 메인 윈도우 생성
root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

# 캔버스
canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()


frame = Frame(root)
frame.pack(pady=10)

button1 = Button(root, text = "사각형", command = button_clicked1).pack(side="left", padx=10)
button2 = Button(root, text = "원", command = button_clicked2).pack(side="left", padx=10)
button3 = Button(root, text = "그림", command = button_clicked3).pack(side="left", padx=10)
button4 = Button(root, text = "지우기", command = button_clicked4).pack(side="left", padx=10)

label = Label(root, text = "버튼을 눌러 도형을 선택하세요.")
label.pack()


root.mainloop()