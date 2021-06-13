# Import packages
from ackley import *

#  Find minimum using Gradient Descent algorithm
class Gradient_descent:

    # Initialize an object
    def __init__ (self, start_point, tolerance, step_factor, max_iter, h) -> None:
        self.start_point = start_point
        self.tolerance = tolerance
        self.step_factor = step_factor
        self.max_iter = max_iter
        self.h = h

    # Execute the algorithm
    def exec (self) -> dict:
        prev_step = self.start_point - self.tolerance
        step = self.start_point
        iter = 0

        # Check if maximum iterations is reached
        while iter < self.max_iter:
            # Check if tolerance is exceeded
            if (self.tolerance > np.linalg.norm(step - prev_step)):
                break

            prev_step = step.copy()
            
            # Calculate the vector and move
            vector = - self.step_factor * ackley_gradient(step[0], step[1], self.h)
            step += vector

            iter += 1

        return {
            'best_coord': step,
            'best_value': ackley_scalar(step[0], step[1]),
            'iterations': iter,
            'max_iter_r': (False, True)[iter == self.max_iter]
        }