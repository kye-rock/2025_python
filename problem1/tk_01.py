from tkinter import*

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    
    def borrow(self):
        if self.borrowed == False:
            self.borrowed = True
            return f"{self.title}이(가) 대출되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출 중입니다."
        
    def return_book(self):
        if self.borrowed == True:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."
    
# current_book = None

def borrow_book():
    global current_book
    title = entry_title.get()
    author = entry_author.get()
    
    #if current_book is None or current_book.title != title or current_book.author != author:
        #current_book = Book(title, author)
    
    current_book = Book(title, author)
    msg = current_book.borrow()
    label_result.config(text=msg, fg="blue")

def return_book():
    global current_book
    
    msg = current_book.return_book()
    label_result.config(text=msg, fg="green")


root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("400x250")

Label(root, text="도서 대출 관리 프로그램", font=("Arial", 14)).pack(pady=10)

frame_input = Frame(root)
frame_input.pack(pady=10)

Label(frame_input, text="제목:").grid(row=0, column=0, padx=5, pady=5)
Label(frame_input, text="저자:").grid(row=1, column=0, padx=5, pady=5)

entry_title = Entry(frame_input, width=30)
entry_author = Entry(frame_input, width=30)
entry_title.grid(row=0, column=1, padx=5, pady=5)
entry_author.grid(row=1, column=1, padx=5, pady=5)

frame_btn = Frame(root)
frame_btn.pack(pady=10)

Button(frame_btn, text="대출", width=10, command=borrow_book).pack(side="left", padx=10)
Button(frame_btn, text="반납", width=10, command=return_book).pack(side="left", padx=10)

label_result = Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()