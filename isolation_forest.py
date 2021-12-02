import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


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


def convert_to_dataframe(file):
    f = open(file, encoding="utf-8")
    data = []
    for line in f:
        vec = convert_password(line)
        data.append(vec)
    df = pd.DataFrame(data, columns=['length', 'lowercase', 'uppercase', 'digits', 'symbols', 'groups'])
    return df


train_data = convert_to_dataframe(sys.argv[1])
test_data = convert_to_dataframe(sys.argv[2])

#random_state = np.random.RandomState(42)
model = IsolationForest(n_estimators=100, max_features=6)

train_values = train_data.values
test_values = test_data.values

# shows histogram for every metric
#test_data.hist(figsize=(20,20), bins = 50, color = "c", edgecolor='black')
#plt.show()
#train_data.hist(figsize=(20,20), bins = 50, color = "c", edgecolor='black')
#plt.show()

model.fit(train_values)

for s in model.score_samples(test_values):
    print(s)

