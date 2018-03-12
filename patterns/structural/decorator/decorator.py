

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 5

# USEFUL LINKS:
#
# 1) UML + explanation
#    https://en.wikipedia.org/wiki/Decorator_pattern
#
# 2) Cross-cutting concerns
#    https://stackoverflow.com/questions/23700540/cross-cutting-concern-example
#
# 3) Use timeit.Timer()
#    https://docs.python.org/2/library/timeit.html


# GENERAL INFORMATION:

# Composition should generally be preferred over inheritance, because
# inheritance makes code reuse harder, it's static, and applies to an
# entire class and all instances of it.

# [Python implementation]

# A Decorator pattern can add responsibilities to an object dynamically,
# and in a transparent manner. A Python decorator is a specific change
# to the syntax of Python that is used for extending the behavior of a
# class, method, or function without using inheritance. In terms of 
# implementation, a Python decorator is a callable (function, method, 
# class) that accepts a function object fin as input, and returns another
# function object fout. This means that any callable that has these
# properties can be treated as a decorator.

# There is no one-to-one relationship between the Decorator pattern and
# Python decorators. Python decorators can actually do much more than
# the Decorator pattern. One of the things they can be used for, is to
# implement the Decorator pattern.


# [Generic implementation (not only Python) - from wiki]

# Decorator class wraps the original class. This wrapping could be
# achieved by the following sequence of steps:
# - Subclass the original Component class into a Decorator class
# - In the Decorator class, add a Component pointer as a field
# - In the Decorator class, pass a Component to the Decorator 
#   constructor to initialize the Component pointer
# - In the Decorator class, forward all Component methods to the 
#   Component pointer
# - In the ConcreteDecorator class, override any Component method(s)
#   whose behavior needs to be modified.


print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# The Decorator pattern shines when used for implementing cross-cutting
# concerns. Examples of cross-cutting concerns are:
# - Data validation
# - Transaction processing (A transaction in this case is similar to
#   a database transaction, in the sense that either all steps should
#   be completed successfully, or the transaction should fail.)
# - Caching
# - Logging
# - Monitoring
# - Debugging
# - Business rules
# - Compression
# - Encryption

# In general, all parts of an application that are generic and can be
# applied to many other parts of it, are considered cross-cutting 
# concerns.

# https://stackoverflow.com/questions/23700540/cross-cutting-concern-example

# A Concern is a term that refers to a part of the system divided on
# the basis of the functionality.

# The concerns representing single and specific functionality for PRIMARY 
# requirements are known as core concerns. For example: Business logic

# The crosscutting concern (=system-wide concern) is a concern which is 
# applicable throughout the application and it affects the entire application.

# For example: logging, security and data transfer are the concerns which
# are needed in almost every module of an application, hence they are
# cross-cutting concerns.

# Another popular example of using the Decorator pattern is Graphical
# User Interface (GUI) toolkits. In a GUI toolkit, we want to be able
# to add features such as borders, shadows, colors, and scrolling to
# individual components/widgets.

from timeit import Timer

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# Memoization decorator.

print("-" * 20 + "# 2.1 Naive Fibonacci's algorithm" + "-" * 20)

def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    t = Timer()
    # To give the timeit module access to functions you define, you can
    # pass a setup parameter which contains an import statement. Instead
    # of Timer() timeit() or repeat() may be used when we need to set a 
    # number of repetitions. Timer() is a class for timing execution speed
    # of small code snippets. 
    t = Timer('fibonacci(7)', setup = "from __main__ import fibonacci")
    print(t.timeit())

    # OUTPUT: 9.43 sec (very long)


print("-" * 20 + "# 2.2 Fibonacci's algorithm with memoization" + "-" * 20)

known = {0:0, 1:1}

def fibonacci2(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = res
    return res

if __name__ == "__main__":
    t = Timer('fibonacci2(100)', setup = "from __main__ import fibonacci2")
    print(t.timeit())

    # OUTPUT: 0.23 sec
    
# But there are already a few problems with this approach. While the
# performance is not an issue any longer, the code is not as clean as
# it is when not using memoization. And what happens if we decide to
# extend the code with more math functions and turn it into a module?
# Let's assume that the next function we decide to add is nsum(), which
# returns the sum of the first n numbers. 

known_sum = {0:0}

def nsum(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n-1)
    known_sum[n] = res
    return res

# Do you notice the problem already? We ended up with a new dict called
# known_sum which acts as our cache for nsum, and a function that is
# more complex than it would be without using memoization. Our module 
# is becoming unnecessarily complex. Is it possible to keep the recursive
# functions as simple as the naive versions, but achieve a performance 
# similar to the performance of the functions that use memoization?

print("-" * 20 + "# 2.2 Fibonacci's algorithm with memoization by the decorator" + "-" * 20)

import functools

def memoize_decorator(fn):
    known = dict()
    
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)                                # *args unpacks a tuple (a,b)
        return known[args]

    return memoizer

@memoize_decorator
def nsum3(n):
    """ Returns the sum of the first n numbers """
    assert (n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum3(n-1)

@memoize_decorator
def fibonacci3(n):
    """ Returns the nth number of the FIbonacci sequence"""
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci3(n-1) + fibonacci3(n-2) 
    
if __name__ == "__main__":
    measure = [{'exec':'fibonacci3(100)', 'import':'fibonacci3', 'func':fibonacci3},
               {'exec':'nsum3(200)', 'import':'nsum3', 'func':nsum3}]
    
    for m in measure:
        
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))

        print('name: {}, doc: {}, executing: {}, time: {}'.format(m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))

    # OUTPUT:
    # name: fibonacci3, doc:  Returns the nth number of the FIbonacci sequence, executing: fibonacci3(100), time: 0.371177911758
    # name: nsum3, doc:  Returns the sum of the first n numbers , executing: nsum3(200), time: 0.394763946533
    
  
# Now, you might argue that this is not the Decorator pattern, since
# we don't apply it in runtime. The truth is that a decorated function
# cannot be undecorated; but you can still decide in runtime if the
# decorator will be executed or not. 

# I have one last exercise for you. The memoize() decorator does not 
# work with functions that accept more than one argument. How can we
# verify that? After verifying it, try finding a way of fixing this issue.


