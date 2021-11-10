import sys

lowercase = set(range(97, 122))
uppercase = set(range(65, 90))
digits = set(range(48, 57))
symbols = set(range(32, 47)) | set(range(58, 64)) | set(range(91, 96)) | set(range(123, 126))


def convert_password(password):
    vec = [0, 0, 0, 0, 0, 0]
    vec[0] = len(password)-1
    group = 0
    for c in password:
        if ord(c) in lowercase:
            vec[1] += 1
            if group != 1:
                vec[5] += 1
                group = 1
        if ord(c) in uppercase:
            vec[2] += 1
            if group != 2:
                vec[5] += 1
                group = 2
        if ord(c) in digits:
            vec[3] += 1
            if group != 3:
                vec[5] += 1
                group = 3
        if ord(c) in symbols:
            vec[4] += 1
            if group != 4:
                vec[5] += 1
                group = 4
    return vec


f = open(sys.argv[1], encoding="utf-8")
print("length,lowercase,uppercase,digits,symbols,groups", end='\n')
for line in f:
    vec = convert_password(line)
    print(vec[0], ",", vec[1], ",", vec[2], ",", vec[3], ",", vec[4], ",", vec[5], sep='', end='\n')
