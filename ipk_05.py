import tkinter as tk

class Pet:
    def __init__(self, name):
        self.name = name
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
root.title("문제5")
root.geometry("700x300")

label_title = tk.Label(root, text="반려동물 등록하기", font=("Arial", 14))
label_title.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

kind = tk.StringVar()
kind.set("dog")

rb1 = tk.Radiobutton(root, text="강아지", value="dog", variable=kind)
rb2 = tk.Radiobutton(root, text="고양이", value="cat", variable=kind)
rb1.pack()
rb2.pack()

vax = tk.IntVar()
neutral = tk.IntVar()

chk1 = tk.Checkbutton(root, text="예방접종 완료", variable=vax)
chk2 = tk.Checkbutton(root, text="중성화 완료", variable=neutral)
chk1.pack()
chk2.pack()

label_out = tk.Label(root, text="", fg="blue")
label_out.pack(pady=10)

def register():
    name = entry.get().strip()
    if name == "":
        name = "이름없음"

    if kind.get() == "dog":
        pet = Dog(name)
    else:
        pet = Cat(name)
    person.pet = pet

    v1 = "예방접종 완료" if vax.get() == 1 else "예방접종 미완료"
    v2 = "중성화 완료" if neutral.get() == 1 else "중성화 미완료"

    msg = f"반려동물 등록 완료!\n이름: {pet.name}\n종류: {kind.get()}\n소리: {pet.speak()}\n{v1}, {v2}"
    label_out.config(text=msg)

def reset_all():
    entry.delete(0, tk.END)
    kind.set("dog")
    vax.set(0)
    neutral.set(0)
    label_out.config(text="")

btn_reg = tk.Button(root, text="등록하기", command=register)
btn_reg.pack()

btn_reset = tk.Button(root, text="초기화", command=reset_all)
btn_reset.pack(pady=5)

root.mainloop()

