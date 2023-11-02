def main():
    __author__ = "7093700, Schenk"
    try:
        # INPUT OF NUMBERS
        print('The program will calculate bonus points for the exam')
        gpr = float(input('Enter points for GPR (range 0 - 110): '))
        epr = float(input('Enter points for EPR (range 0 - 110): '))
        zbnp = float(input('Enter third number for ZBNP: '))
        # CHECK FOR RANGE
        if 0 <= gpr <= 110 and 0 <= epr <= 110:
            bonus_points = calc_bonus_points(gpr, epr, zbnp)
            returning(bonus_points)
        else:
            print('First number and second number have to be between 0 and 110')
    except:
        print('All input has to be a number.')


# BONUS POINTS CALCULATION
def calc_bonus_points(gpr, epr, zbnp):
    return round(min(zbnp / 4, (epr + gpr) / 14), 2)


# PRINT IN CONSOLE
def returning(bonus_points):
    print(f'The bonus points for the input would be {bonus_points} points')


main()