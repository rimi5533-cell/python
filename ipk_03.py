import tkinter as tk
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def draw(self, canvas):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="tomato")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)
    def perimeter(self):
        return 2 * math.pi * self.r
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r, fill="skyblue")

root = tk.Tk()
root.title("문제3")
root.geometry("300x220")

shape_var = tk.StringVar()
shape_var.set("rect")

label_top = tk.Label(root, text="도형을 선택하고 그리기를 누르세요.")
label_top.pack(pady=5)

btn_rect = tk.Radiobutton(root, text="사각형", value="rect", variable=shape_var)
btn_circle = tk.Radiobutton(root, text="원", value="circle", variable=shape_var)
btn_rect.pack()
btn_circle.pack()

canvas = tk.Canvas(root, width=300, height=100, bg="white")
canvas.pack()

label_out = tk.Label(root, text="")
label_out.pack(pady=5)

def draw_shape():
    canvas.delete("all")
    if shape_var.get() == "rect":
        s = Rectangle(50, 50, 100, 60)
    else:
        s = Circle(150, 110, 40)
    s.draw(canvas)
    a = round(s.area(), 2)
    p = round(s.perimeter(), 2)
    label_out.config(text=f"면적={a}, 둘레={p}")

btn_draw = tk.Button(root, text="그리기", command=draw_shape)
btn_draw.pack(pady=5)

root.mainloop()
