import os

def merge_file(path_1, path_2, path_3):

    with open(path_1, "r", encoding = "utf-8") as file1:
        file1_r = file1.read()

    with open(path_2, "r", encoding = "utf-8") as file2:
        file2_r = file2.read()

        merge = file1_r + "\n" + file2_r

    with open(path_3, "w", encoding = "utf-8") as file3:
        file3.write(merge)

base_dir = os.path.dirname(__file__)

path_1 = os.path.join(base_dir, "file1.txt")
path_2 = os.path.join(base_dir, "file2.txt")
path_3 = os.path.join(base_dir, "output.txt")

merge_file(path_1, path_2, path_3)