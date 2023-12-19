""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk 8017459, Ratnakumar"


def create_borders(matrix, border_value):
    """ This function creates one line of borders around our matrix (with value = 100).

    """
    matrix_with_borders = [[border_value for n in range(len(matrix) + 2)]]
    # 100 at the beginning and 100 et the end as well as one extra line of 100s at first position as well as at the end
    for part in matrix:
        matrix_with_borders.append([border_value] + part + [border_value])
    matrix_with_borders.append([border_value for n in range(len(matrix) + 2)])
    return matrix_with_borders


def search_for_lightest_way(matrix_with_borders, starting_point):
    """ This function calls and prints the two functions to walk through the created matrix.

    """
    # case: the matrix just contains one row and one column
    ending_point = (len(matrix_with_borders) - 1, len(matrix_with_borders) - 1)
    if starting_point == ending_point:
        return [starting_point]

    # always: starting point as well as the costs at the starting point should be included
    path = [starting_point]
    costs = [matrix_with_borders[1][1]]
    # recursively walks the matrix locally/ based on the values of the direct neighbours
    path, costs = walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    print(path, sum(costs))

    best_path = [()]
    best_cost = [100]
    # recursively walks the matrix globally/ based on the values of all possible ways to go in the matrix
    optimal_path, optimal_costs = walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    print(optimal_path, sum(optimal_costs))


def walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs):
    """ This function walks the matrix based on the local neighbours.

    """
    # case: goal/ end point is reached
    if starting_point == ending_point:
        return path, costs
    else:
        # look at the neighbours, to the right and down
        right_neighbour = (starting_point[0], starting_point[1] + 1)
        bottom_neighbour = (starting_point[0] + 1, starting_point[1])
        if max(right_neighbour[1], bottom_neighbour[1]) < len(matrix_with_borders) - 1:
            # look at the values from both possible neighbours
            value_right_neighbour = matrix_with_borders[starting_point[0]][starting_point[1] + 1]
            value_bottom_neighbour = matrix_with_borders[starting_point[0] + 1][starting_point[1]]
            # case 1: right neighbour is less expensive than the bottom one
            if value_right_neighbour < value_bottom_neighbour:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
            # case 2: right neighbour is more expensive than the bottom one
            elif value_bottom_neighbour < value_right_neighbour:
                path.append(bottom_neighbour)
                costs.append(value_bottom_neighbour)
                walk_the_matrix_locally(matrix_with_borders, bottom_neighbour, ending_point, path, costs)
            # case 3: both neighbours have the same costs
            else:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
    return path, costs



def walk_the_matrix_globally(matrix_with_borders, x, y, path, cost, best_cost, best_path):
    """ This function walks the matrix in every possible way to get the global optimal path.

    """
    # borders of matrix reached
    if x >= len(matrix_with_borders) - 1 or y >= len(matrix_with_borders[0]) - 1:
        return
    # stops before going to a visited cell
    if (x, y) in path:
        return

    # new path and new costs
    path.append((x, y))
    cost = cost + matrix_with_borders[x][y]

    # look if the new starting point is at the end point and a path is completed
    if x == len(matrix_with_borders) - 2 and y == len(matrix_with_borders[0]) - 2:
        # set the new costs to the minimum costs if a less expensive path was found
        if cost < best_cost[0]:
            best_cost[0] = cost
            best_path[0] = list(path)
    else:
        # calls the function again / recursively with new x and y - values as starting point.
        walk_the_matrix_globally(matrix_with_borders, x + 1, y, path, cost, best_cost, best_path)
        walk_the_matrix_globally(matrix_with_borders, x, y + 1, path, cost, best_cost, best_path)

    path.pop()
    return best_path, best_cost


def doc_tests():
    """ This functions contains the doc tests on the two ways to walk the created matrix.
    >>> search_for_lightest_way(create_borders([[4, 0], [-1, 7]], 100), (1, 1))
    [(1, 1), (2, 1), (2, 2)] 10
    [[(1, 1), (2, 1), (2, 2)]] 10
    >>> search_for_lightest_way(create_borders([[4, 0, 8], [-3, -4, 7], [-8, -1, 7]], 100), (1, 1))
    [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)] -1
    [[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]] -1
    >>> search_for_lightest_way(create_borders([[4, 0, 8, -4], [-3, -4, 7, -5], [-8, -1, 7, 1], [-4, -4, 6, 1]], 100), (1, 1))
    [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)] -8
    [[(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]] -8
    """
