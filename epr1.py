def main():
    __author__ = "7093700, Schenk"
    # INPUT OF NUMBERS
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        # NOW CONDUCT TO EACH PART
        harmonic_mid = calc_harmonic_mid(a, b)
        arithmetic_mid = calc_arithmetic_mid(a, b)
        returning(harmonic_mid, arithmetic_mid)
    except:
        print('Input has to be a float or integer.')


def calc_harmonic_mid(a, b):
    return 2*a*b/(a+b)


def calc_arithmetic_mid(a, b):
    return (a+b)/2


def returning(harmonic_mid, arithmetic_mid):
    print(f'The harmonic mean is: {harmonic_mid}')
    print(f'The arithmetic mean is: {arithmetic_mid}')


main()