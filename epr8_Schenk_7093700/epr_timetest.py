""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk"

import random
import time
import timeit

import epr_exercise_1


def main():
    n = 10
    border_value = 100
    starting_point = (1, 1)     # because of borders (0, 0) --> (1, 1)
    matrix = create_matrix(n)
    matrix_with_borders = create_borders(matrix, border_value)
    search_for_lightest_way(matrix_with_borders, starting_point)


def create_matrix(n):
    """ This function checks if the provided graph is tree.

    """
    matrix = [[random.randint(-9, 9) for _ in range(n)] for _ in range(n)]
    #matrix = [[4, 0, 8], [-3, -4, 7], [-8, -1, 7]]
    return matrix


def create_borders(matrix, border_value):
    matrix_with_borders = [[border_value for n in range(len(matrix) + 2)]]
    for part in matrix:
        matrix_with_borders.append([border_value] + part + [border_value])
    matrix_with_borders.append([border_value for n in range(len(matrix) + 2)])
    return matrix_with_borders


def search_for_lightest_way(matrix_with_borders, starting_point):
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
    path, costs = epr_exercise_1.walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    end_time = time.time()
    end_timeit = timeit.timeit()
    print('Needed time (in seconds, with package time):', end_time - start_time)
    print('Needed time (in seconds, with package timeit):', end_timeit - start_timeit)
    print('Result: costs of', sum(costs), 'with the path:', path)

    print('\n', '-' * 50, '2) This part is for the global optimum', '-' * 50)
    best_path = [()]
    best_cost = [100]
    start_time = time.time()
    start_timeit = timeit.timeit()
    optimal_path, optimal_costs = epr_exercise_1.walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    end_time = time.time()
    end_timeit = timeit.timeit()
    print('Needed time (in seconds, with package time):', end_time - start_time)
    print('Needed time (in seconds, with package timeit):', end_timeit - start_timeit)
    print('The optimal path for the starting point to go to the end point is:\n', optimal_path)
    print('The costs for the optimal path would be:', optimal_costs[0])


main()

