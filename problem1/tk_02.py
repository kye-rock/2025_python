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
        
borrowed_books = []
        
def update_borrowed_list():
    if borrowed_books:
        books_str = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
    else:
        books_str = "현재 대출 중인 도서가 없습니다."
    label_list.config(text=f"대출 현황: {books_str}")

def borrow_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()
    if not title or not author:
        label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            label_result.config(text=f"{title}은(는) 이미 대출 중입니다.", fg="red")
            return

    book = Book(title, author)
    borrowed_books.append(book)
    label_result.config(text=f"{title}이(가) 대출되었습니다.", fg="blue")
    update_borrowed_list()

def return_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()

    if not title or not author:
        label_result.config(text="제목과 저자를 모두 입력하세요.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            borrowed_books.remove(b)
            label_result.config(text=f"{title}이(가) 반납되었습니다.", fg="green")
            update_borrowed_list()
            return

    label_result.config(text=f"{title}은(는) 대출 목록에 없습니다.", fg="red")


root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("400x300")

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

label_list = Label(root, text="대출 현황: 현재 대출 중인 도서가 없습니다.", wraplength=400, justify="left")
label_list.pack(pady=10)

root.mainloop()