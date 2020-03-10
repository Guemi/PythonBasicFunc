#!/usr/bin/env python
unsorted_list = [7,6.7,8.9,6.4,3,9,2,6,1,0,5.8,7,6.4]
sorted_list = [3,6,8,9,26]
#listM = [[(val*y+y) for val in range (4)] for y in range(3)]
listMa = [val for val in range (6)]
print(*listMa,sep='\n')
listM = [x*x for x in listMa if x%2 == 0 ]
print((sorted(set(listM)))[2])
print(str(listM))
print(set(unsorted_list))
print(listM)
pv, *sv = input().split()
print(pv,'\n',sv)
"""
# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

# Nested List comprehension with an if condition
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]

print(flatten_planets)

# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]

print(flatten_matrix)

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]

print(matrix)
* collects all the positional arguments in a tuple.

** collects all the keyword arguments in a dictionary.

>>> def functionA(*a, **kw):
       print(a)
       print(kw)


>>> functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
(1, 2, 3, 4, 5, 6)
{'a': 2, 'c': 5, 'b': 3}

In a function call:

* unpacks a list or tuple into position arguments.

** unpacks a dictionary into keyword arguments.
"""
