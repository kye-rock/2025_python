from tkinter import*

root = Tk()

canvas = Canvas(root, width = 300, height = 200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)    #(왼쪽위 / 오른쪽 아래)

root.mainloop()