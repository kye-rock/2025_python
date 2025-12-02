import os
base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, input("입력 파일 이름: "))

try:
    with open(infilename, "r", encoding = "utf-8") as infile:
        s = infile.read()
        print(s)
    infile.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")