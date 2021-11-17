import sys
import re


def count_digits(p):
    return sum(c.isdecimal() for c in p)


def count_lower(p):
    return sum(c.islower() for c in p)


def count_upper(p):
    return sum(c.isupper() for c in p)


def split_group(p):
    return re.findall('\d+|[A-Z]+|[a-z]+|[^A-Za-z\d]+', p)


def convert_password(password):
    password = password.replace("\n", "")
    v = [0, 0, 0, 0, 0, 0]
    v[0] = len(password)
    v[1] = count_lower(password)
    v[2] = count_upper(password)
    v[3] = count_digits(password)
    v[4] = len(password) - v[1] - v[2] - v[3]
    v[5] = len(split_group(password))
    return v


f = open(sys.argv[1], encoding="utf-8")
print("length,lowercase,uppercase,digits,symbols,groups", end='\n')
for line in f:
    vec = convert_password(line)
    print(vec[0], ",", vec[1], ",", vec[2], ",", vec[3], ",", vec[4], ",", vec[5], sep='', end='\n')
