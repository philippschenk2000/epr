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
    # SET STEPS TO 0 IN CASE a IS 0
    steps = 0
    while a != 0:
        a = a / 2
        # ADD UP +1 FOR EVERY STEP
        steps = steps + 1
    return steps


def function_c(length):

    # PUT 0 IN A LIST IN CASE THE length IS 0
    listed = [0]
    # CREATE ONE ALTERNATING LIST WITH ONEs and ZEROs
    for l in range(length):
        if listed[-1] == 0:
            listed.append(1)
        else:
            listed.append(0)
    # CREATE A SECOND ALTERNATING LIST BUT WITH THE OTHER NUMBER AT THE BEGINNING
    listed2 = listed[1:]
    # KICK OUT THE LAST ELEMENT OF THE FIRST LIST
    listed = listed[:-1]
    # PRINT BOTH LISTS ALSO ALTERNATING IN THE CONSOLE, WITHOUT COMMAS AND BRACKETS
    for k in range(len(listed)):
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
        # TO GET THE DIFFERENCE BETWEEN r AND r-1 A THE LENGTH OF THE LIST NEEDS TO BE OVER ONE
        # THEN THE DIFFERENCE CAN BE EASILY CALCULATED BETWEEN THE NEIGHBOURING LIST ELEMENTS
        if len(listed) > 1:
            print('Difference is: ', ((listed[-1] - listed[-2])))    # abs()?


f_a = function_a(input('First number: '), input('Second number: '))
# TEST 1:
# IN:  SHOULD BE:   OUT:
# TEST 2:
# IN:  SHOULD BE:   OUT:
# TEST 3:
# IN:  SHOULD BE:   OUT:

f_b = function_b(12)

# TEST 1:
# IN:  SHOULD BE:   OUT:
# TEST 2:
# IN:  SHOULD BE:   OUT:
# TEST 3:
# IN:  SHOULD BE:   OUT:

f_c = function_c(1)
# TEST 1:
# IN:  SHOULD BE:   OUT:
# TEST 2:
# IN:  SHOULD BE:   OUT:
# TEST 3:
# IN:  SHOULD BE:   OUT:

f_d_e = catalan_constant_d_e(4, 10, 3)
# TEST 1:
# IN:  SHOULD BE:   OUT:
# TEST 2:
# IN:  SHOULD BE:   OUT:
# TEST 3:
# IN:  SHOULD BE:   OUT:

