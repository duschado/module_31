#!/usr/bin/python3
number = input('Enter a number\n > ')
number_int = int(number)
if number_int % 2 == 0:
	print('The number {} is even.'.format(number))
else:
	print('The number {} is odd.'.format(number)) 