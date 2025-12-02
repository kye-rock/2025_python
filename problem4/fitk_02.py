import os

def parse_file(path, s):
    str_n = 0
    
    with open(path, "r", encoding = "utf-8") as infile:
        for line in infile:
            str_n += line.count(s)
    return str_n

base_dir = os.path.dirname(__file__)

filename = input("텍스트 파일 이름을 입력하시오: ")
s = input("검색 문자열을 입력하세요: ")

filepath = os.path.join(base_dir, filename)

str_n = parse_file(filepath, s)
print(f"'{s}'(은)는 파일 내에서 {str_n}번 나타납니다.")