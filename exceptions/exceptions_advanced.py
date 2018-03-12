


# USEFUL LINKS:


# GENERAL INFORMATION:

# The two common variations on the try statement are try/except/else (for
# catching exceptions) and try/finally (for specifying cleanup actions that
# must occur whether an exception is raised or not).

print("-" * 20 + "#1 The try/except/else Statement" + "-" * 20)

# try:
#     statements                                                       # Run this main action first
# except name1:
#     statements                                                       # Run if name1 is raised during try block
# except (name2, name3):
#     statements                                                       # Run if any of these exceptions occur
# except name4 as var:
#     statements                                                       # Run if name4 is raised, assign instance raised to var
# except:
#     statements                                                       # Run for all other exceptions raised
# else:
#     statements                                                       # Run if no exception was raised during try block
# finally:
#     statements                                                       # Always perform this block on exit (exception or no exception)


# Semantically, the block under the try header in this statement represents the main
# action of the statement-the code you're trying to run and wrap in error processing
# logic. The except clauses define handlers for exceptions raised during the try block,
# and the else clause (if coded) provides a handler to be run if no exceptions occur.

# If an exception occurs while the try block's statements are running, and the 
# exception matches one that the statement names, Python jumps back to the try and
# runs the statements under the first except clause that matches the raised exception,
# after assigning the raised exception object to the variable named after the as 
# keyword in the clause (if present). After the except block runs, control then resumes
# below the entire try statement (unless the except block itself raises another 
# exception, in which case the process is started anew from this point in the code).

# If an exception occurs while the try block's statements are running, but the 
# exception does not match one that the statement names, the exception is propagated
# up to the next most recently entered try statement that matches the exception; if
# no such matching try statement can be found and the search reaches the top level
# of the process, Python kills the program and prints a default error message.

# If an exception does not occur while the try block's statements are running, Python
# runs the statements under the else line (if present), and control then resumes below
# the entire try statement.

# Formally, there may be any number of except clauses, but you can code else only if
# there is at least one except, and there can be only one else and one finally. 

# except clauses that list a set of exceptions in parentheses (except (e1, e2, e3):)
# catch any of the listed exceptions. Because Python looks for a match within a given
# try by inspecting the except clauses from top to bottom, the parenthesized version
# has the same effect as listing each exception in its own except clause.

# Empty excepts also raise some design issues, though. Although convenient, they may
# catch unexpected system exceptions unrelated to your code, and they may inadver-
# tently intercept exceptions meant for another handler. For example, even system exit
# calls and Ctrl-C key combinations in Python trigger exceptions, and you usually want
# these to pass. 

# Python 3.X more strongly supports an alternative that solves one of these problems-
# catching an exception named Exception has almost the same effect as an empty
# except, but ignores exceptions related to system exits:
# try:
#     action()
# except Exception:
#     ...                                                              # Catch all possible exceptions, except exits

# In short, it works because exceptions match if they are a subclass of one named
# in an except clause, and Exception is a superclass of all the exceptions
# you should generally catch this way. This form has most of the same convenience of
# the empty except, without the risk of catching exit events.

# Without else, there is no direct way to tell (without setting and checking
# Boolean flags) whether the flow of control has proceeded past a try statement because
# no exception was raised, or because an exception occurred and was handled.

# Much like the way else clauses in loops make the exit cause more apparent, the else
# clause provides syntax in a try that makes what has happened obvious and unambiguous:
# try:
#     ...run code...
# except IndexError:
#     ...handle exception...
# else:
#     ...no exception occurred...

# You can almost emulate an else clause by moving its code into the try block:
#  try:
#      ...run code...
#      ...no exception occurred...
#  except IndexError:
#     ...handle exception...

# This can lead to incorrect exception classifications, though. If the "no exception
# occurred" action triggers an IndexError, it will register as a failure of the try 
# block and erroneously trigger the exception handler below the try (subtle, but true!).
# By using an explicit else clause instead, you make the logic more obvious and guarantee
# that except handlers will run only for real failures in the code you're wrapping in a
# try, not for failures in the else no-exception case's action.

def kaboom(x, y):
    print(x + y)                                                       # Trigger TypeError
    
try:
    kaboom([0, 1, 2], 'spam')
except TypeError:                                                      # Catch and recover here
    print('Hello world!')
print('resuming here')                                                 # Continue here if exception or not
# Hello world!
# resuming here

print("-" * 20 + "#2 The try/finally Statement" + "-" * 20)

# If an exception does not occur while the try block is running, Python continues 
# to run the finally block, and then continues execution past the try statement.

# If an exception does occur during the try block's run, Python still comes back and
# runs the finally block, but it then propagates the exception up to a previously
# entered try or the top-level default handler; the program does not resume execution
# below the finally clause's try statement. That is, the finally block is run even an
# exception is raised, but unlike an except, the finally does not terminate exception
# it continues being raised after the finally block runs.

# File objects are automatically closed on garbage collection in standard Python
# (CPython). However, it's not always easy to predict when garbage collection will
# occur. The try statement makes file closes more explicit and predictable and
# pertains to a specific block of code. It ensures that the file will be closed on
# block exit, regardless of whether an exception occurs or not.

print("-" * 20 + "#3 Unified try Statement Syntax" + "-" * 20)

# (square brackets mean optional and star means zero-or-more here):

# Format 1

# try:
#     statements
# except [type [as value]]:                                            # [type [, value]] in Python 2.X
#     statements
# [except [type [as value]]:
#     statements]*
# [else:
#     statements]
# [finally:
#     statements]

# Format 2

# try:
#     statements
# finally:
#     statements

# Because of these rules, the else can appear only if there is at least one except,
# and it's always possible to mix except and finally, regardless of whether an else
# appears or not.

sep = '-'*20 + '\n'

print(sep + "EXCEPTION RAISED AND CAUGHT")
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
# except run
# finally run
# after run

print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# finally run
# after run

print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

# else run
# finally run
# after run

print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    #x = 1 / 0
    pass
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')
# finally run
# ZeroDivisionError: integer division or modulo by zero


print("-" * 20 + "#4 The raise Statement" + "-" * 20)

# raise instance                                                       # Raise instance of class
# raise class                                                          # Make and raise instance of class: makes an instance (with no constructor arguments)
# class                                                                # Reraise the most recent exception

# If we pass a class instead, Python calls the class with no constructor
# arguments, to create instance to be raised; this form is equivalent to
# adding parentheses after the class reference. 

# The last form reraises the most recently raised exception; it's commonly
# used in exception handlers to propagate exceptions that have been caught.

# Version skew note: Python 3.X no longer supports the raise Exc, Args
# form that is still available in Python 2.X. In 3.X, use the raise
# Exc(Args) instance-creation call form described in this book instead.

# raise IndexError                                                     # Class (instance created)
# raise IndexError()                                                   # Instance (created in statement)

# We can also create the instance ahead of time-because the raise statement
# accepts any kind of object reference, the following two examples raise
# IndexError just like prior two:

# exc = IndexError()                                                   # Create instance ahead of time
# raise exc

# excs = [IndexError, TypeError]
# raise excs[0]

# When an exception is raised, Python sends the raised instance along with
# the exception. If a try includes an except name as X: clause, the variable
# X will be assigned the instance provided in the raise.

# Once caught by an except clause anywhere in the program, an exception dies
# (i.e., won't propagate to another try), unless it's reraised by another
# raise statement or error.

# In Python 2.X, the exception reference variable name in an except clause
# is not localized to the clause itself, and is available after the associated
# block runs.

import sys

if sys.version_info <= (3, 0):
    try:
        1 / 0
    except Exception as X:                                             # P3,P2: as, P2: also "except Exception, X:"
        print(X)                                                       # integer division or modulo by zero
    
    print(X)                                                           # integer division or modulo by zero

if sys.version_info >= (3, 0):
    try:
        1 / 0
    except Exception as X:
        print(X)
    
    # print(X)                                                         # NameError: name 'X' is not defined

# Unlike compression loop variables, though, this variable is removed after
# the except block exits in 3.X. It does so because it would otherwise retain
# a reference to the runtime call stack, which would defer garbage collection
# and thus retain excess memory space.

X = 99
print({X for X in "spam"})                                             # set(['a', 'p', 's', 'm'])
print(X)                                                               # 99

# If you do need to reference the exception instance after the try statement,
# simply assign it to another name that won't be automatically removed.

if sys.version_info >= (3, 0):

    try: 
        1 / 0
    except Exception as X:                                             # Python removes this reference 
        print(X)                                                       # division by zero
        saveit = X                                                     # Assign exception to retain exception if needed

    # print(X)                                                         # NameError: name 'X' is not defined
    print(saveit)                                                      # division by zero

# Propagating Exceptions with raise

# try:
#     raise IndexError('spam')                                           # Exception remember arguments
# except IndexError:
#     print('propagating')
#     raise                                                              # Reraise most recent exception

# raise IndexError('spam')                                           
# IndexError: spam

print("-" * 20 + "#5 Python 3.X Exception Chaining: raise from" + "-" * 20)

# Exceptions can sometimes be triggered in response to other exceptions-both 
# deliberately and by new program errors. To support full disclosure in such
# cases, Python 3.X (but not 2.X) also allows raise statements to have an 
# optional from clause:
#     raise newexception from otherexception

# When the from is used in an explicit raise request, the expression following 
# from specifies another exception class or instance to attach to the __cause__
# attribute of the new exception being raised. If the raised exception is not
# caught, Python prints both exceptions as part of the standard error message.

if sys.version_info >= (3, 0):

    try:
        1 / 0
    except Exception as E:
        # raise TypeError('Bad') from E                                 # Explicitly chained exception
        pass

# Traceback (most recent call last):
#   File "exceptions_advanced.py", line 326, in <module>
#     1 / 0
# ZeroDivisionError: division by zero

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "exceptions_advanced.py", line 328, in <module>
#     raise TypeError('Bad') from E                                    # Explicitly chained exception
# TypeError: Bad

# Similar effect
    try:
        1 / 0
    except:
        # badname
        pass
    
# Traceback (most recent call last):
#   File "exceptions_advanced.py", line 344, in <module>
#     1 / 0
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "exceptions_advanced.py", line 346, in <module>
#     badname
# NameError: name 'badname' is not defined

# In both cases, because the original exception objects thus attached
# to new exception objects may themselves have attached causes, the
# causality chain can be arbitrary  long, and is displayed in full in
# error messages.

# raise newexception from None

# This allows the display of the chained exception context described in
# the preceding section to be disabled. This makes for less cluttered error
# messages in applications that convert between exception types while
# processing exception chains.

print("-" * 20 + "#6 The assert Statement" + "-" * 20)

# It is mostly just syntactic shorthand for a common raise usage pattern,
# and an assert can be thought of as a conditional raise statement. 
# A statement of the form:

# assert test, data                                                    # The data part is optional    

# works like the following code:
# if __debug__:
#     if not test:
#         raise AssertionError(data)

# In other words, if the test evaluates to false, Python raises an exception:
# the data item (if it's provided) is used as the exception's constructor 
# argument. Like all exceptions, the AssertionError exception will kill your
# program if it's not caught with a try, in which case the data item shows up
# as part of the standard error message.

# As an added feature, assert statements may be removed from a compiled prog-
# ram's byte code if the -O Python command-line flag is used, thereby optimi-
# zing the program. AssertionError is a built-in exception, and the __debug__
# flag is a built-in name that is automatically set to True unless the -O flag
# is used. Use a command line like python -O main.py to run in optimized mode
# and disable (and hence skip) asserts.

def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

# It's important to keep in mind that assert is mostly intended for trapping
# user-defined constraints, not for catching genuine programming errors. Be-
# cause Python traps programming errors itself, there is usually no need to
# code assert to catch things like out-of-bounds indexes, type mismatches,
# and zero divides.

def reciprocal(x):
    assert x != 0                                                      # A generally useless assert    
    return 1 / x                                                       # Python checks for ro automatically

# Such assert use cases are usually superfluous-because Python raises excep-
# tions on errors automatically, you might as well let it do the job for you.
# As a rule, you don't need to do error checking explicitly in your own code.


print("-" * 20 + "#7 with/as Context Managers" + "-" * 20)

# This statement is designed to work with context manager objects, which sup-
# port a new method-based protocol, similar in spirit to the way that iteration
# tools work with methods of the iteration protocol. 

# The with/as statement is designed to be an alternative to a common try/finally
# usage idiom; like that statement, with is in large part intended for specifying
# termination-time or "cleanup" activities that must run regardless of whether an
# exception occurs during a processing step.

# Unlike try/finally, the with statement is based upon an object protocol for
# specifying actions to be run around a block of code. This makes 'with' less 
# general, qualifies it as redundant in termination roles, and requires coding
# classes for objects that do not support its protocol. On the other hand, 'with'
# also handles entry actions, can reduce code size, and allows code contexts to
# be managed with full OOP.

# with expression [as variable]                                        # variable is optional
#     with-block

# The expression here is assumed to return an object that supports the context
# management protocol (more on this protocol in a moment). This object may also
# return a value that will be assigned to the name variable if the optional as
# clause is present.

# Note that the variable is not necessarily assigned the result of the expres-
# sion; the result of the expression is the object that supports the context
# protocol, and the variable may be assigned something else intended to be used
# inside the statement. The object returned by the expression may then run star-
# tup code before the with-block is started, as well as termination code after
# the block is done, regardless of whether the block raised an exception or not.

# File objects have a context manager that automatically closes the file after
# the with block regardless of whether an exception is raised, and regardless
# of if or when the version of Python running the code may close automatically.

# with open(r'C:\misc\data') as myfile:
#     for line in myfile:
#         print(line)
#         ...more code here...

# Here, the call to open returns a simple file object that is assigned to the name
# myfile. We can use myfile with the usual file tools. However, this object also 
# supports the context management protocol used by the with statement. After this
# with statement has run, the context management machinery guarantees that the fi-
# le object referenced by myfile is automatically closed, even if the for loop rai-
# sed an exception while processing the file.

# Although file objects may be automatically closed on garbage collection, it's
# not always straightforward to know when that will occur, especially when using
# alternative Python implementations. The with statement in this role is an alter-
# native that allows us to be sure that the close will occur after execution of a
# specific block of code.

# We can achieve the same result with try/finally statement.

# Another example of with is 
 
#     lock = threading.Lock()
#     with lock:
#     # critical section of code
#     ...access shared resources...

# Here, the context management machinery guarantees that the lock is automatically
# acquired before the block is executed and released once the block is complete,
# regardless of exception outcomes.

print("-" * 20 + "#8 The Context Management Protocol" + "-" * 20)

# Here's how the with statement actually works:

# 1. The expression is evaluated, resulting in an object known as a context 
# manager that must have __enter__ and __exit__ methods.

# 2. The context manager's __enter__ method is called. The value it returns
# is assigned to the variable in the as clause if present, or simply discarded
# otherwise.

# 3. The code in the nested with block is executed.

# 4. If the with block raises an exception, the __exit__(type, value, traceback)
# method is called with the exception details. These are the same three values
# returned by sys.exc_info, described in the Python manuals and later in this 
# part of the book. If this method returns a false value, the exception is 
# reraised; otherwise, the exception is terminated. The exception should normally
# be reraised so that it is propagated outside the with statement.

# 5. If the with block does not raise an exception, the __exit__ method is still
# called, but its type, value, and traceback arguments are all passed in as None.

class TraceBlock:
    
    def message(self, arg):
        print('running ' + arg)
        
    def __enter__(self):
        print('starting with block')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally')
        else:
            print('raise an exception! ' + str(exc_type))
            return True                                             # Don't propagate the exception
    
if __name__ == '__main__':
    
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')
    
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')

# starting with block
# running test 1
# reached
# exited normally

# starting with block
# running test 2
# raise an exception! <type 'exceptions.TypeError'>

# Notice that this class's __exit__ method returns False to propagate the
# exception; deleting the return statement would have the same effect, as
# the default None return value of functions is False by definition. Also
# notice that the __enter__ method returns self as the object to assign to
# the as variable; in other use cases, this might return a completely diffe-
# rent object instead. (In my case __exit__ returns True to not propagate
# the exception).

# There's a new contextlib standard module that provides additional tools
# for coding context managers).

print("-" * 20 + "#9 Multiple Context Managers in 3.1, 2.7, and Later" + "-" * 20)

# Any number of context manager items may be listed, and multiple items work
# the same as nested with statements. In Pythons that support this (3.1, 2.7),
# the following code:

# with A() as a, B() as b:
#     ...statements...

# is equivalent to the following, which also works in 3.0 and 2.6:

# with A() as a:
#     with B() as b:
#         ...statements...

# Line-by-line comparison of two text files

# with open('script1.py') as f1, open('script2.py') as f2:
#     for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
#         if line1 != line2:
#             print('%s\n%r\n%r' % (linenum, line1, line2))


