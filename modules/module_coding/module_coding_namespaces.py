


import time


# Modules are just namespaces (places where names are created), and the
# names that live in a module are called its attributes.

# Every name that is assigned a value at the top level of a module file
# (i.e., not nested in a function or class body) becomes an attribute of
# that module. For instance, given an assignment statement such as X = 1
# at the top level of a module file M.py, the name X becomes an attribute
# of M, which we can refer to from outside the module as M.X. 
# The name X also becomes a global variable to other code inside M.py

# - Module statements run on the first import
# - Top-level assignments create module attributes
# - Module namespaces can be accessed via the attribute__dict__ or dir(M)
# --- Module namespaces created by imports are dictionaries
# --- dir() is like __dict__, but is prone to changes
# - Modules are a single scope (local is global)

print('-' * 10 + "A.1. Files Generate Namespaces" + '-' * 10)

import import_files.simple_4
# starting to load...
# done loading.

# Once the module is loaded, its scope becomes an attribute
# namespace in the module object we get back from import.

# Here, sys, name, func, and klass were all assigned while the
# module's statements were being run, so they are attributes 
# after the import.

print(import_files.simple_4.sys)             # <module 'sys' (built-in)>
print(import_files.simple_4.name)            # 42
print(import_files.simple_4.func)            # <function func at 0xb72ee64c>
print(import_files.simple_4.klass)           # import_files.simple_4.klass

print('-' * 10 + "A.2. Namespace Dictionaries: __dict__" + '-' * 10)

# Remember to wrap this in a list call in Python 3.X
# it's a view object there

rv = list(import_files.simple_4.__dict__.keys())
print(rv)
# ['name', '__builtins__', '__file__', '__package__', 'sys', 
#  'klass', 'func', '__name__', '__doc__']

# The names we assigned in the module file become dictionary keys internally, so some
# of the names here reflect top-level assignments in our file. However, Python also adds
# some names in the module's namespace for us; for instance, __file__ gives the name
# __file__ gives the name of the file the module was loaded from
# __name__ gives its name as known to importers

rv = import_files.simple_4.__dict__['__file__']
print(rv)                                      # /home/konstantin/Sphinx/learn_python/modules/module_coding/import_files/simple_4.pyc

rv = import_files.simple_4.__dict__['__name__']
print(rv)                                      # import_files.simple_4

rv = list(name for name in import_files.simple_4.__dict__ if not name.startswith('__'))
print(rv)                                      # ['name', 'sys', 'klass', 'func']

print(import_files.simple_4.name)              # 42
print(import_files.simple_4.__dict__['name'])  # 42

print('-' * 10 + "A.3. Attribute Name Qualification" + '-' * 10)

# In Python, you can access the attributes of any object that has attributes
# using the qualification (a.k.a. attribute fetch) syntax object.attribute.

# The LEGB scope rule applies only to bare, unqualified names- it
# may be used for the leftmost name in a name path, but later names after 
# dots search specific objects instead.

# - Simple variables - X means search for the name X in the current scopes 
#   (following the LEGB rule)
# - Qualification - X.Y means find X in the current scopes, then search for
#   the attribute Y in the object X (not in scopes)

print('-' * 10 + "A.4. Imports versus scopes" + '-' * 10)

# Import operations never give upward visibility to code in imported files -
# an imported file cannot see names in the importing file. More formally:
# - Functions can never see names in other functions, unless they are physically 
#   enclosing.
# - Module code can never see names in other modules, unless they are 
#   explicitly imported.

# Such behavior is part of the lexical scoping notion-in Python, 
# the scopes surrounding a piece of code are completely determined by 
# the code's physical position in your file. Scopes are never influenced 
# by function calls or module imports.

print('-' * 10 + "A.5. Namespace nesting" + '-' * 10)

# In some sense, although imports do not nest namespaces upward, 
# they do nest downward. That is, although an imported module never
# has direct access to names in a file that imports it, using attribute 
# qualification paths it is possible to descend into arbitrarily nested
# modules and access their attributes.
'''
X = 1
import import_files.simple_6

print(X)                                   # 1
print(import_files.simple_6.X)             # 2
print(import_files.simple_6.simple_5.X)    # 3
'''
# The reverse, however, is not true

print('-' * 10 + "A.6. Reloading Modules" + '-' * 10)

# Imports (via both import and from statements) load and run a module's code only
# the first time the module is imported in a process.

# Later imports use the already loaded module object without reloading or rerunning
# the file's code.

# The reload function forces an already loaded module's code to be reloaded and
# rerun. Assignments in the file's new code change the existing module object in place

# Why care about reloading modules? In short, dynamic customization: the reload 
# function allows parts of a program to be changed without stopping the whole program.
# With reload, the effects of changes in components can be observed immediately.

# Though beyond this book's scope, note that reload currently only works on modules
# written in Python; compiled extension modules coded in a language such as C can be
# dynamically loaded at runtime, too, but they can't be reloaded

# In Python 2.X, reload is available as a built-in function. 
# In Python 3.X, it has been moved to the imp standard library module it's known as imp.reload in 3.X.

# - reload is a function in Python, not a statement.
# - reload is passed an existing module object, not a new name.
# - reload lives in a module in Python 3.X and must be imported itself.

# Because reload expects an object, a module must have been previously imported 
# successfully before you can reload it

# As a function reloads require parentheses, but import statements do not

# When you call reload, Python rereads the module file's source code and reruns its top-
# level statements. Perhaps the most important thing to know about reload is that it
# changes a module object in place; it does not delete and re-create the module object.
# Because of that, every reference to an entire module object anywhere in your program
# is automatically affected by a reload.  

# - reload runs a module file's new code in the module's current namespace.
# Rerunning a module file's code overwrites its existing namespace, 
# rather than deleting and re-creating it.

# Top-level assignments in the file replace names with new values. For instance,
# rerunning a def statement replaces the prior version of the function in the module's
# namespace by reassigning the function name.

# Reloads impact all clients that use import to fetch modules. Because clients
# that use import qualify to fetch attributes, they'll find new values in the module
# object after a reload.

# Reloads impact future from clients only. Clients that used from to fetch attributes
# in the past won't be affected by a reload; they'll still have references to the old
# objects fetched before the reload.

# Reloads apply to a single module only. You must run them on each module you
# wish to update, unless you use code or tools that apply reloads transitively.

# Create initial file content
# Clear the file: https://docs.python.org/2/tutorial/inputoutput.html
f = open('import_files/simple_7.py', 'w')
f.write('message = "First"\n')
f.close()

import import_files.simple_7
print(import_files.simple_7.message)        # First

time.sleep(1)                               # So the timestamp of the file changes: https://stackoverflow.com/questions/47392526/module-reload-doesnt-work-as-expected

# Modify file content
f = open('import_files/simple_7.py', 'w')
f.write('message = "Second"\n')
f.close()

import import_files.simple_7
print(import_files.simple_7.message)        # First (it's fine, because we haven't reloaded the file)

from imp import reload                      # Necessary for Python 3.X
reload(import_files.simple_7)
print(import_files.simple_7.message)        # Second

# The from * form is worse in most regards - it can
# seriously corrupt namespaces and obscure the meaning of variables, 
# so it is probably best used sparingly.