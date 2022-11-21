#import Liberaries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.random.rand(100, 1)
y = 4 + 5 * x + np.random.rand(100, 1)

reg = LinearRegression()
reg.fit(x, y)

x_vals = np.linspace(0, 1, 100).reshape(-1, 1)
