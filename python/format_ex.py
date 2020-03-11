#!/usr/bin/env python
func_name = "Swap"
a, b = 5, 10
def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b

print("Function {0} with values a = {1} and b = {2} returns {3}".format(func_name,a,b,swap(a, b)))
print('{:d}'.format(42))
print("42")