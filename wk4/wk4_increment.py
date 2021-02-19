#!/usr/bin/python

#It returns True if all the characters in the String are in ascending order
#If returns False if at least one pair of characters are in descending order

import sys

def LongerThan(inarg):
    iterator = int()

    for iterator in range(len(inarg) - 1):
        if inarg[iterator] < inarg[iterator + 1]:
            continue
        else:
            return False
    return True
        
#unit tests:
print(LongerThan('asdf'))
print(LongerThan('qwer'))
print(LongerThan('zxcv'))
print(LongerThan('1234'))

#keyboard input:
#newvar = input('do this: ')
#print(LongerThan(newvar))

#command line:
#try:
#    print(LongerThan(sys.argv[1]))
#except IndexError:
#    print('you must have on parameter')
