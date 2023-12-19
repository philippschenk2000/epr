""" This script contains the time stopping function for the new exercise in epr """

__author__ = "7093700, Schenk"


import time
import timeit

import epr_exercise1


def main(matrix):
    """ This function stops the time for the two exercises/ two different ways to go through the matrix.

    """
    starting_point = (1, 1)
    matrix_with_borders = epr_exercise1.create_borders(matrix, 100)
    print('This is the matrix with borders of value=100:')
    [print(row) for row in matrix_with_borders]
    # REMEMBER THE PATH FROM NOW ON
    # CALL THE OTHER FUNCTION ONE TIME WHICH CALLS ITSELF RECURSIVELY
    ending_point = (len(matrix_with_borders) - 1, len(matrix_with_borders) - 1)
    if starting_point == ending_point:
        return [starting_point]

    path = [starting_point]
    costs = [matrix_with_borders[1][1]]
    print('\n', '-' * 50, '1) This part is for the local optimum', '-' * 50)
    start_time = time.time()
    start_timeit = timeit.timeit()
    path, costs = epr_exercise1.walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    end_time = time.time()
    end_timeit = timeit.timeit()
    print(path, sum(costs))
    print('Needed time (in seconds, with package time):', end_time - start_time)
    print('Needed time (in seconds, with package timeit):', end_timeit - start_timeit)
    print('Result: costs of', sum(costs), 'with the path:', path)

    print('\n', '-' * 50, '2) This part is for the global optimum', '-' * 50)
    best_path = [()]
    best_cost = [100]
    start_time = time.time()
    start_timeit = timeit.timeit()
    optimal_path, optimal_costs = epr_exercise1.walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    end_time = time.time()
    end_timeit = timeit.timeit()
    print(optimal_path, sum(optimal_costs))
    print('Needed time (in seconds, with package time):', end_time - start_time)
    print('Needed time (in seconds, with package timeit):', end_timeit - start_timeit)
    print('The optimal path for the starting point to go to the end point is:\n', optimal_path[0])
    print('The costs for the optimal path would be:', optimal_costs[0])


testset = [
    [[4, 0, 8], [-3, -4, 7], [-8, -1, 7]],
    [[4, 0, 8, -4], [-3, -4, 7, -5], [-8, -1, 7, 1], [-4, -4, 6, 1]],
    [[4, 0, 8, -4, 8, 9, -4, 4], [-3, -4, 7, -5, 8, 9, -2, 9], [-8, -1, 7, 1, -4, 7, 2, 1], [-4, -4, 6, 1, -1, -3, -3, -2],
     [-4, -4, 6, 1, -1, 8, -4, -2], [-4, -4, 6, 1, -1, 8, -1, 3], [-4, -4, 6, 1, -1, 8, -1, 5], [-4, -4, 6, 1, -1, 8, -1, 7]]
    ]

for matrix in testset:
    main(matrix)
    print('_' * 180)
