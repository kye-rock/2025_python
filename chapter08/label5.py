from tkinter import*

root = Tk()
photo = PhotoImage(file = "chapter08\moon.gif")
w = Label(root, image = photo, justify = "left").pack(side = "right")
message = """움짤로 보는
36년만의
우주쇼
"""
w2 = Label(root,
           padx = 10,
           text = message).pack(side = "left")
root.mainloop()