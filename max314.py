#!/usr/bin/python3
import random
n = input('Enter the number of items in the list\n > ')
n = int(n)
N = random.sample(range(1, 101), n)
print(N)
for i in range(n):
	for j in range(i+1, n):
		item_min = N[i]
		if item_min > N[j]:
			item_min = N[j]
			N[j] = N[i]
			N[i] = item_min
print(N)