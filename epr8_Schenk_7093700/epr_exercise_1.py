""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk"


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
            #print(value_right_neighbour, 'vs', value_bottom_neighbour)
            # CASE: VALUE FROM BOTH THE SAME
            if value_right_neighbour < value_bottom_neighbour:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                #print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
                walk_the_matrix_locally(matrix_with_borders, right_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            elif value_bottom_neighbour < value_right_neighbour:
                path.append(bottom_neighbour)
                costs.append(value_bottom_neighbour)
                #print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', bottom_neighbour)
                walk_the_matrix_locally(matrix_with_borders, bottom_neighbour, ending_point, path, costs)
            # CASE: VALUE FROM BOTH THE SAME
            else:
                path.append(right_neighbour)
                costs.append(value_right_neighbour)
                #print('The walk goes from:', starting_point, 'to', ending_point, 'over the point', right_neighbour)
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


