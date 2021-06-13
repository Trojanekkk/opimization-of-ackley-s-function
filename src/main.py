# Import packages
import numpy as np

from ackley import *

from hooke_jeeves import Hooke_jeeves
from gradient_descent import Gradient_descent
from genetic_algorithm import Genetic_algorithm

from simulator import Simulator

# Prepare range
wek_x = np.arange(-35,36,1)
wek_y = np.arange(-35,36,1)

X, Y = np.meshgrid(wek_x, wek_y)

# Calculate ackley and plot
Z = ackley(X, Y)

plot_ackley(X, Y, Z)

plot_ackley_contour(X, Y, Z)

# Generate seed
seed = Simulator([None, None], init_children_n=20).seed

# Test Hooke-Jeeves algorithm
scenarios = [
    [0.1, 0.005, 0.1], [0.1, 0.005, 0.4], [0.1, 0.005, 0.9],
    [0.1, 0.5, 0.1], [0.1, 0.5, 0.4], [0.1, 0.5, 0.9],
    [0.5, 0.005, 0.1], [0.5, 0.005, 0.4], [0.5, 0.005, 0.9],
    [0.5, 0.5, 0.1], [0.5, 0.5, 0.4], [0.5, 0.5, 0.9],
    [1, 0.500, 0.1], [1, 0.005, 0.4], [1, 0.005, 0.9],
    [1, 0.5, 0.1], [1, 0.5, 0.4], [1, 0.5, 0.9],
    [10, 0.005, 0.1], [10, 0.005, 0.4], [10, 0.005, 0.9],
    [10, 0.5, 0.1], [10, 0.5, 0.4], [10, 0.5, 0.9],
]

for i, s in enumerate(scenarios):
    simulation = Simulator([Hooke_jeeves, None, *s], seed=seed)
    simulation.run()
    print("Scenario " + str(i + 1), simulation.process_results())

# Test Gradient Descent algorithm
scenarios = [
    [1, 0.1], [1, 0.3], [1, 0.5], [1, 0.7], [1, 0.9], 
    [0.5, 0.1], [0.5, 0.3], [0.5, 0.5], [0.5, 0.7], [0.5, 0.9],
    [0.1, 0.1], [0.1, 0.3], [0.1, 0.5], [0.1, 0.7], [0.1, 0.9],
    [0.05, 0.1], [0.05, 0.3], [0.05, 0.5], [0.05, 0.7], [0.05, 0.9],
    [0.01, 0.1], [0.01, 0.3], [0.01, 0.5], [0.01, 0.7], [0.01, 0.9],
    [0.005, 0.1], [0.005, 0.3], [0.005, 0.5], [0.005, 0.7], [0.005, 0.9]
]

for i, s in enumerate(scenarios):
    simulation = Simulator([Gradient_descent, None, *s, 500, 0.1], seed=seed)
    simulation.run()
    print("Scenario " + str(i + 1), simulation.process_results())

# Test Genetic Algorithm
scenarios = [
    [0.1, 0.1, 5], [0.1, 0.4, 5], [0.1, 0.8, 5], [0.4, 0.1, 5], [0.4, 0.4, 5], [0.4, 0.8, 5], [0.8, 0.1, 5], [0.8, 0.4, 5], [0.8, 0.8, 5], 
    [0.1, 0.1, 10], [0.1, 0.4, 10], [0.1, 0.8, 10], [0.4, 0.1, 10], [0.4, 0.4, 10], [0.4, 0.8, 10], [0.8, 0.1, 10], [0.8, 0.4, 10], [0.8, 0.8, 10], 
    [0.1, 0.1, 20], [0.1, 0.4, 20], [0.1, 0.8, 20], [0.4, 0.1, 20], [0.4, 0.4, 20], [0.4, 0.8, 20], [0.8, 0.1, 20], [0.8, 0.4, 20], [0.8, 0.8, 20], 
    [0.1, 0.1, 50], [0.1, 0.4, 50], [0.1, 0.8, 50], [0.4, 0.1, 50], [0.4, 0.4, 50], [0.4, 0.8, 50], [0.8, 0.1, 50], [0.8, 0.4, 50], [0.8, 0.8, 50]
]

for i, s in enumerate(scenarios):
    simulation = Simulator([Genetic_algorithm, None, *s], seed=seed, init_children_n=6)
    simulation.run()
    print("Scenario " + str(i + 1), simulation.process_results())
