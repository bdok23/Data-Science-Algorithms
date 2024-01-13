import matplotlib.pyplot as plt
import numpy as np

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

x1 = np.random.normal(5.0, 1.0, 1000)
y1 = np.random.normal(4.0, 2.1, 1000)

plt.scatter(x1, y1)
plt.show()

