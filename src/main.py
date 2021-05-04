# Import packages
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Calculate ackley 
def ackley(X, Y):
    Z = np.zeros((len(X), len(Y)))
    
    factor_1 = -0.02 * np.sqrt(0.5 * (X * X + Y * Y))
    factor_2 = 0.5 * (np.cos(2 * np.pi * X + np.cos(2 * np.pi * Y)))
    
    Z = -20 * np.exp(factor_1) - np.exp(factor_2) + np.exp(1) + 20

    return Z

# Define plotting ackley
def plot_ackley (X, Y, Z):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X, Y, Z, label='Ackley Function')
    plt.show()

# Define plotting ackley contour
def plot_ackley_contour (X, Y, Z):
    ax = plt.axes()
    ax.contour(X, Y, Z)

# Prepare range
wek_x = np.arange(-35,36,1)
wek_y = np.arange(-35,36,1)

X, Y = np.meshgrid(wek_x, wek_y)

# Calculate ackley and plot
Z = ackley(X, Y)

plot_ackley(X, Y, Z)

plot_ackley_contour(X, Y, Z)

def ackley_scalar (x, y):
    factor_1 = -0.02 * np.sqrt(0.5 * (x * x + y * y))
    factor_2 = 0.5 * (np.cos(2 * np.pi * x + np.cos(2 * np.pi * y)))

    return -20 * np.exp(factor_1) - np.exp(factor_2) + np.exp(1) + 20

def hooke_jeeves (SP):
    B_x = [[1,0],[-1,0]]
    B_y = [[0,1],[0,-1]] 
    best_coord = SP
    best_value = ackley_scalar(SP[0], SP[1])
    temp_coord = best_coord
    temp_value = best_value
    
    for xyz in range(10):
        for possible_step in B_x:
            test_value = ackley_scalar(best_coord[0] + possible_step[0], best_coord[1] + possible_step[1])
            if test_value < best_value and test_value < temp_value:
                temp_value = test_value
                temp_coord = [best_coord[0] + possible_step[0], best_coord[1] + possible_step[1]]

        for possible_step in B_y:
            test_value = ackley_scalar(temp_coord[0] + possible_step[0], temp_coord[1] + possible_step[1])
            if test_value < best_value and test_value < temp_value:
                temp_value = test_value
                temp_coord = [temp_coord[0] + possible_step[0], temp_coord[1] + possible_step[1]]

        slope_vector = [temp_coord[0] - best_coord[0], temp_coord[0] - best_coord[0]]

        print(f'Wektor: {slope_vector}:')

        while temp_value < best_value:
            best_coord = temp_coord
            best_value = temp_value
            temp_coord = best_coord[0] + slope_vector[0], best_coord[1] + slope_vector[1]
            temp_value = ackley_scalar(temp_coord[0], temp_coord[1])
            print(best_coord)
            print(best_value)

SP = (2,12)          # Starting position 

hooke_jeeves(SP)