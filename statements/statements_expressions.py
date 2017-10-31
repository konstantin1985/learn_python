
import sys
import os

# from __future__ import print_function  # to use Python3 print() in Python2


print('-' * 10 + "A.1. In-place changes" + '-' * 10)

# This doesn't quite work, though. Calling an in-place change operation such as append,
# sort, or reverse on a list always changes the list in place, but these methods do not
# return the list they have changed; instead, they return the None object.
L = [1, 2]
L = L.append(3)
print(L)  # None

# Expressions vs statements
# https://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python
# The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements.
# An expression is a combination of values, variables, operators, and calls to functions. 
# Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.

# Assignment statement
w = 5

# Expressions can be used as statements in Python 
w + 5

print('-' * 10 + "A.2. Printing" + '-' * 10)
# print() in Python 3 has some arguments
# print([object, ...][, sep=' '][, end='\n'][, file=sys.stdout][, flush=False])
w = 'spam'
x = 99
y = ['eggs']


# print(w, x, y, sep = ', ')  # only in Python 3

# print x, y,; print x, y  # 99 ['eggs'] 99 ['eggs']

# Printing the hard way (exactly what print() does)
sys.stdout.write('hello world\n')  # hello world

# We can reassign sys.stdout to something different
sys.stdout = open('log.txt', 'a')
print(x,y)
print(x,y)
# Return the original value to sys.stdout https://docs.python.org/2/library/sys.html#sys.__stdin__
sys.stdout = sys.__stdout__ 
os.remove('log.txt')

# We can redirect print to the object if it has write() - LATER

# We can print to the file without reassigning sys.stdout
if sys.version_info[0] < 3:
    log = open('log_next.txt', 'a')
    print >> log, x, y  # print to the file
    print(w)            # print to the original std
    log.close()
    os.remove('log_next.txt')

# Writing to error stream stderr
sys.stderr.write(("Bad!" * 4) + '\n')  # Bad!Bad!Bad!Bad! in red

# Doing the same using print
if sys.version_info[0] < 3:
    print >> sys.stderr, ("Bad!" * 4)  # Bad!Bad!Bad!Bad! in red
else:
    # print("Bad!" * 4, file = sys.stderr) # Only in python3
    pass

# For truly no difference in print() between Python2 and Python3 use ONE object in print (format and % could help)

# Work differently    
print('spam')                 # Same in P2 and P3
print('spam', 'ham', 'eggs')  # ('spam', 'ham', 'eggs') - like tuple in P2, spam ham eggs - in P3
 
# Work the same in P2 and P3
print('%s %s %s' % ('spam', 'ham', 'eggs'))
print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))


