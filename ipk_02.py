import tkinter as tk

class Pet:
    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

person = Person("홍길동")

root = tk.Tk()
root.title("문제2")
root.geometry("400x200")

label_top = tk.Label(root, text="동물을 선택해 주세요.")
label_top.pack(pady=10)

label_out = tk.Label(root, text="")
label_out.pack(pady=15)

def select_dog():
    person.pet = Dog()
    label_out.config(text="강아지를 선택했습니다.")

def select_cat():
    person.pet = Cat()
    label_out.config(text="고양이를 선택했습니다.")

def speak_now():
    if person.pet is None:
        label_out.config(text="반려동물을 먼저 선택해주세요.")
    else:
        msg = person.pet.speak()
        label_out.config(text=f"{person.name}의 반려동물 → {msg}")

btn_dog = tk.Button(root, text="강아지 선택", command=select_dog)
btn_dog.pack()

btn_cat = tk.Button(root, text="고양이 선택", command=select_cat)
btn_cat.pack()

btn_speak = tk.Button(root, text="말하기", command=speak_now)
btn_speak.pack(pady=5)

root.mainloop()
