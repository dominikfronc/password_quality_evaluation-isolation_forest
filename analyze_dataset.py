import sys
import re


def analyzedataset(line):
    global count, min_len, max_len, char_count, L, U, S, D, LU, LD, LUD, containssymbol
    count += 1
    char_count += len(line)
    if min_len> len(line):
        min_len = len(line)
    if max_len < len(line):
        max_len = len(line)
    if re.match("(^[a-z]+$)", line):
        L += 1
    if re.match("(^[A-Z]+$)", line):
        U += 1
    if re.match("(^[0-9]+$)", line):
        D += 1
    if re.match("(^[a-zA-Z]+$)", line):
        LU += 1
    if re.match("(^[a-z0-9]+$)", line):
        LD += 1
    if re.match("(^[a-zA-Z0-9]+$)", line):
        LUD += 1
    if not re.match("(^[a-zA-Z0-9]+$)", line):
        containssymbol += 1


count = 0
min_len = 100
max_len = 0
char_count = 0
L = 0
U = 0
D = 0
LU = 0
LD = 0
LUD = 0
containssymbol = 0

f = open(sys.argv[1], encoding="latin-1")
for line in f:
    analyzedataset(line)

print("pocet hesiel: ", count)
print("min dlzka: ", min_len)
print("max dlzka: ", max_len)
print("priemerna dlzka hesla: ", char_count / count)
print("[a-z]: ", L, " %: ", L / count*100)
print("[A-Z]: ", U, " %: ", U / count*100)
print("[0-9]: ", D, " %: ", D / count*100)
print("[a-zA-z]: ", LU, " %: ", LU / count*100)
print("[a-z0-9]: ", LD, " %: ", LD / count*100)
print("[a-zA-z0-9]: ", LUD, " %: ", LUD / count*100)
print("obsahuje spec sym: ", containssymbol, " %: ", containssymbol / count*100)
