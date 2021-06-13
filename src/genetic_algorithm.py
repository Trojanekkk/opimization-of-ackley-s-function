# Import packages
import numpy as np
from random import shuffle, randint

from ackley import *

# Find minimum using Genetic Algorithm (GA)
class Genetic_algorithm:

    # Initialize an object
    def __init__ (self, init_population, inheritance_power, bastardness_probability, n_generation) -> None:
        self.init_population = init_population
        self.inheritance_power = inheritance_power
        self.bastardness_probability = bastardness_probability
        self.n_generation = n_generation

    # Execute the algorithm
    def exec (self) -> dict:

        # Init population and calculate value of individuals
        population = []
        for coord in self.init_population:
            population.append({'coord': np.array(coord), 'value': ackley_scalar(coord[0], coord[1])})

        # Evolute generations
        for generation in range(0, self.n_generation):

            # Randomly mix individuals
            shuffle(population)

            # Divide population and groupe in couples
            females = population[0:int(len(population)/2)]
            males = population[int(len(population)/2):]

            grouped_population = list(zip(females, males))
            population = []

            # For every couple create two children - reproduction
            for couple in grouped_population:
                worse = max(couple, key=lambda c: c['value'])
                better = min(couple, key=lambda c: c['value'])

                # Create new DNA, mutate the DNA if the children is a bastard
                vector = np.array([
                    (better['coord'][0] - worse['coord'][0]) * (-1,1)[randint(0,100) > 100 * self.bastardness_probability],
                    (better['coord'][1] - worse['coord'][1]) * (-1,1)[randint(0,100) > 100 * self.bastardness_probability]
                    ])

                # Inject the DNA to a new child
                child_2_coord = worse['coord'] + vector * self.inheritance_power

                # Create a new population - succession
                population.extend([better,{'coord': child_2_coord, 'value': ackley_scalar(child_2_coord[0], child_2_coord[1])}])

        # Select best solution final population
        solution = min(population, key=lambda c: c['value'])
        return {
            'best_coord': solution['coord'],
            'best_value': solution['value'],
            'iterations': self.n_generation
        }