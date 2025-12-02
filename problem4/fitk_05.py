from tkinter import*
from tkinter import filedialog, messagebox

def count_stats(filename):
    space = 0
    upper = 0
    lower = 0

    with open(filename, "r", encoding = "utf-8") as infile:
        for line in infile:
            for char in line:
                if char == " ":
                    space += 1
                elif char.isupper():
                    upper += 1
                elif char.islower():
                    lower += 1
    return space, upper, lower

def select():
    file_path = filedialog.askopenfilename(title = "파일을 선택하세요", filetypes = [("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
    if not file_path:
        return
    try:
        space, upper, lower = count_stats(file_path)

        label2.config(text = f"선택된 파일: {file_path}")
        label3.config(text = f"스페이스: {space}, 대문자: {upper}, 소문자: {lower}")
    except:
        messagebox.showerror("에러")
        
root = Tk()
root.title("문제5")
root.geometry("520x220")

labe1l = Label(root, text = "텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.")
labe1l.pack()

button = Button(root, text = "파일 선택", command = select)
button.pack()

label2 = Label(root, text = "선택된 파일: (없음)")
label2.pack()

label3 = Label(root, text = "스페이스: 0, 대문자: 0, 소문자: 0")
label3.pack()

root.mainloop()