#!/usr/bin/python

# TAKE only 1 parameter from the CLI
# calculate and print the CLI parameter + 5

# NOTE: Attempt this WITHOUT an if statement
#       use try: except: block instead

import sys

try:
    newnum = int(sys.argv[1]) + 4
    if(newnum = 999):
        raise Exception('blah')
except ValueError:
    print('err')
    sys.exit(1)
except IndexError:
    newnum = 99
print(newnum)
sys.exit(0)







































import sys

try:
    newvar = int(sys.argv[1]) + 4
except:
    print('err: arg error')
    sys.exit(1)

print(newvar)
sys.exit(0)




























def GetInput():
    return input('give me a number: ')

def EvalAsNum(anum = 'a'):
    if anum.isdigit():
        return True
    else:
        return False

numb = str('abca')

#while EvalAsNum(numb) == False:
#    numb = GetInput()

try:
    if int(numb) > 5:
        print('larger than 5')
    else:
        print('smaller or equal to 5')
except ValueError:
    print('I give up!!!') 
