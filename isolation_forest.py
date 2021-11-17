import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

train_data = pd.read_csv(sys.argv[1])
test_data = pd.read_csv(sys.argv[2])

random_state = np.random.RandomState(42)
model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.1), random_state=random_state)

train_values = train_data.values
test_values = test_data.values

#shows histogram for every metric
#train_data.hist(figsize=(20,20), bins = 50, color = "c", edgecolor='black')
#plt.show()

model.fit(train_values)
prediction = model.predict(train_values)

print("Number of points:", len(prediction))
print("Number of anomalies:", (prediction == -1).sum())
print("Number of normal points:", (prediction == 1).sum())
print("Percentage of anomalies:", (prediction < 0).mean()*100)
for e in prediction:
    print(e)
