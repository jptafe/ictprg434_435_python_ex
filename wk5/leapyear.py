#!/usr/bin/python
# What is a leap year? To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not. 2020, 2024 and 2028 
# Write a function that returns True if the integer given is a leap year

def IsLeap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    return False

try:
    assert IsLeap(2019) == False 
    assert IsLeap(2020) == True 
    assert IsLeap(2016) == True 
    assert IsLeap(2023) == False 
    assert IsLeap(2021) == False 
    assert IsLeap(1964) == True
    assert IsLeap(1900) == False
    assert IsLeap(1800) == False
    assert IsLeap(1700) == False
    assert IsLeap(1600) == True 
    assert IsLeap(1904) == True 
except AssertionError:
    print('err')






