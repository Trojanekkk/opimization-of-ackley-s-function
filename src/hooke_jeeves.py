# Import packages
import numpy as np

from ackley import *

# Find minimum using Hook-Jeeves algorithm
class Hooke_jeeves:

    # Initialize an object
    def __init__ (self, start_point, step_length, tolerance, step_factor) -> None:
        self.start_point = start_point
        self.step_length = step_length
        self.tolerance = tolerance
        self.step_factor = step_factor

    # Execute the algorithm
    def exec (self) -> dict:
        B_x = [[1,0],[-1,0],[0,0]]
        B_y = [[0,1],[0,-1],[0,0]] 
        best_coord = self.start_point
        best_value = ackley_scalar(self.start_point[0], self.start_point[1])
        temp_coord = best_coord
        temp_value = best_value
        iter = 0
        
        while self.step_length >= self.tolerance:

            # Chose best point from X axis
            for possible_step in B_x:
                test_value = ackley_scalar(best_coord[0] + possible_step[0] * self.step_length, best_coord[1] + possible_step[1] * self.step_length)
                if test_value < best_value and test_value < temp_value:
                    temp_value = test_value
                    temp_coord = [best_coord[0] + possible_step[0] * self.step_length, best_coord[1] + possible_step[1] * self.step_length]

            # Chose best point from Y axis
            for possible_step in B_y:
                test_value = ackley_scalar(temp_coord[0] + possible_step[0] * self.step_length, temp_coord[1] + possible_step[1] * self.step_length)
                if test_value < best_value and test_value < temp_value:
                    temp_value = test_value
                    temp_coord = [temp_coord[0] + possible_step[0] * self.step_length, temp_coord[1] + possible_step[1] * self.step_length]

            # Calculate vector
            slope_vector = [temp_coord[0] - best_coord[0], temp_coord[1] - best_coord[1]]

            # Move point along the vector until find worse value
            while temp_value < best_value:
                best_coord = temp_coord
                best_value = temp_value
                temp_coord = best_coord[0] + slope_vector[0], best_coord[1] + slope_vector[1]
                temp_value = ackley_scalar(temp_coord[0], temp_coord[1])
                iter += 1

            # Reduct step length
            self.step_length *= self.step_factor

        return {
            'best_coord': best_coord,
            'best_value': best_value,
            'iterations': iter,
        }