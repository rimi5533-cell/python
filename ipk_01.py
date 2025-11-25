import tkinter as tk

class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        return ""

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

car1 = Car("car1")
truck1 = Truck("truck1")

root = tk.Tk()
root.title("문제1")
root.geometry("400x300")

label_top = tk.Label(root, text="버튼을 눌러보세요.")
label_top.pack(pady=10)

label_out = tk.Label(root, text="")
label_out.pack(pady=20)

def car_drive():
    label_out.config(text=car1.drive())

def truck_drive():
    label_out.config(text=truck1.drive())

btn_car = tk.Button(root, text="자동차 주행", command=car_drive)
btn_car.pack()

btn_truck = tk.Button(root, text="트럭 주행", command=truck_drive)
btn_truck.pack()

root.mainloop()
