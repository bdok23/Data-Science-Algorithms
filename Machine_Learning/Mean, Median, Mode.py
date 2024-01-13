import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.mean(speed)
print(x)

x = np.median(speed)
print(x)

x = stats.mode(speed)
print(x)

x = np.std(speed)
print(x)

x = np.var(speed)
print(x)

x = np.percentile(speed, 90)
print(x)

x = np.random.uniform(0.0, 5.0, 25000) # value range and the number of values
plt.hist(x, 100)
plt.show()

x = np.random.normal(5.0, 1.0, 100000) # mean of 5.0, std of 1.0, 100000 values

