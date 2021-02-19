#!/usr/bin/python

class SundaryMethods:

    def isPositive(self, a_number):
        if a_number > 0: 
            return True
        else:
            return False

    def startString(self, sentance, sentancestart):
        return sentance[0:sentancestart]

    def reverseString(self, instring):
        return instring[::-1]


sundaryObject = SundaryMethods()

truthy = sundaryObject.isPositive(-5)
print(truthy)


class Assignment_part1:

    def ValidateArgs(args):
        return True

    def SimplifyString(inputstring):
        return True

    def ShiftString(inputString):  #### TASK 2
        return True



