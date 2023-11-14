__author__ = "7093700, Schenk"

def function_a(a, b):
    # TRY EXCEPT FOR NON INTEGER NUMBERS
    try:
        sum1 = []
        # PREPARE FOR THE FOR-LOOP BY GOING FROM LOWER TO HIGHER NUMBER
        lower_one = min(int(a), int(b))
        higher_one = max(int(a), int(b))
        # RANGE SHOULD INCLUDE THE LAST NUMBER TOO
        for i in range(lower_one, higher_one + 1):
            sum1.append(i)
        return sum(sum1)
    except:
        print('Both inputs have to be a number.')


def function_b(a):
    # SET STEPS TO 0 BECAUSE NO STEP WAS DONE TIL THIS POINT
    steps = 0
    while a != 0:
        a = a / 2
        # ADD UP +1 FOR EVERY STEP
        steps = steps + 1
    return steps


def function_c(n, m):

    # PUT 0 IN A LIST IN CASE THE length IS 0
    listed = [0]
    # CREATE ONE ALTERNATING LIST WITH ONEs and ZEROs
    for l in range(n):
        if listed[-1] == 0:
            listed.append(1)
        else:
            listed.append(0)
    # CREATE A SECOND ALTERNATING LIST BUT WITH THE OTHER NUMBER AT THE BEGINNING
    listed2 = listed[1:]
    # KICK OUT THE LAST ELEMENT OF THE FIRST LIST
    listed = listed[:-1]
    # PRINT BOTH LISTS ALSO ALTERNATING IN THE CONSOLE, WITHOUT COMMAS AND BRACKETS
    for k in range(m):
        if k % 2 == 0:
            print(str(listed).replace('[', '').replace(']', '').replace(',', ''))
        else:
            print(str(listed2).replace('[', '').replace(']', '').replace(',', ''))


def catalan_constant_d_e(a, b, steps):
    # CREATE AN EMPTY LIST
    listed = []
    # FOR EVERY VALUE (INPUT: 4, 10, 3)
    for r in range(a, b, steps):
        # CREATE A NEW EMPTY LIST FOR EVERY r
        listed2 = []
        # CALCULATE CATALAN FORMULA AND ADD THEM INTO THE LIST FOR r
        for n in range(r):
            nominator = (-1)**n
            denominator = (2*n + 1)**2
            listed2.append(nominator / denominator)
        # AS THE LIST GOT FILLED FOR r, THE CATALAN RESULT FOR EVERY r IS THE SUM OF ALL LIST ELEMENTS
        print('n =', r, ' Catalan constant is: ', sum(listed2))
        listed.append(sum(listed2))
        # TO GET THE DIFFERENCE BETWEEN r AND r-1, THE LENGTH OF THE LIST NEEDS TO BE OVER ONE
        # THEN THE DIFFERENCE CAN EASILY BE CALCULATED BETWEEN THE NEIGHBOURING LIST ELEMENTS
        if len(listed) > 1:
            print('Difference is: ', ((listed[-1] - listed[-2])))    # abs()?


f_a = function_a(input('First number: '), input('Second number: '))
print(f_a)
# TEST 1:
# IN: -12.0, 20       SHOULD BE: Both inputs have to be a number.     OUT: Both inputs have to be a number.
# TEST 2:
# IN: -12, 20       SHOULD BE: 132     OUT: 132
# TEST 3:
# IN: 2, 489      SHOULD BE: 119804     OUT: 119804

f_b = function_b(389270.578)
print(f_b)
# TEST 1:
# IN: 12      SHOULD BE: 1079     OUT: 1079
# TEST 2:
# IN: 2      SHOULD BE: 1076     OUT: 1076
# TEST 3:
# IN: 389270.578      SHOULD BE: 1094     OUT: 1094

f_c = function_c(4, 6)
# TEST 1:
# IN: 0, 0      SHOULD BE: (nothing)     OUT: (nothing)

# TEST 2:
# IN: 4, 1
# SHOULD BE:
# 0 1 0 1
# OUT:
# 0 1 0 1

# TEST 3:
# IN: 4, 6
# SHOULD BE:
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# OUT:
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

f_d_e = catalan_constant_d_e(4, 10, 3)
# TEST 1:
# IN: 4, 10, 3
# SHOULD BE:
# n = 4  Catalan constant is:  0.9084807256235827
# n = 7  Catalan constant is:  0.9184791015893248
# Difference is:  0.009998375965742046
# OUT:
# n = 4  Catalan constant is:  0.9084807256235827
# n = 7  Catalan constant is:  0.9184791015893248
# Difference is:  0.009998375965742046

# TEST 2:
# IN: 4, 23, 2
# SHOULD BE:
# n = 4  Catalan constant is:  0.9084807256235827
# n = 6  Catalan constant is:  0.9125619418260111
# Difference is:  0.004081216202428406
# n = 8  Catalan constant is:  0.9140346571448803
# Difference is:  0.0014727153188691666
# n = 10  Catalan constant is:  0.914724781654844
# Difference is:  0.0006901245099637521
# n = 12  Catalan constant is:  0.9151019961827472
# Difference is:  0.0003772145279031802
# n = 14  Catalan constant is:  0.9153302540702645
# Difference is:  0.00022825788751723586
# n = 16  Catalan constant is:  0.9154787319860305
# Difference is:  0.00014847791576599878
# n = 18  Catalan constant is:  0.9155806791009646
# Difference is:  0.00010194711493416442
# n = 20  Catalan constant is:  0.9156536770949605
# Difference is:  7.299799399584916e-05
# n = 22  Catalan constant is:  0.9157077282099416
# Difference is:  5.405111498113513e-05
# OUT:
# n = 4  Catalan constant is:  0.9084807256235827
# n = 6  Catalan constant is:  0.9125619418260111
# Difference is:  0.004081216202428406
# n = 8  Catalan constant is:  0.9140346571448803
# Difference is:  0.0014727153188691666
# n = 10  Catalan constant is:  0.914724781654844
# Difference is:  0.0006901245099637521
# n = 12  Catalan constant is:  0.9151019961827472
# Difference is:  0.0003772145279031802
# n = 14  Catalan constant is:  0.9153302540702645
# Difference is:  0.00022825788751723586
# n = 16  Catalan constant is:  0.9154787319860305
# Difference is:  0.00014847791576599878
# n = 18  Catalan constant is:  0.9155806791009646
# Difference is:  0.00010194711493416442
# n = 20  Catalan constant is:  0.9156536770949605
# Difference is:  7.299799399584916e-05
# n = 22  Catalan constant is:  0.9157077282099416
# Difference is:  5.405111498113513e-05

# TEST 3:
# IN: 4, 5, 1
# SHOULD BE: n = 4  Catalan constant is:  0.9084807256235827
# OUT: n = 4  Catalan constant is:  0.9084807256235827

