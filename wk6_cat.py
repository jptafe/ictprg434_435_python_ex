#!/usr/bin/python

#IMPORTS
import sys

#DECLARATIONS
fp = list()

#INPUT VALIDATION 
if sys.argv[1] == '--help':
    print('help: goes here')
    exit(0)
if len(sys.argv) < 3:
    print('err, not enough args. Arrrgggggg!')
    exit(1)

#ANALYSE INPUTS
for filecounter in range(len(sys.argv)):
    if filecounter == 0:
        continue
    if sys.argv[filecounter] == '-':
        fp.append(input('type something here: '))
        continue
    try:
        fp.append( open(sys.argv[filecounter], 'r') )
    except FileNotFoundError: 
        print('err, not file(s) not found, Arrrgggggg!')
        exit(1)

#CONCATENATE TO SCREEN 
for filepointer in fp:
    print(type(filepointer))
    if isinstance(filepointer, str):
        print(filepointer)
    else:
        try:
            print(filepointer.read())
        except UnicodeDecodeError:
            print('err, file is not a text file')
