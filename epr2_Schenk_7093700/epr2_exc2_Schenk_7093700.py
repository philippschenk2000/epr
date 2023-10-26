def main():
    __author__ = "7093700, Schenk"
    try:
        # INPUT OF NUMBERS
        a = int(input('Enter first number (range 0 - 110) for GPR: '))
        b = int(input('Enter second number (range 0 - 110) for EPR: '))
        c = int(input('Enter third number for ZBNP: '))
        if 0 <= a <= 110 and 0 <= b <= 110:
            print(0)
        else:
            print('First number and second number have to be between 0 and 110')
    except:
        print('Input has to be a integer.')


def calc_harmonic_mid(a, b):
    return 2*a*b/(a+b)


def returning(harmonic_mid, arithmetic_mid):
    print(f'The harmonic mean is: {harmonic_mid}')
    print(f'The arithmetic mean is: {arithmetic_mid}')


main()