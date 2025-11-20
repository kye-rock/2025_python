infile = open(r"C:\2025_2_python\chapter12\phones.txt", "r", encoding = "utf-8")

line = infile.readline()
for line in infile:
    line = line.rstrip()
    print(line)     #줄바꿈 생김
infile.close()