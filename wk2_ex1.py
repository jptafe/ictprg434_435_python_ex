#!/usr/bin/python

line_of_string = input()
print(line_of_string)
new_string = line_of_string.lstrip()
print(new_string)

try:
    print(new_string.index('foo'))
except ValueError:
    print('error string not found')
