 # pylint: disable=C0103
 # pylint: disable=C0304
 # pylint: disable=C0111

n1 = input('Enter a number: ')
n2 = input('Enter another number: ')

if n1 > n2:
    print('The first number is greater than the second.')
elif n1 == n2:
    print('The first number is equal to the second.')
else:
    print('The first number is less than the second.')