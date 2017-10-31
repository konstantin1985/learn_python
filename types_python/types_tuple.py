# Tuples construct simple groups of objects. 
# They work exactly like lists, except that tuples can't be changed in
# place (they're immutable) and are usually written as a series of items in parentheses,
# not square brackets. 
print((1, 2) + (3, 4))     # (1, 2, 3, 4)

# If you really want a single-item tuple, simply add a trailing comma
# after the single item, before the closing parenthesis
x = (40)
print(x)                   # 40, an integer
y = (40,)
print(y)                   # (40,) a tuple

# To sort you need to use sorted() function
T = ('cc', 'aa', 'dd', 'bb')
print(sorted(T))           # ['aa', 'bb', 'cc', 'dd']

# List comprehensions are really sequence operations-they always build new lists, but
# they may be used to iterate over any sequence objects, including tuples, strings, and
# other lists.
T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)                   # [21, 22, 23, 24, 25]

# Also, note that the rule about tuple immutability applies only to the top level of the
# tuple itself, not to its contents. A list inside a tuple, for instance, can be changed as usual
T = (1, [2, 3], 4)
# T[1] = 'spam'            # error
T[1][0] = 'spam'
print(T)                   # (1, ['spam', 3], 4)

# Tuples and other immutables, therefore, serve a similar role to "constant" declarations 
# in other languages, though the notion of constantness is associated with objects 
# in Python, not variables
# Tuples can also be used in places that lists cannot-for example, as dictionary key

# NAMEDTUPLE utility add logic to tuples that allows components to be 
# accessed by both position and attribute name
from collections import namedtuple
Rec = namedtuple('Rec123', ['name', 'age', 'jobs'])
bob = Rec('Bob', age = 40.5, jobs = ['dev', 'mgr'])
print(bob)                 # Rec123(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob[0])              # Bob
print(bob.name)            # Bob

# Converting to a dictionary supports key-based behavior when needed
D = bob._asdict()
print(D['name'])           # Bob

# Need to learn further about generators
# https://stackoverflow.com/questions/20736917/concatenate-elements-of-a-tuple-in-a-list-in-python

print('-' * 10 + 'Exercises' + '-' * 10)
# 1. Tuple assignment. Type the following lines:
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)                # ('eggs', 'spam')

