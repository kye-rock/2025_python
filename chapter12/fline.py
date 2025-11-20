infile = open(r"C:\2025_2_python\chapter12\proverbs.txt")

outfile = open(r"C:\2025_2_python\chapter12\output.txt", "w")

i = 1

for line in infile:
    outfile.write(str(i) + ": " + line)

    i += 1

infile.close()
outfile.close()