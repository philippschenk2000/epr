def function_a(a, b):
    try:
        sum1 = []
        lower_one = min(int(a), int(b))
        higher_one = max(int(a), int(b))
        for i in range(lower_one, higher_one + 1):
            sum1.append(i)
        return sum(sum1)
    except:
        print('Both inputs have to be a number.')


def function_b(a):
    steps = 0
    while a != 0:
        a = a / 2
        steps = steps + 1
    return steps


def function_c(length):
    listed = [0]
    for l in range(length):
        if listed[-1] == 0:
            listed.append(1)
        else:
            listed.append(0)
    listed2 = listed[1:]
    listed = listed[:-1]
    for k in range(len(listed)):
        if k % 2 == 0:
            print(str(listed).replace('[', '').replace(']', '').replace(',', ''))
        else:
            print(str(listed2).replace('[', '').replace(']', '').replace(',', ''))


def catalan_constant_d_e(a, b, steps):
    listed = []
    for r in range(a, b, steps):
        listed2 = []
        for n in range(r):
            nominator = (-1)**n
            denominator = (2*n + 1)**2
            listed2.append(nominator / denominator)
        print('n =', r, ' Catalan constant is: ', sum(listed2))
        listed.append(sum(listed2))
        if len(listed) > 1:
            print('Difference is: ', ((listed[-1] - listed[-2])))    # abs()?


#f_a = function_a(input('First number: '), input('Second number: '))
#f_b = function_b(preferred_number)
#f_c = function_c(preferred_length)
f_d_e = catalan_constant_d_e(4, 10, 3)

