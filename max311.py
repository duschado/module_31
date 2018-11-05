#!/usr/bin/python3
import random
N = random.sample(range(1, 100), 1)
n = N[0]
number = input("Enter a number from 1 to 100\n > ")
number_int = int(number)
while number_int != n:	
	if number_int < n:
		number = input("Please enter a larger number\n > ")
	elif number_int > n:
		number = input("Please enter a smaller number\n > ")			
	number_int = int(number)
print("""Congratulations! 
You guessed the number. 
It's """ + number + "!")

