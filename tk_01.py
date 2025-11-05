from tkinter import *

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title}이(가) 대출되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출중입니다."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."


def borrow_book():
    title = entry_title.get()
    author = entry_author.get()
    if title and author:
        book = Book(title, author)
        result.config(text=book.borrow(), fg="black")
    else:
        result.config(text="제목과 저자를 입력하세요.", fg="red")

def return_book():
    title = entry_title.get()
    author = entry_author.get()
    if title and author:
        book = Book(title, author)
        result.config(text=book.return_book(), fg="black")
    else:
        result.config(text="제목과 저자를 입력하세요.", fg="red")

root = Tk()
root.title("도서대출관리프로그램")
root.geometry("400x250")

Label(root, text="도서 제목").pack()
entry_title = Entry(root)
entry_title.pack()

Label(root, text="저자").pack()
entry_author = Entry(root)
entry_author.pack()

Button(root, text="대출", command=borrow_book).pack()
Button(root, text="반납", command=return_book).pack()

result = Label(root, text="")
result.pack()

root.mainloop()
