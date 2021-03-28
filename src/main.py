# Import packages
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Calculate ackley 
def ackley(range_array):
    res = np.empty([len(range_array[0])])
    
    for i in range(len(range_array[0])):
        factor_1 = -0.02 * np.sqrt(0.5 * (range_array[0][i] * range_array[0][i] + range_array[1][i] * range_array[1][i]))
        factor_2 = 0.5 * (np.cos(2 * np.pi * range_array[0][i]) + np.cos(2 * np.pi * range_array[1][i]))
        
        res[i] = -20 * np.exp(factor_1) - np.exp(factor_2) + np.exp(1) + 20

    return res

# Plot results
def plot_ackley(x1_range,x2_range):
    range_array = [x1_range,x2_range]
    z_range = ackley(range_array)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x1_range, x2_range, z_range, label='Ackley Function')

# Prepare range
x1_range = []
x2_range = []

for x in np.linspace(-35, 35, 71):
    for y in np.linspace(-35, 35, 71):
        x1_range.append(x)
        x2_range.append(y)
    
plot_ackley(x1_range ,x2_range)