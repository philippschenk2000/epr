""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk"


def main():
    n = 3
    border_value = 100
    starting_point = (1, 1)     # because of borders (0, 0) --> (1, 1)
    matrix = create_matrix(n)
    matrix_with_borders = create_borders(matrix, border_value)
    search_for_lightest_way(matrix_with_borders, starting_point)


def create_matrix(n):
    """ This function checks if the provided graph is tree.

    """
    matrix = [[4, 0, 8],
                        [-3, -4, 7],
                        [-8, -1, 7]]
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
    print('-' * 50, '1) This part is for the local optimum', '-' * 50)
    path = walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs)
    print('costs of', sum(path[1]), 'with the path:', path[0])
    print('-' * 50, '2) This part is for the global optimum', '-' * 50)
    path = [starting_point]
    costs = [matrix_with_borders[1][1]]
    path = walk_the_matrix_globally(matrix_with_borders, starting_point, ending_point, path, costs)


def walk_the_matrix_locally(matrix_with_borders, starting_point, ending_point, path, costs):
    # CHANGE THE STARTING POINT AND THE NEIGHBORS FROM HERE ON
    if starting_point == ending_point:
        return path, costs
    else:
        #print(path, costs)
        right_neighbour = (starting_point[0], starting_point[1] + 1)
        left_neighbour = (starting_point[0] + 1, starting_point[1])
        if max(right_neighbour[1], left_neighbour[1]) < len(matrix_with_borders) - 1:
            value_right_neighbour = matrix_with_borders[starting_point[0]][starting_point[1] + 1]
            value_left_neighbour = matrix_with_borders[starting_point[0] + 1][starting_point[1]]
            print(value_right_neighbour, 'vs', value_left_neighbour)
            # CASE: VALUE FROM BOTH THE SAME
            if value_right_neighbour < value_left_neighbour:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            elif value_left_neighbour < value_right_neighbour:
                path.append(left_neighbour)
                costs.append(value_left_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', left_neighbour)
                walk_the_matrix_locally(matrix_with_borders, left_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            else:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
    return path, costs


def walk_the_matrix_globally(matrix_with_borders, starting_point, ending_point, path, costs):
    # CHANGE THE STARTING POINT AND THE NEIGHBORS FROM HERE ON
    if starting_point == ending_point:
        return path, costs
    else:
        #print(path, costs)
        right_neighbour = (starting_point[0], starting_point[1] + 1)
        left_neighbour = (starting_point[0] + 1, starting_point[1])

    return path, costs



main()

