#!/usr/bin/python
import sys
import operator
import re

while True:
    number_pattern = re.compile("^-?[0-9]+$")

    first_input = str(input('Enter a number (or a letter to exit): '))
    if number_pattern.match(first_input):
        first_number = int(first_input)
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

    result = round(operation(first_number, second_number))
    print('Result:', result, '\n')