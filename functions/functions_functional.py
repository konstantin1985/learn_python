
# Good articles on Python functional progreamming
# - https://docs.python.org/3/howto/functional.html




# Python's functional programming arsenal:
# - map
# - filter
# - reduce
# - first-class object
# - nested scope closure
# - lambda
# - generators
# - comprehensions
# - decorators


print('-' * 10 + "A.1. Mapping Functions over Iterables: map" + '-' * 10)

# Updating all the counters in a list can be done with a for loop

counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)
print(updated)  # [11, 12, 13, 14]

# map applies a passed-in function to each item in an iterable object
# and return a list containing all the function call results

# Remember that map is an iterable in Python 3.X, so a list call is used
# to force it to produce all its results for display here;
# this isn't necessary in 2.X

def inc(x): return x + 10
updated = list(map(inc, counters))
print(updated)  # [11, 12, 13, 14]

# Because map expects a function to be passed in and applied, it also happens 
# to be one of the places where lambda commonly appears.

updated = list(map(lambda x: x + 3, counters))
print(updated)  # [4, 5, 6, 7]

# map is faster than a manually coded for loop in some usage modes

# given multiple sequence arguments, it sends items
# taken from sequences in parallel as distinct arguments to the function

rv = list(map(pow, [1, 2, 3], [2, 3, 4]))  # 1**2, 2**3, 3**4
print(rv)  # [1, 8, 81]

# The map call is similar to the list comprehension expressions
rv = list(map(inc, [1, 2, 3, 4]))
print rv  # [11, 12, 13, 14]
rv = [inc(x) for x in [1, 2, 3, 4]]
print rv  # [11, 12, 13, 14]

# In some cases, map may be faster to run than a list comprehension (e.g., 
# when mapping a built-in function), and it may also require less coding.

print('-' * 10 + "A.2. Selecting items in Iterables: filter" + '-' * 10)

# Because it also returns an iterable, filter (like range) requires 
# a list call to display all its results in 3.X.
rv = list(range(-5, 5))  
print(rv)                # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

rv = list(filter(lambda x: x > 0, range(-5, 5)))
print rv                 # [1, 2, 3, 4]

rv = list(filter(lambda x: True, range(-5, 5)))
print rv                 # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# Also like map, filter can be emulated by list comprehension syntax 
# with often-simpler results
print([x for x in range(-5, 5) if x > 0])  # [1, 2, 3, 4]

print('-' * 10 + "A.3. Combining items in Iterables: reduce" + '-' * 10)

from functools import reduce  # was moved here in Python 3.X (only required in Python 3.X)

# At each step, reduce passes the current sum or product, along with the next item from
# the list, to the passed-in lambda function. By default, the first item in the sequence
# initializes the starting value.

rv = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(rv)  # 10, 1+2=3, 3+3=6, 6+4=10

rv = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(rv)  # 24, 1*2=2, 2*3=6, 6*4=24

# Coding your own version of reduce is actually fairly straightforward. 

def myreduce(function, sequence):
    total = sequence[0]
    for nexts in sequence[1:]:
        total = function(total, nexts)
    return total

rv = myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
print(rv)  # 15

rv = myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print(rv)  # 120

# It's possible to use functions from the operator package

import operator
rv = reduce(operator.add, [1, 2, 3, 4])
print rv  # 10 
# rv = list(reduce(operator.add, [1, 2, 3, 4]))  # TypeError: 'int' object is not iterable

print('-' * 10 + "A.4. Comparison to list comprehensions" + '-' * 10)

# For complicated expressions list comprehensions produce
# much easier code
rv = [x ** 2 for x in range(10) if x % 2 == 0]
print(rv)  # [0, 4, 16, 36, 64]

rv = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
print(rv)  # [0, 4, 16, 36, 64]

 
