import numpy as np
import matplotlib.pyplot as plt

N = 2

x_axis = np.linspace(-1, 1, 10000000)
y_axis = lambda x, N: -20 * np.exp(-0.02 * np.sqrt(N ** (-1) * sum(x ** 2 for n in range(N)))) - np.exp(N ** (-1) * sum(np.cos(2 * np.pi * x) for n in range(N))) + 20 + np.e

plt.plot(x_axis, [y_axis(x, N) for x in x_axis])