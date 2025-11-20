from tkinter import*

root = Tk()
root.geometry("300x100")

button1 = Button(root, text = "버튼1", bg = "red", fg = "white")
button2 = Button(root, text = "버튼1", bg = "green", fg = "black")
button3 = Button(root, text = "버튼1", bg = "blue", fg = "white")

button1.pack(side = LEFT)   #기본적으로 중앙정렬, side 매개변수를 사용하여 좌우 정렬
button2.pack(side = LEFT)
button3.pack(side = LEFT)

root.mainloop()