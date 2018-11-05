#!/usr/bin/python3
import random
n = input('Enter the number of items in the list\n > ')
n = int(n)
N = random.sample(range(1, 101), n)
print(N)
for i in range(n-1):
	sw = 0
	for j in range(n-1):
		if N[j] > N[j+1]: 
			temp = N[j]
			N[j] = N[j+1]
			N[j+1] = temp
			sw = 1					
	if sw == 0:		
		break
print(N)
		


