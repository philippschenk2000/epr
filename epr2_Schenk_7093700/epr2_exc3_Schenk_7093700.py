def main():
    __author__ = "7093700, Schenk"
    try:
        # INPUT OF NUMBERS
        print('The program will calculate the rest after dividing the minimum of both by 2, 4 & 8.')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        # CALC MINIMUM
        minimum = min(a, b)
        for elem in [2, 4, 8]:
            rest = minimum % elem
            if rest == 0:   # kein eva prinzip! zwischenzeitliche ausgabe
                print(f'The minimum of both numbers ({minimum}) is dividable by {elem} with no rest')
            else:
                print(f'The minimum of both numbers ({minimum}) is NOT dividable by {elem} with a rest of {rest}')
    except:
        print('All input has to be non-decimal number.')


main()