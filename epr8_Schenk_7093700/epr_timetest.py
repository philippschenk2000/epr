""" This script contains the time stopping function for the new exercise in epr """

__author__ = "7093700, Schenk 8017459, Ratnakumar"


import time
import timeit

import epr_exercise1


def main(matrix):
    """ This function stops the time for the two exercises/ two different ways to go through the matrix.

    """
    starting_point = (1, 1)
    # 100 at the beginning and 100 et the end as well as one extra line of 100s at first position as well as at the end
    matrix_with_borders = epr_exercise1.create_borders(matrix, 100)
    print('This is the matrix with borders of value=100:')
    [print(row) for row in matrix_with_borders]

    # case: the matrix just contains one row and one column
    ending_point = (len(matrix_with_borders) - 1, len(matrix_with_borders) - 1)
    if starting_point == ending_point:
        return [starting_point]

    # always: starting point as well as the costs at the starting point should be included
    path = [starting_point]
    costs = [matrix_with_borders[1][1]]
    print('\n', '-' * 50, '1) This part is for the local optimum', '-' * 50)
    # set the first time before the function
    start_time = time.time()
    start_timeit = timeit.timeit()
    # recursively walks the matrix locally/ based on the values of the direct neighbours
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
    # set the first time before the function
    start_time = time.time()
    start_timeit = timeit.timeit()
    # recursively walks the matrix globally/ based on the values of all possible ways to go in the matrix
    optimal_path, optimal_costs = epr_exercise1.walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    end_time = time.time()
    end_timeit = timeit.timeit()
    print(optimal_path, sum(optimal_costs))
    # print the time difference
    print('Needed time (in seconds, with package time):', end_time - start_time)
    print('Needed time (in seconds, with package timeit):', end_timeit - start_timeit)
    print('The optimal path for the starting point to go to the end point is:\n', optimal_path[0])
    print('The costs for the optimal path would be:', optimal_costs[0])


testset = [
    [[4, 0, 8], [-3, -4, 7], [-8, -1, 7]],
    [[4, 0, 8, -4], [-3, -4, 7, -5], [-8, -1, 7, 1], [-4, -4, 6, 1]],
    [[4, 0, 8, -4, 8], [-3, -4, 7, -5, 8], [-8, -1, 7, 1, -4], [-4, -4, 6, 1, -1], [-4, -4, 6, 1, -1]],
    [[4, 0, 8, -4, 8, 9], [-3, -4, 7, -5, 8, 9], [-8, -1, 7, 1, -4, 7], [-4, -4, 6, 1, -1, -3],
     [-4, -4, 6, 1, -1, 8], [-4, -4, 6, 1, -1, 8]],
    [[4, 0, 8, -4, 8, 9, -4], [-3, -4, 7, -5, 8, 9, -2], [-8, -1, 7, 1, -4, 7, 2], [-4, -4, 6, 1, -1, -3, -3],
     [-4, -4, 6, 1, -1, 8, -4], [-4, -4, 6, 1, -1, 8, -1], [-4, -4, 6, 1, -1, 8, -1]],
    [[4, 0, 8, -4, 8, 9, -4, 4], [-3, -4, 7, -5, 8, 9, -2, 9], [-8, -1, 7, 1, -4, 7, 2, 1], [-4, -4, 6, 1, -1, -3, -3, -2],
     [-4, -4, 6, 1, -1, 8, -4, -2], [-4, -4, 6, 1, -1, 8, -1, 3], [-4, -4, 6, 1, -1, 8, -1, 5], [-4, -4, 6, 1, -1, 8, -1, 7]],
    [[4, 0, 8, -4, 8, 9, -4, 4, 9], [-3, -4, 7, -5, 8, 9, -2, 9, 5], [-8, -1, 7, 1, -4, 7, 2, 1, 4], [-4, -4, 6, 1, -1, -3, -3, -2, 4],
     [-4, -4, 6, 1, -1, 8, -4, -2, 4], [-4, -4, 6, 1, -1, 8, -1, 3, 4], [-4, -4, 6, 1, -1, 8, -1, 5, 4], [-4, -4, 6, 1, -1, 8, -1, 7, 4], [-4, -4, 6, 1, -1, 8, -1, 7, 4]],
    [[4, 0, 8, -4, 8, 9, -4, 4, 9, -2], [-3, -4, 7, -5, 8, 9, -2, 9, 5, -2], [-8, -1, 7, 1, -4, 7, 2, 1, 4, -2], [-4, -4, 6, 1, -1, -3, -3, -2, 4, -2],
     [-4, -4, 6, 1, -1, 8, -4, -2, 4, -2], [-4, -4, 6, 1, -1, 8, -1, 3, 4, -2], [-4, -4, 6, 1, -1, 8, -1, 5, 4, -2], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2],
     [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2]],
    [[4, 0, 8, -4, 8, 9, -4, 4, 9, -2, 6], [-3, -4, 7, -5, 8, 9, -2, 9, 5, -2, 6], [-8, -1, 7, 1, -4, 7, 2, 1, 4, -2, 1], [-4, -4, 6, 1, -1, -3, -3, -2, 4, -2, 1],
     [-4, -4, 6, 1, -1, 8, -4, -2, 4, -2, 6], [-4, -4, 6, 1, -1, 8, -1, 3, 4, -2, 6], [-4, -4, 6, 1, -1, 8, -1, 5, 4, -2], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1],
     [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6]],
    [[4, 0, 8, -4, 8, 9, -4, 4, 9, -2, 6, 4], [-3, -4, 7, -5, 8, 9, -2, 9, 5, -2, 6, 1], [-8, -1, 7, 1, -4, 7, 2, 1, 4, -2, 1, 2], [-4, -4, 6, 1, -1, -3, -3, -2, 4, -2, 1, 3],
     [-4, -4, 6, 1, -1, 8, -4, -2, 4, -2, 6, -2], [-4, -4, 6, 1, -1, 8, -1, 3, 4, -2, 6, 4], [-4, -4, 6, 1, -1, 8, -1, 5, 4, -2, 8], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, 6],
     [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, -5], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, -1], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6, 2], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6, 7]],
    [[4, 0, 8, -4, 8, 9, -4, 4, 9, -2, 6, 4, -3], [-3, -4, 7, -5, 8, 9, -2, 9, 5, -2, 6, 1, 3], [-8, -1, 7, 1, -4, 7, 2, 1, 4, -2, 1, 2, 1], [-4, -4, 6, 1, -1, -3, -3, -2, 4, -2, 1, 3, 3],
     [-4, -4, 6, 1, -1, 8, -4, -2, 4, -2, 6, -2, -3], [-4, -4, 6, 1, -1, 8, -1, 3, 4, -2, 6, 4, 3], [-4, -4, 6, 1, -1, 8, -1, 5, 4, -2, 8, 1], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, 6, 3],
     [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, -5, -3], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 1, -1, 3], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6, 2, 1], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6, 7, 3], [-4, -4, 6, 1, -1, 8, -1, 7, 4, -2, 6, 7, 3]]
    ]

# test different matrices from the testset
for matrix in testset:
    main(matrix)
    print('_' * 180)
