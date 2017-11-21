

import math
import time
import random
import sys

print('-' * 10 + "A.1. The basics" + '-' * 10)

# The basics. At the Python interactive prompt, write a function that prints its single
# argument to the screen and call it interactively, passing a variety of object types:
# string, integer, list, dictionary. Then, try calling it without passing any argument.
# What happens? What happens when you pass two arguments?

def SimplePrint(s):
    print(s)

SimplePrint('abc')                              # abc
SimplePrint(1)                                  # 1
SimplePrint(['a', 'b', 3])                      # ['a', 'b', 3]
SimplePrint({'a':1, 'b':2})                     # {'a': 1, 'b': 2}
# SimplePrint()                                 # TypeError: SimplePrint() takes exactly 1 argument (0 given)
# SimplePrint('a', 'b')                         # TypeError: SimplePrint() takes exactly 1 argument (2 given)

print('-' * 10 + "A.2. Arguments" + '-' * 10)

# Arguments. Write a function called adder in a Python module file. The function
# should accept two arguments and return the sum (or concatenation) of the two.
# Then, add code at the bottom of the file to call the adder function with a variety of
# object types (two strings, two lists, two floating points), and run this file as a script
# from the system command line. Do you have to print the call statement results to
# see results on your screen?

def Adder(a, b):
    return a + b

print(Adder('abc', 'def'))                      # abcdef
print(Adder(['a', '1'], ['b', '2']))            # ['a', '1', 'b', '2']
print(Adder(1.101, 2.202))                      # 3.303
# print(Adder({'a': 1,}, {'b': 2}))             # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(Adder({'a', 1}, {'b', 2}))              # TypeError: unsupported operand type(s) for +: 'set' and 'set'

print('-' * 10 + "A.3. Varargs" + '-' * 10)

# varargs. Generalize the adder function you wrote in the last exercise to compute
# the sum of an arbitrary number of arguments, and change the calls to pass more
# or fewer than two arguments. What type is the return value sum? (Hints: a slice
# such as S[:0] returns an empty sequence of the same type as S, and the type built-
# in function can test types; but see the manually coded min examples in Chapter 18 
# for a simpler approach.) What happens if you pass in arguments of different
# types? What about passing in dictionaries?

def Adder2(*pargs):
    if not pargs: return None
    rv = pargs[0]
    for x in pargs[1:]:
        if type(x) != type(rv): raise BaseException
        rv += x
    return rv

print(Adder2('abc', 'def', 'ghi'))              # abcdefghi
print(Adder2(1, 2, 3, 4))                       # 10
print(Adder2())                                 # None
# print(Adder2('a', 1, 'b', 2))                 # BaseException - arguments of different types
# print(Adder2({'a': 1}, {'b': 2}))             # TypeError: unsupported operand type(s) for +=: 'dict' and 'dict' 


print('-' * 10 + "A.4. Keywords" + '-' * 10)

# Keywords. Change the adder function from exercise 2 to accept and sum/concatenate
# three arguments: def adder(good, bad, ugly). Now, provide default values
# for each argument, and experiment with calling the function interactively. Try
# passing one, two, three, and four arguments. Then, try passing keyword arguments. 
# Does the call adder(ugly=1, good=2) work? Why? Finally, generalize the
# new adder to accept and sum/concatenate an arbitrary number of keyword arguments. 
# This is similar to what you did in exercise 3, but you'll need to iterate over
# a dictionary, not a tuple. (Hint: the dict.keys method returns a list you can step
# through with a for or while, but be sure to wrap it in a list call to index it in 3.X;
# dict.values may help here too.)

def Adder3(a=100, b=200, c=300):
    return a + b + c

print(Adder3(1))                                # 501
print(Adder3(1, 2))                             # 301
print(Adder3(1, 2, 3))                          # 6
# print(Adder3(1, 2, 3, 4))                     # TypeError: Adder3() takes at most 3 arguments (4 given)

print(Adder3(a=1))                              # 501
print(Adder3(b=2))                              # 402
print(Adder3(a=1, b=2))                         # 303
print(Adder3(b=1, a=2))                         # 303

def Adder4(**kargs):
    keys = list(kargs.keys())                   # Without list() next line will produce an error in Python 3.X: TypeError: 'dict_keys' object does not support indexing
    rv = kargs[keys[0]]                         # So rv is the type of what is the value in dictionary
    for k in keys[1:]:
        rv += kargs[k]
    return rv

# print(Adder4(1))                              # TypeError: Adder4() takes exactly 0 arguments (1 given) - only keyword arguments are allowed
print(Adder4(a=1))                              # 1
print(Adder4(b=2))                              # 2
print(Adder4(a=1, b=2))                         # 3
print(Adder4(b=1, a=2))                         # 3


print('-' * 10 + "A.5. Dictionary tools" + '-' * 10)

# Dictionary tools. Write a function called copyDict(dict) that copies its dictionary
# argument. It should return a new dictionary containing all the items in its argument.
# Use the dictionary keys method to iterate (or, in Python 2.2 and later, step
# over a dictionary's keys without calling keys). Copying sequences is easy (X[:]
# makes a top-level copy); does this work for dictionaries, too? As explained in this
# exercise's solution, because dictionaries now come with similar tools, this and the
# next exercise are just coding exercises but still serve as representative function
# examples.

def copyDict1(dict):
    rv = {}
    for key in dict:
        rv[key] = dict[key]
    return rv

myDict = {'a': 1, 'b': 2, 'c': 3}
rv1 = copyDict1(myDict)
myDict['a'] = 100
print("myDict: ", myDict, "rv1: ", rv1)         # ('myDict: ', {'a': 100, 'c': 3, 'b': 2}, 'rv1: ', {'a': 1, 'c': 3, 'b': 2})

# Easier copy

myDict = {'a': 1, 'b': 2, 'c': 3}
rv2 = dict(myDict)
myDict['a'] = 100 
print("myDict: ", myDict, "rv2: ", rv2)         # ('myDict: ', {'a': 100, 'c': 3, 'b': 2}, 'rv2: ', {'a': 1, 'c': 3, 'b': 2})

myDict = {'a': 1, 'b': 2, 'c': 3}
rv2 = myDict.copy()
myDict['a'] = 100 
print("myDict: ", myDict, "rv2: ", rv2)         # ('myDict: ', {'a': 100, 'c': 3, 'b': 2}, 'rv2: ', {'a': 1, 'c': 3, 'b': 2})  

myDict = {'a': 1, 'b': 2, 'c': 3}
# rv2 = myDict[:]                               # TypeError: unhashable type

# Remember that here we just copy a reference

myDict = {'a': 1, 'b': 2, 'c': 3}
rv3 = myDict
myDict['a'] = 100 
print("myDict: ", myDict, "rv3: ", rv3)         # ('myDict: ', {'a': 100, 'c': 3, 'b': 2}, 'rv3: ', {'a': 100, 'c': 3, 'b': 2})


print('-' * 10 + "A.6. Dictionary tools again" + '-' * 10)

# Dictionary tools. Write a function called addDict(dict1, dict2) that computes the
# union of two dictionaries. It should return a new dictionary containing all the items
# in both its arguments (which are assumed to be dictionaries). If the same key appears
# in both arguments, feel free to pick a value from either. Test your function
# by writing it in a file and running the file as a script. What happens if you pass lists
# instead of dictionaries? How could you generalize your function to handle this case,
# too? (Hint: see the type built-in function used earlier.) Does the order of the arguments
# passed in matter?

def addDict(dict1, dict2):
    if isinstance(dict1, dict):                # Handle the case of dicts
        rv = dict1.copy()
        for k in dict2: 
            rv[k] = dict2[k] 
    else: 
        rv = dict1[:] + dict2[:]               # Handle the case of lists
    return rv

print(addDict({"a":1, "b":2}, {"c":3, "d":4}))  # {'a': 1, 'c': 3, 'b': 2, 'd': 4}
print(addDict(["a", 1], ["b", 2]))              # ['a', 1, 'b', 2]
 
 
print('-' * 10 + "A.7. Argument-matching examples" + '-' * 10)

# 7. More argument-matching examples. First, define the following six functions (either
# interactively or in a module file that can be imported).
# Now, test the following calls interactively, and try to explain each result; in some
# cases, you'll probably need to fall back on the matching algorithm shown in Chapter 18. 
# Do you think mixing matching modes is a good idea in general? Can you
# think of cases where it would be useful?

def f1(a, b): print(a, b)                       # Normal args
def f2(a, *b): print(a, b)                      # Positional varargs
def f3(a, **b): print(a, b)                     # Keyword varargs
def f4(a, *b, **c): print(a, b, c)              # Mixed modes
def f5(a, b=2, c=3): print(a, b, c)             # Defaults
def f6(a, b=2, *c): print(a, b, c)              # Defaults and positional varargs

f1(1, 2)                                        # (1, 2)
f1(b=2, a=1)                                    # (1, 2)
f2(1, 2, 3)                                     # (1, (2, 3))
f3(1, x=2, y=3)                                 # (1, {'x':2, 'y':3})
f4(1, 2, 3, x=2, y=3)                           # (1, (2, 3), {'x':2, 'y':3})
f5(1)                                           # (1, 2, 3)
f5(1, 4)                                        # (1, 4, 3)
f6(1)                                           # (1, 2, ())
f6(1, 3, 4)                                     # (1, 3, (4,))

print('-' * 10 + "A.8. Primes revisited" + '-' * 10)

#8. Primes revisited. Recall the following code snippet from Chapter 13, which 
# simplistically determines whether a positive integer is prime.
# Package this code as a reusable function in a module file (y should be a passed-in
# argument), and add some calls to the function at the bottom of your file. While
# you're at it, experiment with replacing the first line's // operator with / to see how
# true division changes the / operator in Python 3.X and breaks this code (refer back
# to Chapter 5 if you need a reminder). What can you do about negatives, and the
# values 0 and 1? How about speeding this up?

def factor(y):
    
    if y < 0:
        raise BaseException
    
    x = y // 2                                  # It is actually possible to look up until sqrt(y) here  
    # x = y ** 0.5                              # For speed up    
    while x > 1:                                # Not including 1
        if y % x == 0:
            print(y, " has factor ", x)
            break
        x -= 1
    else:                                       # Normal exit 
        print(y, " is prime")

factor(5)                                       # (5, ' is prime') 
factor(25)                                      # (25, ' has factor ', 5) 
factor(101)                                     # (101, ' is prime') 

# In Python 2.X, if we change // for / then the result is the same
# In Python 3.X, 5 / 2 will return 2.5 and 5 // 2 will return 2
# In Python 3.X, if we change // for / then the result is WRONG
# 5  has factor  2.5
# 25  has factor  12.5
# 101  has factor  50.5

# factor(-1)                                    # BaseException
factor(0)                                       # (0, ' is prime')
factor(1)                                       # (1, ' is prime')


print('-' * 10 + "A.9. Iterations and comprehensions" + '-' * 10)

# 9. Iterations and comprehensions. Write code to build a new list containing the square
# roots of all the numbers in this list: [2, 4, 9, 16, 25]. Code this as a for loop first,
# then as a map call, then as a list comprehension, and finally as a generator expression. 
# Use the sqrt function in the built-in math module to do the calculation (i.e.,
# import math and say math.sqrt(x)). Of the four, which approach do you like best?

l = [2, 4, 9, 16, 25]

for x in l:
    lNew = math.sqrt(x)
print(lNew)                                     # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]  

lNew = map(math.sqrt, l)
print(lNew)                                     # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0] 

lNew = map(lambda x: x ** 0.5, l)
print(lNew)                                     # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

lNew = [math.sqrt(x) for x in l]
print(lNew)                                     # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

lNew = (math.sqrt(x) for x in l)
print(list(lNew))                               # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

print('-' * 10 + "A.10. Timing tools" + '-' * 10)

# 10. Timing tools. In Chapter 5, we saw three ways to compute square roots:
# math.sqrt(X), X ** .5, and pow(X, .5). If your programs run a lot of these, their
# relative performance might become important. To see which is quickest, repurpose
# the timerseqs.py script we wrote in this chapter to time each of these three tools.
# Use the bestof or bestoftotal functions in one of this chapter's timer modules to
# test (you can use either the original, the 3.X-only keyword-only variant, or the 2.X/
# 3.X version, and may use Python's timeit module as well). You might also want
# to repackage the testing code in this script for better reusability-by passing a test
# functions tuple to a general tester function, for example (for this exercise a copy-
# and-modify approach is fine). Which of the three square root tools seems to run
# fastest on your machine and Python in general? Finally, how might you go about
# interactively timing the speed of dictionary comprehensions versus for loops?

# Very important to use time.time for Linux 
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))               # Equalize 2.X and 3.X
    start = timer()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last resull)
    """
    best = 2 ** 32                             # 136 years seems large enough
    for _ in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

# Runs nested total tests within a best-of test, to get the best-of-totals time.

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


x = random.randint(1000000, 2000000)

print(total(1000000, math.sqrt, x))                     # (1.963301181793213, 1264.8616525138234)
print(total(1000000, lambda x: x ** .5, x))             # (4.259144067764282, 1264.8616525138234)
print(total(1000000, pow, x, .5))                       # (3.5202479362487793, 1264.8616525138234)

print(bestoftotal(3, 1000000, math.sqrt, x))            # (2.3262438774108887, (1.9430460929870605, 1232.8531948289708))
print(bestoftotal(3, 1000000, lambda x: x ** .5, x))    # (5.012866973876953, (4.615306854248047, 1232.8531948289708))
print(bestoftotal(3, 1000000, pow, x, .5))              # (3.5272529125213623, (3.1887550354003906, 1232.8531948289708))

print('-' * 10 + "A.11. Recursive functions" + '-' * 10)

# 11. Recursive functions. Write a simple recursion function named countdown that prints
# numbers as it counts down to zero. For example, a call countdown(5) will print: 5
# 4 3 2 1 stop. There's no obvious reason to code this with an explicit stack or
# queue, but what about a nonfunction approach? Would a generator make sense here?

def countdown(n):
    if n < 1:
        return
    print(n),
    countdown(n-1)

print()
countdown(5)                                            # 5 4 3 2 1

# Python 2.X: SyntaxError: invalid syntax - because print is a statement
# Python 3.X: ok - because print is a function
# [print(x) for x in range(5)]                

print('-' * 10 + "A.12. Computing factorials" + '-' * 10)

# 12. Computing factorials. Finally, a computer science classic (but demonstrative 
# nonetheless). We employed the notion of factorials in Chapter 20's coverage of permutations: N!, 
# computed as N*(N-1)*(N-2)*...1. For instance, 6! is 6*5*4*3*2*1, or 720. 
# Code and time four functions that, for a call fact(N), each return N!. Code
# these four functions (1) as a recursive countdown per Chapter 19; (2) using the
# functional reduce call per Chapter 19; (3) with a simple iterative counter loop per
# Chapter 13; and (4) using the math.factorial library tool per Chapter 20. Use
# Chapter 21's timeit to time each of your functions. What conclusions can you
# draw from your results?

# As a recursive countdown per Chapter 19
def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n - 1)

from functools import reduce  # was moved here in Python 3.X (only required in Python 3.X)

# Using the functional reduce call per Chapter 19
def factorial2(n):
    return reduce(lambda x, y: x*y, range(1, n + 1))

# With a simple iterative counter loop per
def factorial3(n):
    rv = 1
    for x in range(1, n + 1):
        rv *= x
    return rv

# using the math.factorial library tool per Chapter 20
def factorial4(n):
    return math.factorial(n)

print(total(10000, factorial1, 30)) 
print(total(10000, factorial2, 30))
print(total(10000, factorial3, 30))
print(total(10000, factorial4, 30))


(0.08722496032714844, 265252859812191058636308480000000L)
(0.08804202079772949, 265252859812191058636308480000000L)
(0.056723833084106445, 265252859812191058636308480000000L)
(0.03650188446044922, 265252859812191058636308480000000L)