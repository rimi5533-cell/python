from tkinter import *

class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        return "승용차 " + self.name + "가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return "트럭 " + self.name + "가 화물을 싣고 주행합니다."

def append_log(msg):
    f = open("drive_log.txt", "a", encoding="utf-8")
    f.write(msg + "\n")
    f.close()

def clear_log_file():
    f = open("drive_log.txt", "w", encoding="utf-8")
    f.close()

def drive_car():
    name = entry.get().strip()
    if name == "":
        name = "이름없음"
    c = Car(name)
    msg = c.drive()
    append_log(msg)
    label_result.config(text=msg)

def drive_truck():
    name = entry.get().strip()
    if name == "":
        name = "이름없음"
    t = Truck(name)
    msg = t.drive()
    append_log(msg)
    label_result.config(text=msg)

def clear_log():
    clear_log_file()
    label_result.config(text="로그 파일을 비웠습니다.")

root = Tk()
root.title("문제4")
root.geometry("400x320")

label1 = Label(root, text="차량 이름을 입력하세요:")
label1.pack(pady=10)

entry = Entry(root)
entry.pack()

label_result = Label(root, text="결과가 여기에 표시됩니다.")
label_result.pack(pady=20)

frame = Frame(root)
frame.pack()

btn1 = Button(frame, text="자동차 주행", width=15, command=drive_car)
btn1.grid(row=0, column=0)

btn2 = Button(frame, text="트럭 주행", width=15, command=drive_truck)
btn2.grid(row=0, column=1)

btn3 = Button(frame, text="로그 비우기", width=33, command=clear_log)
btn3.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
