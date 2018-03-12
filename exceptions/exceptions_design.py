

# MAIN SOURCE:

# Lutz, "Learning Python" Chapter 36


# USEFUL LINKS:


# GENERAL INFORMATION:

print("-" * 20 + "# 1 Nesting Exception Handlers" + "-" * 20)

# When an exception is raised, Python returns to the most recently
# entered try statement with a matching except clause. Because each
# try statement leaves a marker, Python can jump back to earlier
# trys by inspecting the stacked markers. This nesting of active
# handlers is what we mean when we talk about propagating exceptions
# up to "higher" handlers-such handlers are simply try statements
# entered earlier in the program's execution flow.

# TRY-EXCEPT

# When an exception is eventually raised, Python jumps back to the
# most recently entered try statement that names that exception,
# runs that statement's except clause, and then resumes execution
# after that try.

# Once the exception is caught, its life is over-control does not
# jump back to all matching trys that name the exception; only the
# first (i.e., most recent) one is given the opportunity to handle it.

# TRY-FINALLY

# By contrast, when try statements that contain only finally clauses
# are nested, each finally block is run in turn when an exception
# occurs-Python continues propagating the exception up to other 
# trys, and eventually perhaps to the top-level default handler.

# The finally clauses do not kill the exception-they just specify
# code to be run on the way out of each try during the exception
# propagation process. If there are many try/finally clauses active
# when an exception occurs, they will all be run, unless a try/except
# catches the exception somewhere along the way.

# The propagation of an exception essentially proceeds backward
# through time to try statements that have been entered but not
# yet exited. This propagation stops as soon as control is unwound
# to a matching except clause, but not as it passes through finally
# clauses on the way.

# There are control-flow nesting and syntactic nesting

# EXAMPLE: Control-Flow Nesting

# The place where an exception winds up jumping to depends on the
# control flow through the program at runtime. Because of this, to
# know where you will go, you need to know where you've been. In
# this case, where exceptions are handled is more a function of 
# control flow than of statement syntax.

def action2():
    print(1 + [])                                               # Generate TypeError

def action1():
    try:
        action2() 
    except TypeError:                                           # Most recent matching try
        print('inner try')
        
try:
    action1()
except TypeError:                                               # Here, only if action1 re-raises
    print('outer try')

# OUTPUT:
# inner try

print('-----')


# EXAMPLE: Syntactic Nesting

# The only difference is that the nested handlers are physically
# embedded in a try block, not coded elsewhere in functions that
# are called from the try block.

def raise1(): raise IndexError
def noraise(): return
def raise2(): raise SyntaxError

try:

    for func in (raise1, noraise, raise2):
        print('<%s>' % func.__name__)
        try:
            try:
                func()
            except IndexError:
                print('caught IndexError')
        finally:
            print('finally run')
        print('...')

except:
    print('so not to close the script')

# OUTPUT:
# <raise1>
# caught IndexError
# finally run
# ...
# <noraise>
# finally run
# ...
# <raise2>
# finally run 
# ...
# so not to close the script

print("-" * 20 + "# 2 Exception Idioms" + "-" * 20)

print("-" * 20 + "# 2.1 Breaking Out of Multiple Nested Loops: 'go to'" + "-" * 20)

# Exceptions can often be used to serve the same roles as other
# languages' "go to" statements to implement more arbitrary control
# transfers. Exceptions, however, provide a more structured option
# that localizes the jump to a specific block of nested code.

# In this role, raise is like "go to," and except clauses and exception
# names take the place of program labels. You can jump only out of
# code wrapped in a try this way, but that's a crucial feature -
# truly arbitrary "go to" statements can make code extraordinarily
# difficult to understand and maintain.

# Python's break statement exits just the single closest enclosing 
# loop, but we can always use exceptions to break out of more than
# one loop level if needed.

class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop                        # Break exits just one level         
                print('loop3: %s' % i)
            print('loop2')
        print('loop2')
except Exitloop:
    print('continuing')                                         # Or just pass to move on
print('i = %s' % i)


# OUTPUT:
# loop3: 0
# loop3: 1
# loop3: 2
# loop3: 3
# continuing
# i = 4

# If you change the raise in this to break, you'll get an infinite loop.

# Variable assignments made in a try are not undone in general, though
# as we've seen, exception instance variables listed in except clause
# headers are localized to that clause, and the local variables of any
# functions that are exited as a result of a raise are discarded.

print("-" * 20 + "# 2.2 Exceptions Aren't Always Errors" + "-" * 20)

# In Python, all errors are exceptions, but not all exceptions are errors.
# raw_input in 2.X-reads a line of text from the standard input stream, 
# sys.stdin, at each call and raises the built - in EOFError at end-of-file.
# So it's not an error.

# while True:
#     try:
#         line = input()                                          # Read line from stdin (raw_input in 2.X)
#     except EOFError:
#         break                                                   # Exit loop at end-of-file
#     else:
#         ...process next line here...

print("-" * 20 + "# 2.3 Functions Can Signal Conditions with raise" + "-" * 20)

# User-defined exceptions can also signal nonerror conditions. For instance,
# a search routine can be coded to raise an exception when a match is found
# instead of returning a status flag for the caller to interpret. 

# class Found(Exception): pass
#
# def searcher():
#     if ...success...
#         raise Found()                                           # Raise exceptions instead of returning flags
#     else:
#         return
# try: 
#     searcher()
# except Found:                                                   # Exception if item was found 
#     ...success...
# else:                                                           # else returned: not found
#     ...failure...

# May also be useful for any function that cannot return a sentinel value to
# designate success or failure - it's impossible for any return value to signal
# a failure condition. Exceptions provide a way to signal results without a
# return value

# class Failure(Exception): pass
# 
# def searcher():
#     if ...success...:
#         return ...founditem...
#     else:
#         raise Failure()
#     
# try:
#     item = searcher()
# except Failure:
#     ...not found...
# else:
#     ...use item here...

# Because Python is dynamically typed and polymorphic to the core, exceptions,
# rather than sentinel return values, are the generally preferred way to signal
# such conditions.

print("-" * 20 + "# 2.4 Closing Files and Server Connections" + "-" * 20)

# Exception processing tools are also commonly used to ensure that system
# resources are finalized, regardless of whether an error occurs during
# processing or not. For example, some servers require connections to be
# closed in order to terminate a session. Similarly, output files may require
# close calls to flush their buffers to disk for waiting consumers, and
# input files may consume file descriptors if not closed; although file
# objects are automatically closed when garbage-collected if still open, in
# some Pythons it may be difficult to be sure when that will occur.

# The most general and explicit way to guarantee termination actions for
# a specific block of code is the try/finally statement

# myfile = open(r'C:\code\textdata', 'w')
# try:
#     ...process myfile...
# finally:
#     myfile.close()

# Some objects make this potentially easier in Python 2.6, 3.0, and later
# by providing context managers that terminate or close the objects for 
# us automatically when run by the with/as statement.

# with open(r'C:\code\textdata', 'w') as myfile:
#     ...process myfile...

# Compared to the traditional try/finally, context managers are more
# implicit, which runs contrary to Python's general design philosophy.
# Context managers are also arguably less general - they are available
# only for select objects, and writing user-defined context managers
# to handle general termination requirements is more complex than coding
# a try/finally.

# The context manager protocol supports entry actions in addition to
# exit actions and requires less code when contex manager is already
# implemented.

# myfile = open(filename, 'w')                                    # Traditional form
# ...process myfile...
# myfile.close()

# with open(filename) as myfile:                                  # Context manager form
#     ...process myfile...

print("-" * 20 + "# 2.5 Debugging with Outer try Statements" + "-" * 20)

print("-" * 20 + "# 2.6 Running In-Process Tests" + "-" * 20)

print("-" * 20 + "# 2.7 More on sys.exc_info" + "-" * 20)

# The sys.exc_info result used in the last two sections allows an
# exception handler to gain access to the most recently raised
# exception generically. This is especially useful when using the
# empty except clause to catch everything blindly, to determine 
# what was raised:
# try:
#     ...
# except:
#     sys.exc_info()[0:2] are the exception class and instance

# If no exception is being handled, this call returns a tuple
# containing three None values. Otherwise, the values returned
# are (type, value, traceback), where:
# - type is the exception class of the exception being handled.
# - value is the exception class instance that was raised.
# - traceback is a traceback object that represents the call
#   stack at the point where the exception originally occurred

print("-" * 20 + "# 2.7 Displaying Errors and Tracebacks" + "-" * 20)

# import traceback

# Write traceback to a file

print("-" * 20 + "# 3 Exception Design Tips and Gotchas" + "-" * 20)

# The real art behind them is in deciding how specific or 
# general your except clauses should be and how much code
# to wrap up in try statements.

print("-" * 20 + "# 3.1 What Should Be Wrapped" + "-" * 20)

# What to wrap is really a design issue that goes beyond the
# language itself, and it will become more apparent with use.
# But for now, here are a few rules of thumb:
#
# - Operations that commonly fail should generally be wrapped
#   in try statements. For example, operations that interface
#   with system state (file opens, socket calls, and the like)
#   are prime candidates for try.
#
# - However, there are exceptions to the prior rule-in a simple
#   script, you may want failures of such operations to kill
#   your program instead of being caught and ignored.  This is
#   especially true if the failure is a showstopper. Failures
#   in Python typically result in useful error messages (not
#   hard crashes), and this is the best outcome some programs
#   could hope for.
#
# - You should implement termination actions in try/finally
#   statements to guarantee their execution, unless a context
#   manager is available as a with/as option. The try/finally
#   statement form allows you to run code whether exceptions
#   occur or not in arbitrary scenarios.

# - It is sometimes more convenient to wrap the call to a large
#   function in a single try statement, rather than littering 
#   the function itself with many try statements.

print("-" * 20 + "# 3.2 Catching Too Much: Avoid Empty except and Exception" + "-" * 20)

# As mentioned, exception handler generality is a key design choice.
# Python lets you pick and choose which exceptions to catch, but you
# sometimes have to be careful to not be too inclusive. For example,
# you've seen that an empty except clause catches every exception
# that might be raised while the code in the try block runs.

# That's easy to code, and sometimes desirable, but you may also wind
# up intercepting an error that's expected by a try handler higher up
# in the exception nesting structure. For example, an exception handler
# such as the following catches and stops every exception that reaches
# it, regardless of whether another handler is waiting for it

# def func():
#     try:
#         ...                                                     # IndexError is raised in here
#     except:
#         ...                                                     # But everything comes here and dies!
#
# try:
#     func()
# except IndexError:
#     ...                                                         # Exception should be processed here

# Perhaps worse, such code might also catch unrelated system exceptions.
# Same code as above may cause also big problems if sys.exit(40) [critical
# error] is ignored by "except:"

# You simply might not expect all the kinds of exceptions that could
# occur during an operation. Using the built-in exception classes of
# the prior chapter can help in this particular case, because the
# Exception superclass is not a superclass of SystemExit

# import sys
# def bye():
#     sys.exit(40)                                                # Crucial error: abort now!

#
# try:
#     bye()
# except Exception:                                               # Won't catch exits, but will catch many others
#     ... 

# In other cases, though, this scheme is no better than an empty except
# clause-because Exception is a superclass above all built-in exceptions
# except system-exit events, it still has the potential to catch exceptions
# meant for elsewhere in the program.

# IMPORTANT: probably worst of all, both using an empty except and catching
# the Exception superclass will also catch genuine programming errors,
# which should be allowed to pass most of the time.

# IMPORTANT: As a rule of thumb, be as specific in your handlers as you can
# be - empty except clauses and Exception catchers are handy, but potentially
# error-prone. 

# mydictionary = {...}
# ...
# try:
#     x = myditctionary['spam']                                   # Oops: misspelled 
# except:
#     x = None                                                    # Assume we got KeyError
# ...continue here with x...                     

# The coder here assumes that the only sort of error that can happen when
# indexing a dictionary is a missing key error. But because the name 
# myditctionary is misspelled (it should say mydictionary), Python raises
# a NameError instead for the undefined name reference, which the handler
# will silently catch and ignore. The event handler will incorrectly fill
# in a None default for the dictionary access, masking the program error.

# Moreover, catching Exception here will not help-it would have the exact
# same effect as an empty except. You would be better off saying except
# KeyError: to make your intentions explicit and avoid intercepting unrelated
# events.

print("-" * 20 + "# 3.3 Catching Too Little: Use Class-Based Categories" + "-" * 20)

# On the other hand, neither should handlers be too specific. When you
# list specific exceptions in a try, you catch only what you actually list.
# This isn't necessarily a bad thing, but if a system evolves to raise other
# exceptions in the future, you may need to go back and add them to exception
# lists elsewhere in your code.

# The following handler is written to treat MyExcept1 and MyExcept2 as
# normal cases and everything else as an error. If you add a MyExcept3
# in the future, though, it will be processed as an error unless you
# update the exception list.

# try:
#     ...
# except (MyExcept1, MyExcept2):                                  # Breaks if you add a MyExcept3 later
#     ...                                                         # Nonerrors
# else:
#     ...                                                         # Assumed to be an error

# If you catch a general superclass, you can add and raise more specific
# subclasses in the future without having to extend except clause lists
# manually-the superclass becomes an extendible exceptions category.

# try:
#     ...
# except SuccessCategoryName:                                     # OK if you add a MyExcept3 subclass later 
#     ...                                                         # Nonerrors
# else:
#     ...                                                         # Assumed to be an error

# The moral of the story is to be careful to be neither too general nor
# too specific in exception handlers, and to pick the granularity of your
# try statement wrappings wisely. Especially in larger systems, exception
# policies should be a part of the overall design




