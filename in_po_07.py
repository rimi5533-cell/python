from tkinter import *

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def total_price(self, qty):
        return self.price * qty
    def __str__(self):
        return "메뉴: " + self.name + ", 단가: " + str(self.price) + "원"

class DeliveryFood(Food):
    def __init__(self, name, price, fee):
        Food.__init__(self, name, price)
        self.fee = fee
    def total_price(self, qty):
        return self.price * qty + self.fee
    def __str__(self):
        return "메뉴: " + self.name + ", 단가: " + str(self.price) + "원, 배달비: " + str(self.fee) + "원"

class Order:
    def __init__(self):
        self.items = []
    def add(self, food, qty):
        self.items.append((food, qty))
    def clear(self):
        self.items = []
    def total(self):
        t = 0
        for f, q in self.items:
            t += f.total_price(q)
        return t
    def summary(self):
        s = ""
        for f, q in self.items:
            s += f.name + " x " + str(q) + " = " + str(f.total_price(q)) + "원\n"
        s += "총합계: " + str(self.total()) + "원"
        return s

foods = [
    Food("김밥", 3000),
    Food("라면", 4000),
    DeliveryFood("짜장면", 6000, 2000),
    DeliveryFood("치킨", 18000, 3000)
]

order = Order()

root = Tk()
root.title("주문·배달시스템")
root.geometry("650x420")

left = Frame(root)
left.pack(side="left", padx=10, pady=10)
right = Frame(root)
right.pack(side="right", padx=10, pady=10)

Label(left, text="메뉴 목록", font=("Arial",14)).pack()
menu = Listbox(left)
menu.pack()
for f in foods:
    menu.insert(END, f.name)

qty = Spinbox(left, from_=1, to=10, width=5)
qty.pack(pady=5)

def add_item():
    s = menu.curselection()
    if s:
        i = s[0]
        f = foods[i]
        q = int(qty.get())
        order.add(f, q)
        cart.insert(END, f.name + " x " + str(q))
        total_lbl.config(text="총합계: " + str(order.total()) + "원")

Button(left, text="장바구니 담기", command=add_item).pack(pady=5)

cart = Listbox(right)
cart.pack()
total_lbl = Label(right, text="총합계: 0원", font=("Arial",12))
total_lbl.pack(pady=5)

def clear_cart():
    order.clear()
    cart.delete(0, END)
    total_lbl.config(text="총합계: 0원")
    text.delete("1.0", END)

def show_order():
    text.delete("1.0", END)
    text.insert(END, order.summary())

Button(right, text="전체 비우기", command=clear_cart).pack()
Button(right, text="주문하기", command=show_order).pack(pady=3)

text = Text(right, height=8)
text.pack()

root.mainloop()
