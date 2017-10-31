
import os

print('-' * 10 + "A.1. List comprehensions basics" + '-' * 10)

# The list comprehension isn't exactly the same as the for loop
# tatement version because it makes a new list object (which might matter if there are
# ultiple references to the original list), but it's close enough for most applications

# To run the expression, Python executes an iteration across L inside the interpreter,
# assigning x to each item in turn, and collects the results of running the items through
# the expression on the left side.

L = [1, 2, 3]
L = [x + 10 for x in L]

# Depending on your Python and code, list comprehensions
# might run much faster than manual for loop statements (often roughly twice as fast)
# because their iterations are performed at C language speed inside the interpreter, rather
# than with manual Python code.

print('-' * 10 + "A.2. Using list comprehensions for files" + '-' * 10)

f = open('mytext.txt', 'w')
f.write('First line\n')
f.write('\n')             # Blank line 
f.write('Second line\n')
f.close()

f = open('mytext.txt', 'r')
lines = f.readlines()
print(lines)  # ['First line\n', '\n', 'Second line\n']

lines = [line.rstrip() for line in lines]
print(lines)  # ['First line', '', 'Second line']
f.close()

# We don't even need to open the file ahead of time.
# List comprehension will automatically use iteration protocol.
lines = [line.rstrip() for line in open('mytext.txt', 'r')]
print(lines)  # ['First line', '', 'Second line']

# We can do much more things
# These list comprehensions will also automatically close the file when their
# temporary file object is garbage-collected after the expression runs.
lines = [line.replace('line', 'spam') for line in open('mytext.txt', 'r')]
print(lines)   # ['First spam\n', '\n', 'Second spam\n']

print('-' * 10 + "A.3. List comprehensions if" + '-' * 10)

lines = [line.rstrip() for line in open('mytext.txt', 'r') if line[0] == 'S']
print(lines)  # ['Second line']

# Calculate number of all lines
print(len(open('mytext.txt', 'r').readlines()))  # 3

# Calculate number of NON-EMPTY lines
print(len([line for line in open('mytext.txt', 'r') if line.rstrip()]))  # 3


print('-' * 10 + "A.4. Nested for in list comprehensions" + '-' * 10)

l = [x + y for x in 'abc' for y in 'lmn']  
print(l)  # ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']

# It's equivalent to 2 for loops
rv = []
for x in 'abc':
    for y in 'lmn':
        rv.append(x+y)
print(rv)   # ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']

# List comprehensions can
# still be twice as fast as corresponding for loops on some tests, but just
# marginally quicker on others, and perhaps even slightly slower on some
# when if filter clauses are used

print('-' * 10 + "A.5. Other functions that work with iterators" + '-' * 10)

# Many of Python's other built-ins process iterables, too. For example, sorted sorts items
# in an iterable; zip combines items from iterables; enumerate pairs items in an iterable
# with relative positions; filter selects items for which a function is true; and reduce
# runs pairs of items in an iterable through a function. All of these accept iterables, and
# zip, enumerate, and filter also return an iterable in Python 3.X, like map. 

# sorted is a built-in that employs the iteration protocol-it's like the orig- inal list sort method, 
# but it returns the new sorted list as a result and runs on any iterable object.
print(sorted(open('mytext.txt')))  # ['\n', 'First line\n', 'Second line\n']

print(repr('&&'.join(open('mytext.txt'))))  # 'First line\n&&\n&&Second line\n'

# Membership test
print('Second line\n' in open('mytext.txt'))  # True

# extend() iterates automatically
L = [12]
L.extend(open('mytext.txt'))
print(L)           # [12, 'First line\n', '\n', 'Second line\n']

# append() doesn't iterate automatically
L = [11]
L.append(open('mytext.txt'))
print(L)           # [11, <open file 'mytext.txt', mode 'r' at 0xb73d2288>]
print(list(L[1]))  # ['First line\n', '\n', 'Second line\n']

print('-' * 10 + "A.6. Set and dictionary comprehensions" + '-' * 10)

s = {line for line in open('mytext.txt')}
print(s)  # set(['Second line\n', 'First line\n', '\n'])

d = {ix: line for ix, line in enumerate(open('mytext.txt'))}
print(d)  # {0: 'First line\n', 1: '\n', 2: 'Second line\n'}

print('-' * 10 + "A.8. Remove created here files" + '-' * 10)

os.remove('mytext.txt')
