
# Some good links
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time



print('-' * 10 + "A.1. Data hiding: _X and __all__" + '-' * 10)

# As we've seen, a Python module exports all the names assigned at the top level of its
# file. There is no notion of declaring which names should and shouldn't be visible 
# outside the module.

# As a special case, you can prefix names with a single underscore (e.g., _X) to prevent
# them from being copied out when a client imports a module's names with a fromstatement.

# Underscores aren't "private" declarations: you can still see and change such names with
# other import forms, such as the import statement

from import_files.simple_8 import *

print(a, c)                           # (1, 3) 
# print(_b)                           # NameError: name '_b' is not defined

import import_files.simple_8

print(import_files.simple_8._b)       # 2

# Alternatively, you can achieve a hiding effect similar to the _X naming convention by
# assigning a list of variable name strings to the variable __all__ at the top level of the
# module. When this feature is used, the from * statement will copy out only those names
# listed in the __all__ list. In effect, this is the converse of the _X convention: __all__
# identifies names to be copied, while _X identifies names not to be copied.

from import_files.simple_9 import *

print(e, _f)                          # (5, 6)
# print(g)                            # NameError: name 'g' is not defined
# print(_h)                           # NameError: name '_h' is not defined

from import_files.simple_9 import e, _f, g, _h

print(e, _f, g, _h)                   # (5, 6, 7, 8)

import import_files.simple_9           
print(import_files.simple_9.e)        # 5
print(import_files.simple_9._f)       # 6
print(import_files.simple_9.g)        # 7
print(import_files.simple_9._h)       # 8

# Like the _X convention, the __all__ list has meaning only to the from * statement form
# and does not amount to a privacy declaration: other import statements can still access
# all names

print('-' * 10 + "A.2. Mixed Usage Modes: __name__ and __main__" + '-' * 10)

# This trick lets you both import a file as a module and run it as a
# standalone program, and is widely used in Python files. Each module has a built-in
# attribute called __name__, which Python creates and assigns automatically as follows:
# - If the file is being run as a top-level program file, __name__ is set to the string
#   "__main__" when it starts.
# - If the file is being imported instead, __name__ is set to the module's name as known
#   by its clients (if import_files.simple_a then __name__ == "import_files.simple_a"

import import_files.simple_a          # Nothing
import_files.simple_a.tester()        # It's Christmas Time

# python simple_a.py                  # It's Christmas Time

# In effect, a module's __name__ variable serves as a usage mode flag, allowing its code to
# be leveraged as both an importable library and a top-level script.

# For instance, perhaps the most common way you'll see the __name__ test applied is for
# self-test code. In short, you can package code that tests a module's exports in the module
# itself by wrapping it in a __name__ test at the bottom of the file. This way, you can use
# the file in clients by importing it, but also test its logic by running it from the system
# shell or via another launching scheme.

# In addition, the __name__ trick is also commonly used when you're writing files that
# can be used both as command-line utilities and as tool libraries. For instance, suppose
# you write a file-finder script in Python. You can get more mileage out of your code if
# you package it in functions and add a __name__ test in the file to automatically call those
# functions when the file is run standalone. 

print('-' * 10 + "A.3. Dual mode code" + '-' * 10)

# Check simple_b.py - important programming techniques for
# __name__, unit tests and string formatting

# python simple_b.py - start unit tests
# python simple_b.py 1214325.1241 15
# $    1,214,325.1

print('-' * 10 + "A.4. Changing the module search path" + '-' * 10)

# Python program itself can actually change the search path by changing the built-in

# sys.path settings endure for only as long as the Python session 
# or program (technically, process) that made them runs; they are not retained after
# Python exits. By contrast, PYTHONPATH and .pth file path configurations live in the
# operating system instead of a running Python program, and so are more global: they are
# picked up by every program on your machine and live on after a program completes.

import sys
print(sys.path)
# sys.path = []                         # clear sys.path
# import string                         # ImportError: No module named string - Python doesn't know where to find the module
 
print('-' * 10 + "A.4. The 'as' extension for import and from" + '-' * 10)

# import modulename as name             # And use name, not modulename

# is equivalent to

# import modulename
# name = modulename
# del modulename                        # Don't keep original name

# This works in a from statement
# from modulename import attrname as name

# This extension is commonly used to provide short synonyms for longer
# names, and to avoid name clashes when you are already using a name
# in your script that would otherwise be overwritten by a normal import statement

# import reallylongmodulename as name   # Use shorter nickname
# name.func()

# from module1 import utility as util1  # Can have only 1 "utility"
# from module2 import utility as util2
# util1(); util2()

# It also comes in handy for providing a short, simple name for an entire directory path
# and avoiding name collisions when using the package import

# import dir1.dir2.mod as mod                # Only list full path once 
# mod.func()

# from dir1.dir2.mod import func as modfunc  # Rename to make unique if needed 
# modfunc()

print('-' * 10 + "A.5. getattr" + '-' * 10)

# attr = module.__dict__[0]
# print(getattr(module, attr))

print('-' * 10 + "A.6. Importing Modules by Name String: exec, __import__ etc" + '-' * 10)

# import 'string'                       # SyntaxError: invalid syntax

# Here, Python will try to import a file x.py, not the string module-the name in an
# import statement both becomes a variable assigned to the loaded module and identifies
# the external file literally.

x = 'string'
# import x                              # ImportError: No module named x

# Most generatl approach is to use exec()
# For explanation of exec() vs eval()
# https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python

# eval accepts only a single expression, exec can take a code block

# An expression in Python is whatever you can have as the value in a variable assignment:
# a_variable = (anything you can put within these parentheses is an expression)
# eval returns the value of the given expression, whereas exec ignores
# the return value from its code, and always returns None

a = 5
rv = eval('37 + a')                       # it is an expression
print(rv)                                 # 42
# rv = exec('37 + a')                     # doesn't work in Python 2.X, in 3.X returns None
exec('a = 47')                            # modify a global variable as a side effect
print(a)                                  # 47
# eval('a = 47')                          # SyntaxError: invalid syntax - you cannot evaluate a statement

modname = 'string'
exec('import ' + modname)
print(string)                             # <module 'string' from '/usr/lib/python2.7/string.pyc'> 

# The only real drawback to exec here is that it must compile the import statement each
# time it runs, and compiling can be slow.

# In most cases it's probably simpler and may run quicker to use the built-in
# __import__ function to load from a name string instead. The effect is similar, 
# but __import__ returns the module object, so assign it to a name here to keep it

modname = 'string'
string = __import__(modname)              # <module 'string' from '/usr/lib/python2.7/string.pyc'>
print(string)

# The newer call importlib.import_module does the same work, and is generally preferred
# in more recent Pythons for direct calls to import by
# name string - at least per the current "official" policy stated in Python's manuals

import importlib
modname = 'string'
string = importlib.import_module(modname)
print(string)                             # <module 'string' from '/usr/lib/python2.7/string.pyc'>

# When you reload a module, though, Python reloads only that particular module's file; 
# it doesn't automatically reload modules that the file being reloaded happens to import.

# A.py
# import C                                # Not reloaded when A is!
# import B                                # Just an import of an already loaded module: no-ops

# from imp import reload
# reload(A)

print('-' * 10 + "A.7. Recursive reload" + '-' * 10)

# Later

print('-' * 10 + "A.8. Module gotchas" + '-' * 10)

# MODULE NAMES CLASH: PACKAGE AND PACKAGE-RELATIVE IMPORTS:

# If you have two modules of the same name, you may only be able to import one of them
# - by default, the one whose directory is leftmost in the sys.path module search path
# will always be chosen. 

# To fix, either avoid using the same name as another module you need or store your
# modules in a package directory and use Python 3.X's package-relative import model,
# available in 2.X as an option. 

# STATEMENT ORDER MATTERS IN TOP-LEVEL CODE:

# Code at the top level of a module file (not nested in a function) runs as soon as
# Python reaches it during an import; because of that, it cannot reference names
# assigned lower in the file.

# Code inside a function body doesn't run until the function is called; because names
# in a function aren't resolved until the function actually runs, they can usually 
# reference names anywhere in the file.

# Generally, forward references are only a concern in top-level module code that executes
# immediately; functions can reference names arbitrarily. Here's a file that illustrates
# forward reference dos and don'ts (https://www.cs.auckland.ac.nz/references/unix/digital/AQTLTBTE/DOCU_024.HTM)

# func1()                                 # NameError: name 'func1' is not defined             

def func1():
    print(func2())
    
# func1()                                 # NameError: global name 'func2' is not defined

def func2():
    return "Hello"

func1()                                   # Hello

# Mixing defs with top-level code is not only difficult to read, it's also dependent on
# statement ordering. As a rule of thumb, if you need to mix immediate code with defs,
# put your defs at the top of the file and your top-level code at the bottom. That way,
# your functions are guaranteed to be defined and assigned by the time Python runs the
# code that uses them.

# FROM COPIES NAMES BUT DOESN'T LINK

# nested1.py
# X = 99
# def printer(): print(X)

# If we import its two names using from in another module, nested2.py, we get copies of
# those names, not links to them. Changing a name in the importer resets only the binding
# of the local version of that name, not the name in nested1.py

# nested2.py
# from nested1 import X, printer          # Copy names out
# X = 88                                  # Changes my "X" only! 
# printer()                               # nested1's X is still 99

# python nested2.py
# 99

# If we use import to get the whole module and then assign to a qualified name, however,
# we change the name in nested1.py.

# nested3.py
# import nested1                          # Get module as a whole
# nested1.X = 88                          # OK: change nested1's X
# nested1.printer()

# python nested3.py
# 88

# FROM * CAN OBSCURE THE MEANING OF VARIABLES

# Because you don't list the variables you want when using the from module import * statement
# form, it can accidentally overwrite names you're already using in your scope.

# For example, if you use from * on three modules in the following, you'll have no way
# of knowing what a raw function call really means

# from module1 import *                   # Bad: may overwrite my names silently
# from module2 import *                   # Worse: no way to tell what we get!
# from module3 import *
# func()                                  # Huh??? From what module is the function here?

# The solution again is not to do this: try to explicitly list the attributes you want in your
# from statements, and restrict the from * form to at most one imported module per file.

# RELOAD MAY NOT IMPACT FROM IMPORTS

# Because from copies (assigns) names when run, there's no link back to the modules where 
# the names came from. Because of this behavior, reloading the importee has no effect on 
# clients that import its names using from. That is, the client's names will still reference
# the original objects fetched with from, even if the names in the original module are
# later reset

# from module import X                    # X may not reflect any module reloads!
# from imp import reload
# reload(module)                          # Changes module, but not my names
# X                                       # Still references old object
     
# To make reloads more effective, use import and name qualification instead of from.
# Because qualifications always go back to the module, they will find the new bindings
# of module names after reloading has updated the module's content in place

# import module                           # Get module, not names
# from imp import reload
# reload(module)                          # Changes module in place
# module.X                                # Get current X: reflects module reloads

# RELOAD, FROM AND INTERACTIVE TESTING

# from module import function
# function(1, 2, 3)

# To truly reload 'function' a lot of work has to be done

# from imp import reload
# import module
# reload(module)
# from module import function             # Or give up and use module.function()
# function(1, 2, 3)

# There are problems inherent in using reload with from: not only do you
# have to remember to reload after imports, but you also have to remember 
# to rerun your from statements after reloads. 

