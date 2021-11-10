import sys


def ascii_lines(iterable):
    for line in iterable:
        try:
            if all((127 > ord(ch) > 31 or ord(ch) == 10) for ch in line) and (len(line) < 42) and (line != '\n'):
                yield line
        except:
            continue


f = open(sys.argv[1], encoding="latin-1")
for line in ascii_lines(f):
    print(line, end='')
