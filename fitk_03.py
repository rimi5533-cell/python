file1 = "a.txt"
file2 = "b.txt"
newfile = "merge.txt"

try:
    f1 = open(file1, "r", encoding="utf-8")
    f2 = open(file2, "r", encoding="utf-8")
    f3 = open(newfile, "w", encoding="utf-8")

    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())

    f1.close()
    f2.close()
    f3.close()

    print("병합 완료")
except:
    print("파일 처리 오류")

