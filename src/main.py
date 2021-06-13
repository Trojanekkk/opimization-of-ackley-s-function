# Import packages
import numpy as np

from ackley import *
from hooke_jeeves import Hooke_jeeves
from gradient_descent import Gradient_descent
from genetic_algorithm import Genetic_algorithm

# Prepare range
wek_x = np.arange(-35,36,1)
wek_y = np.arange(-35,36,1)

X, Y = np.meshgrid(wek_x, wek_y)

# Calculate ackley and plot
Z = ackley(X, Y)

plot_ackley(X, Y, Z)

plot_ackley_contour(X, Y, Z)

# Init variables for searching minimum
SP = np.array([35.0,-32.0])     # Starting position 
SL = 6.5                        # Initial step length
E = 0.01                        # Tolerance, minimum step length
SF = 0.3                        # Step factor, step length reduction 

# Run Hook-Jeeves algorithm
model = Hooke_jeeves(SP, SL, E, SF)
result = model.exec()
print(f"Using Hooke-Jeeves algorithm found minimum at {result['best_coord']} with value: {result['best_value']}, it took {result['iterations']} iterations.")

# cont. Init variables for searching minimum
h = 0.00001                     # Derivative distance factor 
MI = 600                        # Maximum allowed iterations (GD)

# Run Gradient Descent algorithm
model = Gradient_descent(SP, E, SF, MI, h)
result = model.exec()
print(f"Using Gradient Descent algorithm found minimum at {result['best_coord']} with value: {result['best_value']}, it took {result['iterations']} iterations. ", ('','Maximum iterations reached')[result['max_iter_r']])

# cont. Init variables for GA                                
SPs = np.array([[35.0,-32.0],[-17.5,19.0],[-9.5,11.0],[-32.0,-21.0],[-7.5,-13.0],[28.0,11.5]])
                                # Starting population
BP = 0.2                        # Bastardness (mutation occure) probability
N_GEN = 50                      # Number of generations to simulate

# Run Genetic Algorithm
model = Genetic_algorithm(SPs, SF, 0.2, 50)
result = model.exec()
print(f"Using Genetic Algorithm found minimum at {result['best_coord']} with value: {result['best_value']}, it took {result['iterations']} iterations.")
