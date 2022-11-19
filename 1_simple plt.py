#Import Libraries
import numpy as np #For Mathematic Usage
import matplotlib.pyplot as plt # to visual datas


# Add some  random values like X, Y
x = np.random.rand(100, 1) 
y = 4 + 5 * x + np.random.rand(100, 1)

plt.scatter(x, y)
plt.show()
