from zxcvbn import zxcvbn
import sys


f = open(sys.argv[1], encoding="latin-1")
for p in f:
    results = zxcvbn(p[:len(p)-1])
    print(results['guesses'])
