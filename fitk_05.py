from tkinter import *
from tkinter import filedialog, messagebox

def count_stats(filename):
    space_cnt = 0
    upper_cnt = 0
    lower_cnt = 0

    f = open(filename, "r", encoding="utf-8")
    for line in f:
        for ch in line:
            if ch == " ":
                space_cnt += 1
            elif ch.isupper():
                upper_cnt += 1
            elif ch.islower():
                lower_cnt += 1
    f.close()
    return space_cnt, upper_cnt, lower_cnt

def select_file():
    fname = filedialog.askopenfilename()
    if fname == "":
        return
    try:
        s, u, l = count_stats(fname)
        label_file.config(text="선택된 파일: " + fname)
        label_result.config(text="스페이스: " + str(s) +
                            ", 대문자: " + str(u) +
                            ", 소문자: " + str(l))
    except:
        messagebox.showerror("오류", "파일을 처리할 수 없습니다.")

root = Tk()
root.title("문제5")
root.geometry("520x220")

top_label = Label(root, text="텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.")
top_label.pack(pady=10)

btn = Button(root, text="파일 선택", command=select_file)
btn.pack()

label_file = Label(root, text="선택된 파일: 없음")
label_file.pack(pady=10)

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
