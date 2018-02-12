
# MAIN SOURCE:
# Lutz


# USEFUL LINKS:


# GENERAL INFORMATION:

# Both built-in and user-defined exceptions are identified by class instance
# objects. This is what is raised and propagated along by exception processing,
# and the source of the class matched against exceptions named in try statements.

# Can be organized into categories. Exceptions coded as classes support future
#changes by providing categories-adding new exceptions in the future won't gen-
# erally require changes in try statements.

# Have state information and behavior. Exception classes provide a natural place
# for us to store context information and tools for use in the try handler-
# instances have access to both attached state information and callable methods.

# Support inheritance. Class-based exceptions can participate in inheritance 
# hierarchies to obtain and customize common behavior-inherited display methods,
# for example, can provide a common look and feel for error messages.

print("-" * 20 + "#1 Coding Exceptions Classes" + "-" * 20)

# Class exceptions are matched by superclass relationships: the raised exception
# matches an except clause if that except clause names the exception instance's 
# class or ANY SUPERCLASS of it.

# That is, when a try statement's except clause lists a superclass, it catches
# instances of that superclass, as well as instances of all its subclasses lower
# in the class tree. The net effect is that class exceptions naturally support
# the construction of exception hierarchies: superclasses become category names,
# and subclasses become specific kinds of exceptions within a category. By naming
# a general exception superclass, an except clause can catch an entire category 
# of exceptions-any more specific subclass will match.

# In addition to this category idea, class-based exceptions better support excep-
# tion state information (attached to instances) and allow exceptions to partici-
# pate in inheritance hierarchies (to obtain common behaviors). 

# Handlers that catch General will also catch any subclasses of it, including
# Specific1 and Specific2

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()                                                # Raise superclass instance
    raise X

def raiser1():
    X = Specific1()                                              # Raise subclass instance
    raise X

def raiser2():
    X = Specific2()                                              # Raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:                                              # Match General or any subclass of it
        import sys
        print('caught: %s' % sys.exc_info()[0])
        
# caught: <class '__main__.General'>
# caught: <class '__main__.Specific1'>
# caught: <class '__main__.Specific2'>  

# If we list a class name without parentheses in a raise, Python calls the
# class with no constructor argument to make an instance for us.

# The exception handler here uses the sys.exc_info call-it's how we can grab
# hold of the most recently raised exception in a generic fashion. Briefly,
# the first item in its result is the class of the exception raised, and the
# second is the actual instance raised.

print("-" * 20 + "#2 Why Exception Hierarchies?" + "-" * 20)

# For small programs we can list all exceptions
# try:
#     func()
# except (General, Specific1, Specific2):
#     ...

# For large or high exception hierarchies, however, it may be easier to
# catch categories using class-based categories than to list every member
# of a category in a single except clause. Perhaps more importantly, you
# can extend exception hierarchies. Perhaps more importantly, you can 
# extend exception hierarchies as software needs evolve by adding new 
# subclasses without breaking existing code.

# If we have in the library:

# import mathlib 
# class Divzero(Exception): pass
# class Oflow(Exception): pass

# we can use it like:

# try:
#     mathlib.func(...)
# except (mathlib.Divzero, mathlib.Oflow):
#    ...handle and recover...

# If we need to add another extension to the library:

# class Divzero(Exception): pass
# class Oflow(Exception): pass
# class Uflow(Exception): pass

# we need to fix all the CLIENT CODE:

# try:
#     mathlib.func(...)
# except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
#    ...handle and recover...

# Class exception hierarchies fix this dilemma completely. Rather than
# defining your library's exceptions as a set of autonomous classes, 
# arrange them into a class tree with a common superclass to encompass
# the entire category:

# class NumErr(Exception): pass
# class Divzero(NumErr): pass
# class Oflow(NumErr): pass

# This way, users of your library simply need to list the common
# superclass (i.e., category) to catch all of your library's exceptions,
# both now and in the future.

# import mathlib
# try:
#     mathlib.func(...)
# except mathlib.NumErr:
#     ...report and recover...

print("-" * 20 + "#3 Built-in Exception Classes" + "-" * 20)

# Python organizes the built-in exceptions into a hierarchy, to
# support a variety of catching modes. 

# In Python 3.X, all the familiar exceptions you've seen (e.g., SyntaxError)
# are really just predefined classes, available as built-in names in the 
# module named builtins; in Python 2.X, they instead live in __builtin__ and
# are also attributes of the standard library module exceptions.

# BaseException: topmost root, printing and constructor defaults
# The top-level root superclass of exceptions. This class is not supposed
# to be directly inherited by user-defined classes (use Exception instead).

# Exception: root of user-defined exceptions
# The top-level root superclass of application-related exceptions. This is
# an immediate subclass of BaseException and is a superclass to every other
# built-in exception, except the system exit event classes (SystemExit, 
# KeyboardInterrupt, and GeneratorExit). Nearly all user-defined classes
# should inherit from this class, not BaseException. When this convention
# is followed, naming Exception in a try statement's handler ensures that
# your program will catch everything but system exit events, which should
# normally be allowed to pass.

# ArithmeticError: root of numeric errors
# A subclass of Exception, and the superclass of all numeric errors. Its
# subclasses identify specific numeric errors: OverflowError, ZeroDivision-
# Error, and FloatingPointError.

# LookupError: root of indexing errors
# A subclass of Exception, and the superclass category for indexing errors
# for both sequences and mappings - IndexError and KeyError.

# Because Exception is the superclass of all application-level exceptions in
# Python 3.X, you can generally use it as a catchall-the effect is much like
# an empty except, but it allows system exit exceptions to pass and propagate
# as they usually should:

# try:
#     action()
# except Exception:                                              # Exits not caught here      
#     ...handle all application exceptions...
# else:
#     ...handle no-exception case...

# This doesn't quite work universally in Python 2.X, however, because
# standalone user-defined exceptions coded as classic classes are not
# required to be subclasses of the Exception root class. 

print("-" * 20 + "#4 Default Printing and State" + "-" * 20)

# raise IndexError                                               # Same as IndexError(): no arguments
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# IndexError

# raise IndexError('spam')                                       # Constructor argument attached, printed
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# IndexError: spam

I = IndexError('spam') 
print(I.args)                                                    # ('spam',)
print(I)                                                         # spam

# The same holds true for user-defined exceptions in Python 3.X (and 
# for new-style classes in 2.X), because they inherit the constructor
# and display methods present in their built-in superclasses.

# When intercepted in a try statement, the exception instance object
# gives access to both the original constructor arguments and the dis-
# play method.

class E(Exception): pass

try:
    raise E('spam')
except E as X:
    print(X)                                                     # spam
    print(X.args)                                                # ('spam',)
    print(repr(X))                                               # E('spam',)
    
    
print("-" * 20 + "#5 Custom Print Displays" + "-" * 20)

class MyBad(Exception):
    def __str__(self):
        return("Always look on the bright side of life ...")
    
try:
    raise MyBad()
except MyBad as X:
    print(X)                                                     # Always look on the bright side of life ...

print("-" * 20 + "#6 Custom Data and Behavior" + "-" * 20)

# It is not generally feasible to store extra details in global
# variables because the try statement might not know which file
# the globals reside in. Passing extra state information along
# in the exception itself allows the try statement to access it
# more reliably.

class FormatError(Exception):
    
    def __init__(self, line, file):
        self.line = line
        self.file = file
        
def parser():
    raise FormatError(42, file='spam.txt')                       # When error found

try:
    parser()
except FormatError as X:
    print("Error at: %s %s" % (X.file, X.line))                  # Error at: spam.txt 42 
    
# The exception class can also define methods to be called
# in the handler.

class FormatError():
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        print("Write Log to logfile")

def oarser():
    raise FormatError(40, 'spam.txt')

if __name__ == '__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()                                           # Write Log to logfile

# Two final notes here: first, the raised instance object
# assigned to exc in this code is also available generically
# as the second item in the result tuple of the sys.exc_info()
# call-a tool that returns information about the most recently
# raised exception.

# Second, although our class's logerror method appends a custom
# message to a logfile, it could also generate Python's standard
# error message with stack trace using tools in the traceback
# standard library module, which uses traceback objects.


