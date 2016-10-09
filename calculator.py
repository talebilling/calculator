#!/usr/bin/python
import sys
import operator
import re

while (True):
    pattern = re.compile("[0-9]+")

    first_input = str(input('Enter a number (or a letter to exit): '))
    if pattern.match(first_input):
        first_number = int(first_input)

        ops = {"+": operator.add, "-": operator.sub,"*": operator.mul,"/": operator.truediv}
        sign = input('Enter an operation: ')
        if sign in ops:
            op_func = ops[sign]
        else:
            break

        second_input = str(input('Enter another number: '))
        if pattern.match(second_input):
            second_number = int(second_input)
        else:
            break

        result = round(op_func(first_number, second_number))
        print('Result:', result)
    else: 
        break