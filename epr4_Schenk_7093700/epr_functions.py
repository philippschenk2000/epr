""" This script contains 3 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"

import random
import turtle

import matplotlib.pyplot as plt


# achte auf die pep8 hinweise als gelb unterstrichen & ändere except in except xxxerror!


# exercise 1a
def decimal_to_octal(zahl):
    """ This functions forms the inputted decimal number into a octal number.

    """
    for ii in range(1):
        try:
            # INPUT OF NUMBER
            zahl = int(zahl)
            # CASE: INPUT = 0
            if zahl == 0:
                print('The octal number (8-bit) would be: \n0')
                return '0'
            # CASE: INPUT UNDER 0
            elif zahl < 0:
                print('the input has to be a number over 0 or 0.')
                break
            # USUAL PROCESSING: DIVIDING BY 8 TIL NO REST
            binary_list = []
            while zahl != 0:
                rest = zahl % 8
                ohnerest = zahl - rest
                zahl = ohnerest / 8
                print(zahl, 'rest is:', rest)
                binary_list.append(str(int(rest)))
            # REVERSE THE APPENDED LIST AND THEN PRINT EVERY ELEMENT
            reversed_string = ''.join(list(reversed(binary_list)))
            return reversed_string
        # CASE: INPUT NOT INTEGER
        except ValueError:
            print('Input has to be a integer number.')


# exercise 1b
def decimal_to_basis(zahl, base):
    """ This functions forms the inputted decimal number into number which is formatted by a custom inputted base.

    """
    for ii in range(1):
        # CREATE A STRING TO WORK FOR NUMBERS OVER 9
        base_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        try:
            # INPUT OF NUMBER
            zahl = int(zahl)
            try:
                base = int(base)
                if base > 35:
                    print('The base has to be between 0 and 35 (inclusive both).')
                    break
                # CASE: INPUT = 0
                if zahl == 0:
                    print(f'The number (8-bit) for the base {base} would be: \n0')
                    return '0'
                # CASE: INPUT UNDER 0
                elif zahl < 0:
                    print('the input has to be a number over 0 or 0.')
                    break
                # USUAL PROCESSING: DIVIDING BY 2 TIL NO REST
                binary_list = []
                while zahl != 0:
                    rest = zahl % base
                    ohnerest = zahl - rest
                    zahl = ohnerest / base
                    print(zahl, 'rest is:', rest)
                    binary_list.append(int(rest))
                # THE REST NUMBERS TO REST NUMBERS / REST CHARACTERS
                binary_list2 = []
                for o in binary_list:
                    binary_list2.append(base_string[o])
                # REVERSE THE APPENDED LIST AND THEN PRINT EVERY ELEMENT
                reversed_string = ''.join(list(reversed(binary_list2)))
                print(reversed_string)
                return reversed_string
            except ValueError:
                print('Base has to be an integer number (0 or over 0).')
        # CASE: INPUT NOT INTEGER
        except ValueError:
            print('Input has to be an integer number (0 or over 0).')


# exercise 1c
def chaos_turtle2(iterations, x_coord, y_coord):
    """ This functions plots a running turtle which builds many triangles while being on the route.

    """
    # CREATE TURTLE AND LET IT RUN FASTER
    turtle.speed(0.001)
    turtle.penup()
    # PUT THE START COORDINATES INTO A VARIABLE-CACHE
    x_coord_cache = x_coord
    y_coord_cache = y_coord
    x_points = []
    y_points = []
    # LET TURTLE START AT START COORDINATES
    turtle.goto(x_coord_cache, y_coord_cache)
    turtle.shape('arrow')
    # DEFINE 3 POINTS FOR THE CORNERS OF THE TRIANGLE
    x1, y1 = 70, 100
    x2, y2 = 150, 140
    x3, y3 = 40, 300
    print('P1: (' + str(x1) + ', ' + str(y1) + ')')
    print('P2: (' + str(x2) + ', ' + str(y2) + ')')
    print('P3: (' + str(x3) + ', ' + str(y3) + ')')
    print('---------' * 4)
    # LET THE TURTLE RUN i TIMES IN THE DIRECTION OF A RANDOM CHOSEN CORNER
    for i in range(iterations):
        point = random.choice([(x1, y1), (x2, y2), (x3, y3)])
        new_x = point[0]
        new_y = point[1]
        # LET TURTLE RUN JUST THE HALF OF THE WAY TO ONE RANDOM CORNER
        half_way_x = (new_x - x_coord) / 2 + x_coord
        half_way_y = (new_y - y_coord) / 2 + y_coord
        # SEND TURTLE TO THE HALF ROUTE AND MARK THERE
        turtle.goto((half_way_x, half_way_y))
        turtle.dot(3)
        print(
            f'{i + 1}: From ({x_coord}, {y_coord}) --> Walk to point P: {point} \n{i + 1}: Stop at ({half_way_x}, {half_way_y})')
        # DEFINE THESE POINTS AS THE NEW START COORDINATES FOR THE NEXT RUN
        x_coord = half_way_x
        y_coord = half_way_y

        x_points.append(half_way_x)
        y_points.append(half_way_y)
    # OPTIONAL: PLOT THE TURTLE WALK VIA TURTLE GRAPHICS OR MATPLOTLIB
    turtle.done()
    plt.figure(figsize=(8, 6))
    plt.scatter(x_points, y_points, label='Turtle Walk')
    plt.scatter([x1, x2, x3], [y1, y2, y3], color='red', label='Dreieck')
    plt.scatter(x_coord_cache, y_coord_cache, color='blue', label='Start', s=100)
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color='red')
    plt.title("Turtle Walking Diagram")
    plt.legend()
    plt.grid(True)
    #plt.show()


# CALL THE 3 DIFFERENT FUNCTIONS
if __name__ == '__main__':
    print()
    #a = decimal_to_octal(input('Enter a beautiful decimal number: '))
    #b = decimal_to_basis(input('Enter a beautiful decimal number: '), input('Enter a base for your beautiful number: '))
    #c = chaos_turtle2(100, -100, -100)


# EXERCISE 1a:
# TEST 1:
# IN: 0 SHOULD: 0
# OUT:
# The octal number (8-bit) would be:
# 0
# TEST 2:
# IN: -10 SHOULD: the input has to be a number over 0 or 0.
# OUT: the input has to be a number over 0 or 0.
# TEST 3:
# IN: 294 SHOULD: returns 446
# OUT: (nothing, but returns 446)

# EXERCISE 1b:
# TEST 1:
# IN: 0, 2 SHOULD: 0
# OUT:
# The number (8-bit) for the base 2 would be:
# 0
# TEST 2:
# IN: 3, 0 SHOULD: Base has to be an integer number (0 or over 0).
# OUT: Base has to be an integer number (0 or over 0).
# TEST 3:
# IN: 294, 8 SHOULD: returns 446
# OUT: (nothing, but returns 446)

# EXERCISE 1c:
# TEST 1:
# IN: 30, 0, 0 SHOULD: be as the output
# OUT:
# P1: (70, 100)
# P2: (150, 140)
# P3: (40, 300)
# ------------------------------------
# 1: From (0, 0) --> Walk to point P: (70, 100)
# 1: Stop at (35.0, 50.0)
# 2: From (35.0, 50.0) --> Walk to point P: (150, 140) .... and so on
# CREATES A BIT OF SHAPE IN THE CHART
# TEST 2:
# IN: 100, 100, 100 SHOULD: be as the output
# OUT:
# P1: (70, 100)
# P2: (150, 140)
# P3: (40, 300)
# ------------------------------------
# 1: From (100, 100) --> Walk to point P: (40, 300)
# 1: Stop at (70.0, 200.0)
# 2: From (70.0, 200.0) --> Walk to point P: (150, 140) .... and so on
# TEST 3:
# IN: -100, -100, -100 SHOULD: be as the output
# OUT:
# P1: (70, 100)
# P2: (150, 140)
# P3: (40, 300)
# ------------------------------------
# 1: From (-100, -100) --> Walk to point P: (40, 300)
# 1: Stop at (-30.0, 100.0)
# 2: From (-30.0, 100.0) --> Walk to point P: (70, 100)
