import os
base_dir = os.path.dirname(__file__)
filename = input("파일명을 입력하세요: ").strip()
filepath = os.path.join(base_dir, filename)

infile = open(filepath, "r", encoding = "utf=8")

freqs = {}

#파일의 각 줄에 대하여 문자를 추출한다.
#각 문자를 사전 freqs에 추가하며, 이미 있는 문자면 빈도수를 증가시킨다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs)
infile.close()