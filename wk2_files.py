#!/usr/bin/python

def readfile(filename_param):
    f = open(filename_param, 'r')
    #the below will return a list
    return f.readlines()




def processdata(process_param):
    # process the list, ignore blank lines
    newstring = str()
    for line in process_param:
        newstring += line[::-1]
    return newstring 



input_data = readfile('wk2_hilbilleeey_ipsum.txt')
output_data = processdata(input_data)
print(output_data)

























### Exercise #0 revision
def warm_up():
    inpval = input()
    # try catch to remove error if no ' '
    print(inpval.index(' '))
    print(inpval.lstrip())

