from tkinter import *

class Animal:
    def speak(self):
        return ""

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"

def make_sound(a):
    lbl.config(text=a.speak())

root = Tk()
root.title("동물소리듣기")

lbl = Label(root, text="", font=("Arial",18))
lbl.pack()

Button(root, text="강아지", command=lambda: make_sound(Dog())).pack()
Button(root, text="고양이", command=lambda: make_sound(Cat())).pack()
Button(root, text="오리", command=lambda: make_sound(Duck())).pack()

root.mainloop()
