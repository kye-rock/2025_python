from tkinter import*

root = Tk()
photo = PhotoImage(file = "chapter08\dog2.gif") #이미지 파일을 읽어서 tkinter가 표시할 수 있는 이미지 객체로 만듦
label = Label(root, image = photo)  
label.pack()
root.mainloop()