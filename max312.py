#!/usr/bin/python3
N = input('Enter a number N, N > 1\n > ')
N = int(N)
if N <= 1:
	print('You entered an incorrect value')
else:
	fibonacci_lst = []
	fn_1 = 0
	fn_2 = 1
	fibonacci_lst.append(fn_1)
	

	while fn_2 <= N:
		fibonacci_lst.append(fn_2)
		fn_new = fn_1 + fn_2
		fn_1 = fn_2
		fn_2 = fn_new
print(fibonacci_lst)

