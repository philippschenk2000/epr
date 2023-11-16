import epr_functions
__author__ = "7093700, Schenk"


print('You have the following 3 functions to choose from:')
options = {'1': 'Calculate a decimal number to the octal version of it',
           '2': 'Calculate a decimal number to a choosen base by you of it',
           '3': 'Lets run a beautiful turtle from your starting point the half way to three random points and see the route'}
for o in options:
    print('Option', o, ':', options[str(o)])

option = input('Enter you favorite option: ')
print('You choosed: ', options[str(option)])

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