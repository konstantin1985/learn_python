

# USEFUL LINKS:


# GENERAL INFORMATION:

# In Python, exceptions are triggered automatically on errors, 
# and they can be triggered and intercepted by your code.


# try/except : Catch and recover from exceptions raised by Python, 
# or by you.
# try/finally: Perform cleanup actions, whether exceptions occur or not.
# raise      : Trigger an exception manually in your code.
# assert     : Conditionally trigger an exception in your code.
# with/as    : Implement context managers in Python 2.6, 3.0, and later.

# You can jump to an exception handler in a single step, abandoning all 
# function calls begun since the exception handler was entered. Code in
# the exception handler can then respond to the raised exception as
# appropriate.

# One way to think of an exception is as a sort of structured "super go to."
# An exception handler ( try statement) leaves a marker and executes some 
# code. Somewhere further ahead in the program, an exception is raised that
# makes Python jump back to that marker, abandoning any active functions that
# were called after the marker was left. This protocol provides a coherent
# way to respond to unusual events. Moreover, because Python jumps to the
# handler statement immediately, your code is simpler-there is usually no
# need to check status codes after every call to a function that could
# possibly fail.

# Exception roles:
# Error handling
# Event notification
#     Special-case handling: Sometimes a condition may occur so rarely that 
#     it's hard to justify convoluting your code to handle it in multiple
#     places. You can often eliminate special-case code by handling unusual
#     cases in exception handlers in higher levels of your program. (assert)
# Termination actions

# Notice that there's no way in Python to go back to the code that triggered
# the exception (short of rerunning the code that reached that point all over
# again, of course). Once you've caught the exception, control continues
# after the entire try that caught the exception, not after the statement
# that kicked it off. 

print("-" * 20 + "#1 User-Defined Exceptions" + "-" * 20)

# You can also define new exceptions of your own that are specific to your
# programs. User-defined exceptions are coded with classes, which inherit
# from a built-in exception class: usually the class named Exception.

class CustomException(Exception): pass                                 # User-defined exception

def fcn():
    raise CustomException()                                            # Raise an instance

try: 
    fcn()
except CustomException:
    print("got exception")                                             # got exception
    
# An "as" clause on an except can gain access to the exception object itself.
# Class-based exceptions allow scripts to build exception categories, which
# can inherit behavior, and have attached state information and methods. They
# can also customize their error message text displayed if they're not caught.

class Career(Exception):
    def __str__(self): 
        return "So I became a waiter..."

# raise Career()                                                       # __main__.Career: So I became a waiter...

print("-" * 20 + "#2 Termination Actions" + "-" * 20)

# These look like except handlers for exceptions, but the try/finally
# combination specifies termination actions that always execute "on 
# the way out," regardless of whether an exception occurs in the try
# block or not.

def after1():
    try:
        raise BaseException
    finally:
        print('after fetch 1')
    print('after try 1')
    
#after1()

# after fetch 1
#     raise BaseException
# BaseException

# IMPORTANT:
# "finally" block is executed, but exception is still raised.
# Here, we don't get the "after try 1" message because control does not
# resume after the try/finally block when an exception occurs. Instead,
# Python jumps back to run the finally action, and then propagates the
# exception up to a prior handler (in this case, to the default handler
# at the top). 

# If there is no exception, both finally and the lines after 
# (print('after try 2')) are executed.

def after2():
    try:
        pass
    finally:
        print('after fetch 2')
    print('after try 2')

after2()
# after fetch 2
# after try 2

# For the comparison, "except" suppresses the exception propagation.
# No exception is raised here.

def after3():
    try:
        raise BaseException
    except:
        print('after fetch 3')
    print('after try 3')
    
after3()
# after fetch 3
# after try 3

# In practice, try/except combinations are useful for catching and
# recovering from exceptions, and try/finally combinations come in
# handy to guarantee that termination actions will fire regardless
# of any exceptions that may occur in the try block's code. For
# instance, you might use try/except to catch errors raised by code
# that you import from a third-party library, and try/finally to
# ensure that calls to close files or terminate server connections
# are always run.

print("-" * 20 + "#3 Why You Will Care: Error Checks" + "-" * 20)

# For instance, if you want to write robust programs in the C language,
# you generally have to test return values or status codes after every
# operation that could possibly go astray, and propagate the results
# of the tests as your programs run:

# doStuff()
# {                                                                 # C program
#     if (doFirstThing() == ERROR)                                  # Detect errors everywhere 
#         return ERROR;                                             # even if not handled here
#     if (doNextThing() == ERROR)
#         return ERROR;
#     ...
#     return doLastThing();
# }

# main()
# {
# if (doStuff() == ERROR)
#     badEnding();
# else
#     goodEnding();
# }

# In fact, realistic C programs often have as much code devoted to
# error detection as to doing actual work. But in Python, you don't
# have to be so methodical (and neurotic!). You can instead wrap 
# arbitrarily vast pieces of a program in exception handlers and 
# simply write the parts that do the actual work, assuming all is
# normally well.

# def doStuff():
#     doFirstThing()                                                # We don't care about exceptions here,
#     doNextThing()                                                 # so we don't need to detect them
#     ...
#     doLastThing()

# if __name__ == '__main__':
#     try:                                                          # This is where we care about results, 
#         doStuff()                                                 # so it's the only place we must check
#     except:
#         badEnding()
#     else:
#         goodEnding()

# Because control jumps immediately to a handler when an exception 
# occurs, there's no need to instrument all your code to guard for
# errors, and there's no extra performance overhead to run all the
# tests. Moreover, because Python detects errors automatically,
# your code often doesn't need to check for errors in the first
# place. The upshot is that exceptions let you largely ignore the 
# unusual cases and avoid error-checking code that can distract 
# from your program's goals.




