import random
__author__ = "7093700, Schenk"
import matplotlib.pyplot as plt


def decimal_to_octal(zahl):
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
            # USUAL PROCESSING: DIVIDING BY 2 TIL NO REST
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
        try:
            # INPUT OF NUMBER
            zahl = int(zahl)
            try:
                base = int(base)
                if base > 10:
                    print('The base has to be between 0 and 10 (inclusive both).')
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
                    binary_list.append(str(int(rest)))
                # REVERSE THE APPENDED LIST AND THEN PRINT EVERY ELEMENT
                reversed_string = ''.join(list(reversed(binary_list)))
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
    x1, y1 = random.randint(0, 10), random.randint(0, 10)
    x2, y2 = random.randint(0, 10), random.randint(0, 10)
    x3, y3 = random.randint(0, 10), random.randint(0, 10)
    print('P1: (' + str(x1) + ', ' + str(y1) + ')')
    print('P2: (' + str(x2) + ', ' + str(y2) + ')')
    print('P3: (' + str(x3) + ', ' + str(y3) + ')')
    print('---------'*4)
    for i in range(iterations):
        point = random.choice([(x1,y1), (x2, y2), (x3, y3)])
        new_x = point[0]
        new_y = point[1]
        half_way_x = (new_x - x_coord) / 2 + x_coord
        half_way_y = (new_y - y_coord) / 2 + y_coord
        print(f'{i + 1}: From ({x_coord}, {y_coord}) --> Walk to point P: {point} \n{i + 1}: Stop at ({half_way_x}, {half_way_y})')
        x_coord = half_way_x
        y_coord = half_way_y

        x_points.append(half_way_x)
        y_points.append(half_way_y)
    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points, '-o', label='Turtle Walk')
    plt.scatter([x1, x2, x3], [y1, y2, y3], color='red', label='Dreieck')
    plt.scatter(x_coord_cache, y_coord_cache, color='blue', label='Start', s=100)
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color='red')
    plt.title("Turtle Walking Diagram")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    print()
    #a = decimal_to_octal(input('Enter a beautiful decimal number: '))
    #b = decimal_to_basis(input('Enter a beautiful decimal number: '), input('Enter a base for your beautiful number: '))
    #c = chaos_turtle(3, 0, 0)