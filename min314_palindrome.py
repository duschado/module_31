#!/usr/bin/python3
word = input('Enter a word\n > ')
word_lower = word.lower()
length = len(word_lower)
middle = len(word_lower)//2
half_1 = list(word_lower[:middle])
half_2 = list(word_lower[-middle:])
half_2.reverse()
if half_1 == half_2:
	print('The word "{}" is a palindrome.'.format(word))
else:
	print('The word "{}" is not a palindrome.'.format(word))