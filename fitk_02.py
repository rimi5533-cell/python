filename = "test.txt"
find_word = "python"

try:
    f = open(filename, "r", encoding="utf-8")
    data = f.read()
    count = data.count(find_word)
    print(find_word, ":", count)
    f.close()
except:
    print("파일 오류")
