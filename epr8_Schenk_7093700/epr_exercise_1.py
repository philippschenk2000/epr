""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk"

import random


def main():
    n = 15
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
    path, costs = walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    print('costs of', sum(costs), 'with the path:', path)
    print('\n', '-' * 50, '2) This part is for the global optimum', '-' * 50)
    best_path = [()]
    best_cost = [100]
    optimal_path, optimal_costs = walk_the_matrix_globally(matrix_with_borders, starting_point[0], starting_point[1], [], 0, best_cost, best_path)
    print('The optimal path for the starting point to go to the end point is:\n', optimal_path)
    print('The costs for the optimal path would be:', optimal_costs[0])


def walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs):
    # CHANGE THE STARTING POINT AND THE NEIGHBORS FROM HERE ON
    if starting_point == ending_point:
        return path, costs
    else:
        #print(path, costs)
        right_neighbour = (starting_point[0], starting_point[1] + 1)
        bottom_neighbour = (starting_point[0] + 1, starting_point[1])
        if max(right_neighbour[1], bottom_neighbour[1]) < len(matrix_with_borders) - 1:
            value_right_neighbour = matrix_with_borders[starting_point[0]][starting_point[1] + 1]
            value_bottom_neighbour = matrix_with_borders[starting_point[0] + 1][starting_point[1]]
            print(value_right_neighbour, 'vs', value_bottom_neighbour)
            # CASE: VALUE FROM BOTH THE SAME
            if value_right_neighbour < value_bottom_neighbour:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            elif value_bottom_neighbour < value_right_neighbour:
                path.append(bottom_neighbour)
                costs.append(value_bottom_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', bottom_neighbour)
                walk_the_matrix_locally(matrix_with_borders, bottom_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            else:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
    return path, costs


def walk_the_matrix_globally(matrix_with_borders, x, y, path, cost, best_cost, best_path):
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


#main()

