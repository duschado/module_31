#!/usr/bin/python3
name = input('What\'s your name?\n > ')
age = input('How old are you?\n > ')
age_int = int(age)
year_int = 100 - age_int + 2018
year = str(year_int)
print('{}!'.format(name) + ' ' + 'You will be 100 years old in ' + year + '!')