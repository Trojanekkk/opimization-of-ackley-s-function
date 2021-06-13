# Import packages
import numpy as np
from random import uniform

# Algorithms scenarios simulator
class Simulator:

    # Initialize simulation
    def __init__ (self, algorithm, seed=False, iterations=100, init_children_n=1) -> None:
        self.algorithm = algorithm[0]
        self.algorithm_args = algorithm[1:]
        self.iterations = iterations
        self.icn = init_children_n
             
        if (seed):
            self.seed = seed
        else:
            self.seed = self.generate_seed(iterations * self.icn)

    # Run a simulation
    def run (self) -> list:
        self.results = []
        for i in range(self.iterations):
            model = self.algorithm(*self.algorithm_args)
            if (hasattr(model, 'start_point')):
                seed = self.seed[i]
                model.start_point = seed
            else:
                seed = self.seed[i * self.icn: i * self.icn + self.icn]
                model.init_population = seed
            result = model.exec()
            result['seed'] = seed
            self.results.append(result)

        return self.results

    # Calculate avarage, weakest, largest solutions, variance
    def process_results (self) -> dict:
        best_values = [r['best_value'] for r in self.results]
        iterations = [r['iterations'] for r in self.results]
        self.results_summary = {
            'values': {
                'best_solution': np.min(best_values),
                'weakest_solution': np.max(best_values),
                'average': np.average(best_values),
                'standard_deviation':  np.std(best_values)
            },
            'iterations': {
                'most': np.max(iterations),
                'least': np.min(iterations),
                'average': np.average(iterations),
                'standard_deviation': np.std(iterations)
            }
        }

        return self.results_summary

    # Generate list of random start_points
    def generate_seed (self, n) -> list:
        return [np.array(self.generate_sample()) for sample in range(n)]

    # Generate random start_point
    def generate_sample (self) -> list:
        return [round(uniform(-35,35), 2), round(uniform(-35,35), 2)]