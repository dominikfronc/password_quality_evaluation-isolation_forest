import random
import string
import sys


def get_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(password)


min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
num = int(sys.argv[3])

if min_length > max_length:
    print("Bad input. Minimum length bigger than maximum.")
else:
    for j in range(num):
        len = random.randint(min_length, max_length)
        get_random_password(len)
