#!/usr/bin/python

import sys         # this is a library of features that extend Python 

#print(sys.argv)    # this prints the entire list of CLI options including the .py file

single_dash_count = 0
double_dash_count = 0
equals_count = 0
total_count = 0

for single_arg in sys.argv:
    total_count += 1
    if single_arg[0:2] == '-h':
        print("this is help")
        break
    if single_arg[0:2] == '--':
        double_dash_count += 1
    elif single_arg[0:1] == '-':
        single_dash_count += 1
    if '=' in single_arg:
        equals_count += 1

print('total params: ' + str(total_count)) 
print('with \'-\'    : ' + str(single_dash_count)) 
print('with \'--\'   : ' + str(double_dash_count)) 
print('with \'=\'    : ' + str(equals_count)) 

############################### TASK #############################################
#
# 0. print 'this is help' when the user passes a -h via the CLI
# 1. Count the number of parameters tendered, is the script filename a parameter?
# 2. identify the paramters with an '=' sign make a separate count for them
# 3. Identify switch parameters by the '-' prefix make a separate count for them 
# 4. Identify longform switch parameters by the '--' prefix make a separate count for them 
# now test
#
# TEST EXAMPLE:
# ./wk3_cli_parameters.py -a --b -c=5
# total params: 4
# with '-'    : 2
# with '--'   : 1
# with '='    : 1
