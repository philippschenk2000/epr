""" This script calls 1 of the 3 different functions for the new exercise"""
import epr_functions
__author__ = "7093700, Schenk"


# exercise 2
# PRINT OUT THE DIFFERENT OPTIONS FOR THE USER
print('You have the following 3 functions to choose from:')
options = {'1': 'Calculate a decimal number to the octal version of it',
           '2': 'Calculate a decimal number to a choosen base by you of it',
           '3': 'Lets run a beautiful turtle from your starting point the half way to three random points and see the route'}
for o in options:
    print('Option', o, ':', options[str(o)])

# USER HAS TO CHOOSE ONE OF THE CORRECT OPTIONS
option = input('Enter you favorite option: ')
print('You choosed: ', options[str(option)])

# CALL THE FUNCTIONS FROM THE OTHER .py SCRIPT
if option == '1':
    result = epr_functions.decimal_to_octal(int(input('Enter your decimal number you want to transform into octal: ')))
    print('The result would be:', result)
elif option == '2':
    result = epr_functions.decimal_to_basis(int(input('Enter your decimal number you want to transform: ')), int(input('Enter the base you want to transform your decimal number with: ')))
    print('The result would be:', result)
elif option == '3':
    result = epr_functions.chaos_turtle2(int(input('Enter the iterations/steps the turtle should do: ')), int(input('Enter start-X-coordinate: ')), int(input('Enter start-Y-coordinate: ')))
else:
    print('This option is not allowed!')


# OPTION 1:
# TEST 1:
# IN: 20 SHOULD: The result would be: 24
# OUT:
# The result would be: 24
# OPTION 2:
# IN: 42 SHOULD: The result would be: 1K
# OUT: The result would be: 1K
# OPTION 3:
# IN: 100, 0, 0 SHOULD: be a graphics with a running turtle
# OUT: a graphics with a running turtle
# P1: (70, 100)
# P2: (150, 140)
# P3: (40, 300)
# ------------------------------------
# 1: From (0, 0) --> Walk to point P: (150, 140)
# 1: Stop at (75.0, 70.0)
# 2: From (75.0, 70.0) --> Walk to point P: (40, 300)
