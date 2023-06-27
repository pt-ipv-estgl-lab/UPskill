#!/usr/bin/env python3 

"""
modulo.py - an example of a Python module

function suml - compute and return the sum of all elements of the_list
function prodl - compute and return the product of all elements of the_list
counts the number of times each function is called on __counter

"""

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
    print(__counter)
