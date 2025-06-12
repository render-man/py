import os
import shutil

n = 4
m = 6

folder = "output"
fname = os.path.join(folder, "d.txt")

def o():
    with open(fname, "w", encoding='utf-8') as f:
        f.write(str(n) + " " + str(m) + "\n")
        for i in range(n):
            for j in range(m):
                f.write(str(i * m + j) + " ")
            f.write("\n")

def r():
    with open(fname, "r", encoding='utf-8') as f:
        (_n, _m) = f.readline().split()
        print("n = {0}, m = {1}".format(_n, _m))
        for l in f.readlines():
            print(l, end='')

os.makedirs(folder, exist_ok=True)
o()
r()
os.makedirs("copy", exist_ok=True)
#shutil.move(fname, os.path.join("copy", "d.txt"))

print("content:")
for file in os.listdir("copy"):
    print(file)