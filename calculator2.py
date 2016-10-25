#!/usr/bin/python

'''
This script makes calculations while user provides the following inputs:
    1. integer number
    2. one of these operations: '+', '-', '*', '/'
    3. integer number. 
Exit if user gives any other input than the expected ones.
'''

import sys
import operator
import re

while True:
    number_pattern = re.compile("^-?[0-9]+$")

    first_input = input('Enter a number (or a letter to exit): ')
    if first_input.isdigit():
        first_input = int(first_input)
    else: 
        break
        
    op_dictionary = {"+": operator.add, 
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv}
    op_sign = input('Enter an operation: ')
    if op_sign in op_dictionary:
        operation = op_dictionary[op_sign]
    else:
        break

    second_input = str(input('Enter another number: '))
    if number_pattern.match(second_input):
        second_number = int(second_input)
    else:
        break

    result = operation(first_input, second_number)
    print('Result:', result, '\n')