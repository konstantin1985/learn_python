

# MAIN SOURSE:
# Lutz, "Learning Python" chapter 36


# USEFUL LINK:
# 1) *pargs, ** kargs
#    https://stackoverflow.com/questions/3394835/args-and-kwargs
# 2) sys.exc_info
#    https://docs.python.org/2/library/sys.html
# GENERAL INFORMATION:


# Error handling. Write a function called safe(func, *pargs, **kargs)
# that runs any function with any number of positional and/or keyword
# arguments by using the* arbitrary arguments header and call syntax,
# catches any exception raised while the function runs, and prints the
# exception using the exc_info call in the sys module.

# Then use your safe function to run your oops function from exercise
# 1 or 2. Put safe in a module file called exctools.py, and pass it
# the oops function interactively. What kind of error messages do you get? 

# Finally, expand safe to also print a Python stack trace when an error
# occurs by calling the built-in print_exc function in the standard
# traceback module; see earlier in this chapter, and consult the Python
# library reference manual for usage details. 

import sys
import traceback

def oops():
    raise KeyError

def foo(a):
    raise IndexError

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)                                         # Unpack arguments and call the function
    except:
        print('Got %s %s' % (sys.exc_info()[0], sys.exc_info()[1]))   # Most recent exception: type, value, traceback
        print(traceback.print_exc())

if __name__ == "__main__":
    # pass
    safe(oops)
    safe(foo, 'abc')

# We could probably code  safe as a function decorator using Chapter 32
# techniques, but we'll have to move on to the next part of the book to
# learn fully how (see the solutions for a preview).

def safe_decorator(func):
    
    def proxy(*pargs, **kargs):
        try:
            func(*pargs, **kargs)
        except:
            print('Got %s %s' % (sys.exc_info()[0], sys.exc_info()[1]))
            print(traceback.print_exc())
    
    return proxy

if __name__ == "__main__":
    
    @safe_decorator
    def test():
        oops()
        
    test()




