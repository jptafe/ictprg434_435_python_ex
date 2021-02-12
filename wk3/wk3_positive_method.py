#!/usr/bin/python

class SundaryMethods:

    def isPositive(self, a_number):
        if a_number > 0: 
            return True
        else:
            return False

    def startString(self, sentance, sentancestart):
        return sentance[:sentancestart]

    def reverseString(self, instring):
        return instring[::-1]


sundaryObject = SundaryMethods()

truthy = sundaryObject.isPositive(-5)
print(truthy)
