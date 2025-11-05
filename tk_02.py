from tkinter import *

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

borrowed_books = []

def update_borrowed_list():
    if borrowed_books:
        text = "\n".join([f"{b.title} ({b.author})" for b in borrowed_books])
    else:
        text = "없음"
    label_list.config(text=text)

def borrow_book():
    title = entry_title.get()
    author = entry_author.get()
    if not title or not author:
        result.config(text="제목과 저자를 입력하세요.", fg="red")
        return
    for b in borrowed_books:
        if b.title == title and b.author == author:
            result.config(text=f"{title}은(는) 이미 대출중입니다.", fg="red")
            return
    new_book = Book(title, author)
    borrowed_books.append(new_book)
    result.config(text=f"{title}이(가) 대출되었습니다.", fg="blue")
    update_borrowed_list()

def return_book():
    title = entry_title.get()
    author = entry_author.get()
    if not title or not author:
        result.config(text="제목과 저자를 입력하세요.", fg="red")
        return
    for b in borrowed_books:
        if b.title == title and b.author == author:
            borrowed_books.remove(b)
            result.config(text=f"{title}이(가) 반납되었습니다.", fg="green")
            update_borrowed_list()
            return
    result.config(text=f"{title}은(는) 대출목록에 없습니다.", fg="red")

root = Tk()
root.title("도서대출관리프로그램 v2")
root.geometry("430x280")

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

Label(root, text="현재 대출중인 도서:").pack()
label_list = Label(root, text="")
label_list.pack()

root.mainloop()
