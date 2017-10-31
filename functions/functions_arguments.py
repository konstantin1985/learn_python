

# Arguments are passed into a function by assignment,
# which means by object reference (which really means by pointer).

# As arguments are simply assigned to passed-in objects, functions
# can change passed-in mutable objects in place, and the results may affect the caller.

# Immutable arguments are effectively passed "by value." Objects such as
# integers and strings are passed by object reference instead of by copying, but because
# you can't change immutable objects in place anyhow, the effect is much like making
# a copy.

# Mutable arguments are effectively passed "by pointer." Objects such as lists
# and dictionaries are also passed by object reference, which is similar to the way C
# passes arrays as pointers-mutable objects can be changed in place in the function,
# much like C arrays.




print('-' * 10 + "A.1. Arguments and shared references" + '-' * 10)

# Because a is a local variable name in the function's scope, the first assignment has
# no effect on the caller-it simply changes the local variable a to reference a 
# completely different object, and does not change the binding of the name X in the caller's
# scope. 

# Argument b is a local variable name, too, but it is passed a mutable object (the list
# that L references in the caller's scope). As the second assignment is an in-place
# object change, the result of the assignment to b[0] in the function impacts the value
# of L after the function returns.

# Really, the second assignment statement in changer doesn't change b-it changes part
# of the object that b currently references. 

# The name L hasn't changed either
# - it still references the same, changed object-but it seems as though L differs after the
# call because the value it references has been modified within the function.

def changer(a, b):
    a = 2          # Chnages local name's value only
    b[0] = 'spam'  # Changes shared object in place
    
X = 1
L = [1, 2]
changer(X, L)
print(X, L)  # (1, ['spam', 2]))

print('-' * 10 + "A.2. Avoiding mutable argument changes" + '-' * 10)

# Arguments are normally passed to functions by reference because that is what we 
# normally want. It means we can pass large objects around our programs without making
# multiple copies along the way, and we can easily update these objects as we go.

X = 1
L = [1, 2]
changer(X, L[:]) # pass a copy, so our L doesn't change
print(X, L)  # (1, [1, 2])

# We can also copy within the function itself
def changer2(a, b):
    b = b[:]
    a = 2
    b[0] = "spam"
    
X, L = 1, [1, 2]
changer2(X, L)
print(X, L)  # (1, [1, 2])

# Both of these copying schemes don't stop the function from changing the object-they
# just prevent those changes from impacting the caller. To really prevent changes, we can
# always convert to immutable objects to force the issue. Tuples, for example, raise an
# exception when changes are attempted

# This solution might impose more limitations on the function than it should, and so should generally
# be avoided (you never know when changing arguments might come in handy for other
# calls in the future). Using this technique will also make the function lose the ability to
# call any list-specific methods on the argument, including methods that do not change
# the object in place.

X, L = 1, [1, 2]
# changer(X, tuple(L))  # TypeError: 'tuple' object does not support item assignment

print('-' * 10 + "A.3. Output parameters and multiple results" + '-' * 10)

# return can send back any sort of object, it
# can return multiple values by packaging them in a tuple or other collection type.

# Although Python doesn't support what some languages label "call by reference" argument 
# passing, we can usually simulate it by returning tuples and assigning the results
# back to the original argument names in the caller

# It looks like the code is returning two values here, but it's really just one-a two-item
# tuple with the optional surrounding parentheses omitted.

def multiple(x, y):
    x = 2        # change local names only
    y = [3, 4]
    return x ,y  # return multiple new values in the tuple

X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X, L)      # (2, [3, 4])

# Correct way to unpack arguments in this case

def f(T):
    (a, (b, c)) = T
    print(a, b, c)
f((1, (2, 3)))  # (1, 2, 3)


print('-' * 10 + "A.4. Arguments matching: positional and keyword" + '-' * 10)

# As we've just seen, arguments are always passed by assignment in Python; names in the
# def header are assigned to passed-in objects.

# In a function call, arguments must appear in this order: any positional arguments
# (value); followed by a combination of any keyword arguments (name=value) and
# the *iterable form; followed by the **dict form.

# In a function header, arguments must appear in this order: any normal arguments
# (name); followed by any default arguments (name=value); followed by the *name (or
# * in 3.X) form; followed by any name or name=value keyword-only arguments (in
# 3.X); followed by the **name form.

# The steps that Python internally carries out to match arguments before
# assignment can roughly be described as follows:
# 1. Assign nonkeyword arguments by position.
# 2. Assign keyword arguments by matching names.
# 3. Assign extra nonkeyword arguments to *name tuple.
# 4. Assign extra keyword arguments to **name dictionary.
# 5. Assign default values to unassigned arguments in header.

# Pass by position
def f100(a, b, c):
    print(a, b, c)
f100(1, 2, 3)  # (1, 2, 3)

# Keyword arguments allow us to match by name
f100(c=3, b=2, a=1)  # (1, 2, 3)

# All positional are matched first
f100(1, c=3, b=2)    # (1, 2, 3)
# f100(1, a=3, b=2)  # TypeError: f100() got multiple values for keyword argument 'a'

# f100(1, b=2, 3)      # SyntaxError: non-keyword arg after keyword arg

print('-' * 10 + "A.5. Arguments matching: default arguments" + '-' * 10)

# If not passed a value, the argument is assigned its default
# before the function runs.

def f110(a, b=2, c=3): print(a, b, c) 
f110(1)       # (1, 2, 3)
f110(a=1)     # (1, 2, 3)
f110(1, 4)    # (1, 4, 3)

# Keywords allow us to essentially skip over arguments with defaults
# Here, a gets 1 by position, c gets 6 by keyword, and b, in between, defaults to 2.
f110(1, c=6)  # (1, 2, 6)

def f120(spam, eggs, toast=0, ham=0):
    print(spam, eggs, toast, ham)
    
f120(1, 2)                      # (1, 2, 0, 0)
f120(1, ham=1, eggs=0)          # (1, 0, 0, 1)
f120(spam=1, eggs=0)            # (1, 0, 0, 0)
f120(toast=1, eggs=2, spam=3)   # (3, 2, 1, 0)
f120(1, 2, 3, 4)                # (1, 2, 3, 4)

# Mutable defaults retain state from
def f130(a = []):
    a.append(1)
    print a
    
f130()     # [1]
f130()     # [1, 1]
f130()     # [1, 1, 1]
f130([5])  # [5, 1]
f130([7])  # [7, 1]
f130()     # [1, 1, 1, 1]

print('-' * 10 + "A.6. Arguments matching: arbitrary arguments" + '-' * 10)

# Collect unmatched positional arguments into a tuple.
# When this function is called, Python collects all the positional arguments into a new
# tuple and assigns the variable args to that tuple.
def f200(*args): print(args)
f200()             # ()
f200(1)            # (1,)
f200(1, 2, 3, 4)   # (1, 2, 3, 4)
 
# The ** feature is similar, but it ONLY works for KEYWORD arguments
# it collects them into a new dictionary.
def f210(**args): print(args)
f210()                # {}
f210(a=1, b='2')      # {'a': 1, 'b': '2'}

# 
# 1 is passed to a by position, 2 and 3 into pargs positional tuple, 
# and x and y wind up in the kargs keyword dictionary
def f220(a, *pargs, **kargs): print(a, pargs, kargs)
f220(1, 2, 3, x=1, y=2)  # (1, (2, 3), {'y': 2, 'x': 1})

print('-' * 10 + "A.7. Arguments matching: unpacking arguments" + '-' * 10)

# Unpacking meaning is the inverse of its meaning in the function definition-it
# unpacks a collection of arguments, rather than building a collection of arguments. 
# For example, we can pass four arguments to a function in a tuple and let Python unpack
# them into individual arguments

def f300(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
f300(*args)      # (1, 2, 3, 4)

kargs = {'a': 1, 'b': 2, 'c': 3}
kargs['d'] = 4
f300(**kargs)    # (1, 2, 3, 4)

kargs = {'a': 1, 'b': 2, 'c': 3}
# f300(**kargs)    # TypeError: f300() takes exactly 4 arguments (3 given)
kargs = {'a': 1, 'b': 2, 'c': 3, 'e': 4}
# f300(**kargs)    # TypeError: f300() got an unexpected keyword argument 'e'

f300(*(1, 2), **{'d': 4, 'c': 3})     # (1, 2, 3, 4)
f300(1, *(2, 3), **{'d': 4})          # (1, 2, 3, 4)
# (2) [not (2,)] will be considered as just an integer, not tuple
f300(1, c=3, *(2,), **{'d': 4})       # (1, 2, 3, 4) 
f300(1, *(2, 3), d=4)                 # (1, 2, 3, 4)
f300(1, *(2,), c=3, **{'d': 4})       # (1, 2, 3, 4)

print('-' * 10 + "A.8. Arguments matching: applying functions generally" + '-' * 10)

def f400(a): print(a)
def f410(a, b, c): print(a, b, c)

cond = True
if cond:
    action, args = f400, (1,)
else:
    action, args = f410, (1, 2, 3)
action(*args)  # 1, dispatch generically

# This technique also comes in handy for functions that test or time other functions.
# For instance, in the following code we support any function with any arguments
# by passing along whatever arguments were sent in.

def tracer(func, *pargs, **kargs):
    print('calling:', func.__name__)
    return func(*pargs, **kargs)

def f420(a, b, c, d):
    return a + b + c + d

rv = tracer(f420, 1, 2, c=3, d=4)    # ('calling:', 'f420')
print rv                             # 10
# rv = tracer(f420, 1, c=2, 3, d=4)  # SyntaxError: non-keyword arg after keyword arg

print('-' * 10 + "A.9. Arguments matching: Python 3.X keyword-only arguments" + '-' * 10)

# Didn't learn

print('-' * 10 + "A.10. Arguments matching: Exercise" + '-' * 10)

# Suppose you want to code a function that is able to compute the minimum value from
# an arbitrary set of arguments and an arbitrary set of object data types. That is, the
# function should accept zero or more arguments, as many as you wish to pass. Moreover,
# the function should work for all kinds of Python object types: numbers, strings, lists,
# lists of dictionaries, files, and even None.

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res: res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first: first = arg
    return first 

def min3(*args):
    l = list(args)
    l.sort()  # it's programmed in C, but sorting is still slower than 1 time pass in min1 and min2
    return l[0]

print(min1(3, 4, 1, 2))              # 1
print(min2("ab", "ba"))              # ab
print(min3([2, 1], [1, 2], [3, 3]))  # [1, 2]

# Example of minmax function

def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def morethan(x, y): return x > y

# To find minimum
print(minmax(lessthan, 4, 3, 1, 19, 5))  # 1
# To find maximum
print(minmax(morethan, 4, 3, 1, 19, 5))  # 19

# The built-in versions of min and max work almost exactly like ours, but they're coded
# in C for optimal speed and accept either a single iterable or multiple arguments.

print('-' * 10 + "A.10. Generalized set functions" + '-' * 10)

# Function that intersects an arbitrary number of sequences
# Common elements in EACH sequence

def intersect(*args):                   # args will be a tuple of all arguments
    res = []
    for x in args[0]:                   # scan first sequence
        if x in res: continue           # skip duplicates
        for other in args[1:]:          # go through all other sequences
            # element x isn't in one of the other sequences, break internal loop
            if x not in other: break
        else:                           # ELSE OF FOR: if we finished without break  
            res.append(x)
    return res

s1, s2, s3 = "SPAM", "SCAM", "SLAM"
print(intersect(s1, s2, s3))              # ['S', 'A', 'M']
print(intersect([1, 2, 3], (5, 7, 1)))    # [1], mixed type of input variables

# Union of an arbitrary number of sequences

def union(*args):
    res = []
    for arg in args:
        for x in arg:
            if x not in res:
                res.append(x)
    return res

print(union(s1, s2, s3))              # ['S', 'P', 'A', 'M', 'C', 'L']
print(union([1, 2, 3], (5, 7, 1)))    # [1, 2, 3, 5, 7]

print('-' * 10 + "A.11. Emulating Python 3.X print function" + '-' * 10)

# To use Python 3.X version we can always print
# from __future__ import print_function

import sys

def print3(*args, **kargs):
    
    # Get parameters 
    sep = kargs.get('sep', ' ') # ' ' is a default value if the key isn't present
    end = kargs.get('end', '\n')
    f = kargs.get('file', sys.stdout)
    
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)  # Ternary operator
        first = False
    f.write(output + end)                            # Write to file or to the stream
    
print3(1, 2, 3)                     # 1 2 3
print3(1, 2, 3, sep='')             # 123
print3(1, [2, 3], (4,), sep='...')  # 1...[2, 3]...(4,)

print('-' * 10 + "A.12. Some examples" + '-' * 10)

def func500(a, *pargs):
    print(a, pargs)
func500(1, 2, 3)                       # (1, (2, 3)), *pargs pack in tuple


def func510(a, **kargs):
    print(a, kargs)
func510(a=1, c=3, b=2)                 # (1, {'c'=3, 'b'=2})

def func520(a, b, c=3, d=4): 
    print(a, b, c, d)
func520(1, *(5, 6))                    # (1, 5, 6, 4) unpack

def func530(a, b, c): 
    a = 2; b[0] = 'x'; c['a'] = 'y'
l = 1; m = [1]; n = {'a': 0}
func530(l, m, n)
print(l, m, n)                         # (1, ['x'], {'a': y}) mutable, in place changes




