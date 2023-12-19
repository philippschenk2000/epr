""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk 8017459, Ratnakumar"


def create_borders(matrix, border_value):
    """ This function creates one lie of borders around our matrix (with value = 100).

    """
    matrix_with_borders = [[border_value for n in range(len(matrix) + 2)]]
    for part in matrix:
        matrix_with_borders.append([border_value] + part + [border_value])
    matrix_with_borders.append([border_value for n in range(len(matrix) + 2)])
    return matrix_with_borders


def search_for_lightest_way(matrix_with_borders, starting_point):
    """ This function calls and prints the two functions to walk through the created matrix.

    """
    # REMEMBER THE PATH FROM NOW ON
    # CALL THE OTHER FUNCTION ONE TIME WHICH CALLS ITSELF RECURSIVELY
    ending_point = (len(matrix_with_borders) - 1, len(matrix_with_borders) - 1)
    if starting_point == ending_point:
        return [starting_point]

    path = [starting_point]
    costs = [matrix_with_borders[1][1]]
    path, costs = walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    print(path, sum(costs))

    best_path = [()]
    best_cost = [100]
    optimal_path, optimal_costs = walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    print(optimal_path, sum(optimal_costs))


def walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs):
    """ This function walks the matrix based on the local neighbours.

    """
    # CHANGE THE STARTING POINT AND THE NEIGHBORS FROM HERE ON
    if starting_point == ending_point:
        return path, costs
    else:
        right_neighbour = (starting_point[0], starting_point[1] + 1)
        bottom_neighbour = (starting_point[0] + 1, starting_point[1])
        if max(right_neighbour[1], bottom_neighbour[1]) < len(matrix_with_borders) - 1:
            value_right_neighbour = matrix_with_borders[starting_point[0]][starting_point[1] + 1]
            value_bottom_neighbour = matrix_with_borders[starting_point[0] + 1][starting_point[1]]
            # CASE: VALUE FROM BOTH THE SAME
            if value_right_neighbour < value_bottom_neighbour:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            elif value_bottom_neighbour < value_right_neighbour:
                path.append(bottom_neighbour)
                costs.append(value_bottom_neighbour)
                walk_the_matrix_locally(matrix_with_borders, bottom_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            else:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
    return path, costs



def walk_the_matrix_globally(matrix_with_borders, x, y, path, cost, best_cost, best_path):
    """ This function walks the matrix in every possible way to get the global optimal path.

    """
    if x >= len(matrix_with_borders) - 1 or y >= len(matrix_with_borders[0]) - 1:
        return  # Außerhalb der Matrixgrenzen
    if (x, y) in path:
        return  # Verhindert das erneute Besuchen derselben Zelle

    # Pfad und Kosten aktualisieren
    path.append((x, y))
    cost = cost + matrix_with_borders[x][y]

    # Überprüfen, ob das Ziel erreicht ist
    if x == len(matrix_with_borders) - 2 and y == len(matrix_with_borders[0]) - 2:
        if cost < best_cost[0]:
            best_cost[0] = cost
            best_path[0] = list(path)
    else:
        # Rekursive Aufrufe
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
