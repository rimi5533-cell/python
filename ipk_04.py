import tkinter as tk

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = []
    def enrollCourse(self, subject):
        self.classes.append(subject)
    def clearCourses(self):
        self.classes = []

stu = Student("홍길동")

root = tk.Tk()
root.title("문제4")
root.geometry("380x280")

label_name = tk.Label(root, text=f"학생: {stu.name}")
label_name.pack(pady=10)

var_py = tk.IntVar()
var_ai = tk.IntVar()
var_ds = tk.IntVar()

chk1 = tk.Checkbutton(root, text="Python", variable=var_py)
chk2 = tk.Checkbutton(root, text="AI", variable=var_ai)
chk3 = tk.Checkbutton(root, text="DataScience", variable=var_ds)
chk1.pack()
chk2.pack()
chk3.pack()

label_out = tk.Label(root, text="")
label_out.pack(pady=10)

def register():
    stu.clearCourses()
    if var_py.get() == 1:
        stu.enrollCourse("Python")
    if var_ai.get() == 1:
        stu.enrollCourse("AI")
    if var_ds.get() == 1:
        stu.enrollCourse("DataScience")
    if len(stu.classes) == 0:
        label_out.config(text="선택된 과목이 없습니다.")
    else:
        label_out.config(text=f"등록된 과목: {', '.join(stu.classes)}")

def reset_all():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    stu.clearCourses()
    label_out.config(text="모든 선택을 해제했습니다.")

btn_reg = tk.Button(root, text="등록하기", command=register)
btn_reg.pack()

btn_clear = tk.Button(root, text="초기화", command=reset_all)
btn_clear.pack(pady=5)

root.mainloop()
