filename = "test.txt"

try:
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
