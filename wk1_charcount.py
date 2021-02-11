#!/usr/bin/python
#first exercise
#print([5, 6, 7].sort(reverse=True)[0])

# Declare 4 Variables
spacetotal = 0
charactertotal = 0 
numbertotal = 0
voweltotal = 0
totalchars = 0
inputstring = input()

# loop through the string and incrment
for character in inputstring:
    # if we see a space
    if character == ' ': 
        spacetotal += 1
    elif character in  '1234567890': 
        numbertotal += 1
    elif character in 'aeiouAEIOU': 
        voweltotal += 1
    else:
        charactertotal += 1 
    totalchars += 1

# Report on the three incremented vars
print('sp: ' + str(spacetotal))
print('ch: ' + str(charactertotal))
print('nu: ' + str(numbertotal))
print('vo: ' + str(voweltotal))
print('to: ' + str(totalchars))

