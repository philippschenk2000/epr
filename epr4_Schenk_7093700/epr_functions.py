""" Hallo hier docstring. """

__author__ = "7093700, Schenk"

import random
import turtle

import matplotlib.pyplot as plt


# achte auf die pep8 hinweise als gelb unterstrichen & ändere except in except xxxerror!
# bei basis aufgabe auch noch die buchstaben


# exercise xy
def decimal_to_octal(zahl):
    """ Hallo hier docstring.


    :param1: integer
    :param2: integer
    :param3: integer
    :return: float
    """
    for ii in range(1):
        try:
            # INPUT OF NUMBER
            zahl = int(zahl)
            # CASE: INPUT = 0
            if zahl == 0:
                print('The octal number (8-bit) would be: \n0')
                break
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
        except:
            print('Input has to be a integer number.')


def decimal_to_basis(zahl, base):
    for ii in range(1):
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
                    break
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
                print(binary_list)
                # THE REST NUMBERS TO REST NUMBERS / REST CHARACTERS
                binary_list2 = []
                for o in binary_list:
                    binary_list2.append(base_string[o])
                # REVERSE THE APPENDED LIST AND THEN PRINT EVERY ELEMENT
                reversed_string = ''.join(list(reversed(binary_list2)))
                print(reversed_string)
                return reversed_string
            except:
                print('Base has to be an integer number (0 or over 0).')
        # CASE: INPUT NOT INTEGER
        except:
            print('Input has to be an integer number (0 or over 0).')


def chaos_turtle(iterations, x_coord, y_coord):
    x_coord_cache = x_coord
    y_coord_cache = y_coord
    x_points = []
    y_points = []
    x1, y1 = 7, 10
    x2, y2 = 5, 4
    x3, y3 = 4, 7
    print('P1: (' + str(x1) + ', ' + str(y1) + ')')
    print('P2: (' + str(x2) + ', ' + str(y2) + ')')
    print('P3: (' + str(x3) + ', ' + str(y3) + ')')
    print('---------' * 4)
    for i in range(iterations):
        point = random.choice([(x1, y1), (x2, y2), (x3, y3)])
        new_x = point[0]
        new_y = point[1]
        half_way_x = (new_x - x_coord) / 2 + x_coord
        half_way_y = (new_y - y_coord) / 2 + y_coord
        print(
            f'{i + 1}: From ({x_coord}, {y_coord}) --> Walk to point P: {point} \n{i + 1}: Stop at ({half_way_x}, {half_way_y})')
        x_coord = half_way_x
        y_coord = half_way_y

        x_points.append(half_way_x)
        y_points.append(half_way_y)
    plt.figure(figsize=(8, 6))
    plt.scatter(x_points, y_points, label='Turtle Walk')
    plt.scatter([x1, x2, x3], [y1, y2, y3], color='red', label='Dreieck')
    plt.scatter(x_coord_cache, y_coord_cache, color='blue', label='Start', s=100)
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color='red')
    plt.title("Turtle Walking Diagram")
    plt.legend()
    plt.grid(True)
    plt.show()


def chaos_turtle2(iterations, x_coord, y_coord):
    turtle.speed(0.001)
    turtle.penup()
    x_coord_cache = x_coord
    y_coord_cache = y_coord
    x_points = []
    y_points = []
    turtle.goto(x_coord_cache, y_coord_cache)
    turtle.shape('arrow')
    x1, y1 = 70, 100
    x2, y2 = 150, 140
    x3, y3 = 40, 300
    print('P1: (' + str(x1) + ', ' + str(y1) + ')')
    print('P2: (' + str(x2) + ', ' + str(y2) + ')')
    print('P3: (' + str(x3) + ', ' + str(y3) + ')')
    print('---------' * 4)
    for i in range(iterations):
        point = random.choice([(x1, y1), (x2, y2), (x3, y3)])
        new_x = point[0]
        new_y = point[1]
        half_way_x = (new_x - x_coord) / 2 + x_coord
        half_way_y = (new_y - y_coord) / 2 + y_coord
        turtle.goto((half_way_x, half_way_y))
        turtle.dot(3)
        print(
            f'{i + 1}: From ({x_coord}, {y_coord}) --> Walk to point P: {point} \n{i + 1}: Stop at ({half_way_x}, {half_way_y})')
        x_coord = half_way_x
        y_coord = half_way_y

        x_points.append(half_way_x)
        y_points.append(half_way_y)
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


if __name__ == '__main__':
    print()
    # a = decimal_to_octal(input('Enter a beautiful decimal number: '))
    # b = decimal_to_basis(input('Enter a beautiful decimal number: '), input('Enter a base for your beautiful number: '))
    # c = chaos_turtle(3, 0, 0)
    #c = chaos_turtle2(3, 0, 0)

