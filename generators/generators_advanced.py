
import os

# Do this exercise
# https://stackoverflow.com/questions/47217475/print-1-to-n-digits-count

print("-" * 20 + "#1 Generator Functions and Generator Expressions" + "-" * 20)

# Generator functions (available since 2.3) are coded as normal def statements, but
# use yield statements to return results one at a time, suspending and resuming their
# state between each.

# Generator expressions (available since 2.4) are similar to the list comprehensions
# of the prior section, but they return an object that produces results on demand
# instead of building a result list.

# Because neither constructs a result list all at once, they save memory space and allow
# computation time to be split across result requests. 


print("-" * 20 + "#2 Generator functions vs generator expressions" + "-" * 20)

# Generator functions
# A function def statement that contains a yield statement is turned into a generator
# function. When called, it returns a new generator object with automatic retention
# of local scope and code position; an automatically created __iter__ method that
# simply returns itself; and an automatically created __next__ method (next in 2.X)
# that starts the function or resumes it where it last left off, and raises 
# StopIteration when finished producing results.

# Generator expressions
# A comprehension expression enclosed in parentheses is known as a generator 
# expression. When run, it returns a new generator object with the same automatically
# created method interface and state retention as a generator function call's results
# with an __iter__ method that simply returns itself; and a __next__ method
# (next in 2.X) that starts the implied loop or resumes it where it last left off, and
# raises StopIteration when finished producing results.

# The net effect is to produce results on demand in iteration contexts that employ these
# interfaces automatically.

# Same iteration can often be coded with either a generator function or a 
# generator expression

G = (c * 4 for c in "SPAM")
print(list(G))  # ['SSSS', 'PPPP', 'AAAA', 'MMMM']

def timesfour(S):
    for c in S:
        yield c * 4
G = timesfour("spam")
print(list(G))  # ['ssss', 'pppp', 'aaaa', 'mmmm']

# Both expression and function support both automatic and manual iteration

G = (c * 4 for c in "SPAM")
I = iter(G)     # NOP
print(next(I))  # SSSS
print(next(I))  # PPPP

# Generator is its own iterator, so no need to explicitly call iter()
G = (c * 4 for c in "SPAM")
print(next(G))  # SSSS
print(next(G))  # PPPP

G = timesfour('spam')
I = iter(G)
print(next(I))  # ssss
print(next(I))  # pppp


print("-" * 20 + "#3 Generators Are Single-Iteration Objects" + "-" * 20)

# A subtle but important point: both generator functions and generator expressions
# are their own iterators and thus support just one active iteration-unlike some 
# built-in types, you can't have multiple iterators of either positioned at 
# different locations in the set of results.

G = (c * 4 for c in "SPAM")  # Making a new generator

# If you iterate over the results stream manually with multiple iterators, 
# they will all point to the same position:

I1 = iter(G)
print next(I1)    # SSSS
print next(I1)    # PPPP
I2 = iter(G)
print next(I2)    # AAAA

# Once any iteration runs to completion, all are exhausted-we have to make
# a new generator to start again

print list(I1)    # ['MMMM']
# print next(I1)  # StopIteration

I3 = iter(G)
# print next(I3)  # StopIteration

I3 = iter(c * 4 for c in "SPAM")
print next(I3)    # SSSS

# The same holds true for generator function

def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('spam')
print(iter(G) is G)         # True
I1, I2 = iter(G), iter(G)
print(next(I1))             # ssss
print(next(I1))             # pppp
print(next(I2))             # aaaa

# This is different from the behavior of some built-in types, which support
# multiple iterators and passes and reflect their in-place changes in 
# active iterators

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print(next(I1))             # 1 
print(next(I1))             # 2
print(next(I2))             # 1
del L[2:]
# print(next(I1))           # StopIteration
print(next(I2))             # 2

# In general, objects that wish to support multiple scans will
# return supplemental class objects instead of themselves.

print("-" * 20 + "#4 Generation in Built-in Types, Tools, and Classes" + "-" * 20)

# Dictionaries are iterables with iterators that produce keys on each iteration

D = {'a':1, 'b':2, 'c':3}
x = iter(D)
#no order here
print next(x) #a
print next(x) #c
print next(x) #b

for key in D:
    print(key, D[key])

# ('a', 1)
# ('c', 3)
# ('b', 2)

# As we've also seen, for file iterators, Python simply loads lines from 
# the file ON DEMAND
# for line in open('temp.txt'):
#     print(line, end='')

# Many Python standard linrary tools generate values

# '.' - current directory
# '..' - directory above
for (root, subs, files) in os.walk('.'):  
    for name in files:
        print(root, name)

# By yielding results as it goes, the walker does not require its clients to wait for an entire
# tree to be scanned.

G = os.walk('.')
print(iter(G) is G)  # True
I = iter(G)          # Unnecessary step
print(next(I))       # ('.', [], ['generators_function.py', 'generators_advanced.py', 'generators_expression.py', '__init__.py'])

# Iteration contexts like for loops accept any iterable that has the expected methods,
# whether user-defined or built-in.
def f(a, b, c):
    print('%s, %s and %s' % (a, b, c))
    
f(0, 1, 2)                      # 0, 1 and 2
f(*range(3))                    # 0, 1 and 2 Unpack range values: iterable in 3.X
f(*(i for i in range(3)))       # 0, 1 and 2 Unpack generator expression values

# dict.values is also a list in 2.X

D = dict(a = 'Bob', b = 'dev', c = 40.5)
print D                           # {'b': 'dev', 'c': 40.5, 'a': 'Bob'} 
f(a = 'Bob', b = 'dev', c = 40.5) # Normal keywords: Bob, dev and 40.5

# IMPORTANT: to unpack like this **D, the keys in the dictionary
# have to be the same as arguments (a, b, c), otherwise an error
# TypeError: f() got an unexpected keyword argument 'cc'
# http://python-reference.readthedocs.io/en/latest/docs/operators/dict_unpack.html
f(**D)                            # Unpack dict key=value: Bob, dev and 40.5
f(*D)                             # Unpack keys iterator: a, c and b
f(*[1, 2, 3])                     # Unpack list: 1, 2 and 3

# dict.values is also a list in 2.X, but iterator in 3.X
# f(*D.values)                    # Works only in Python 3.X

# Technically speaking, sequence assignment actually supports any iterable object on the
# right, not just any sequence. This is a more general category that includes collections
# both physical (e.g., lists) and virtual (e.g., a file's lines), which was defined briefly in
# Chapter 4 and has popped up in passing ever since. We'll firm up this term when we
# explore iterables in Chapter 14 and Chapter 20.





