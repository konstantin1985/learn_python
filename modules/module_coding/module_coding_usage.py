

# It is also possible to create a Python module by writing code in an external 
# language such as C, C++, and others (e.g., Java, in the Jython implementation
# of the language). Such modules are called extension modules, and they are
# generally used to wrap up external libraries for use in Python scripts. When
# imported by Python code, extension modules look and feel the same as modules coded
# as Python source code files-they are accessed with import statements, and they 
# provide functions and objects as module attributes. See "Programming Python" book.

print('-' * 10 + "A.1. import and from" + '-' * 10)

# The from statement is really just a minor extension to
# the import statement-it imports the module file as usual (running the full 
# three-step procedure of the preceding chapter), but adds an extra step that
# copies one or more names (not objects) out of the file. The entire file is 
# loaded, but you're given names for more direct access to its parts.

# When we use a * instead of specific names, we get copies of all names 
# assigned at the top level of the referenced module. Technically, both import
# and from statements invoke the same import operation; the from * form simply 
# adds an extra step that copies all the names in the module into the importing 
# scope. It essentially collapses one module's namespace into another

# In Python 3.X, the from ...* statement form described here can be used
# only at the top level of a module file, not within a function. Python 2.X
# allows it to be used within a function, but issues a warning anyhow. 

from import_files.simple_1 import *

printer("Hello")

# Modules are loaded and run on the first import or from, and only the first. 
# This is on purpose-because importing is an expensive operation, by default
# Python does it just once per file, per process. Later import operations simply
# fetch the already loaded module object.

import import_files.simple_2  # hello_2

# Pay attention that the qualifier import_files.simple_2 is required
print(import_files.simple_2.spam)  # 1 

# Second and later imports don't rerun the module's code; they just fetch
# the already created module object from Python's internal modules table.
# Thus, the variable spam is not reinitialized.

import_files.simple_2.spam = 2     # Change attribute in module
import import_files.simple_2       # Just fetches already loaded module
print import_files.simple_2.spam   # 2, Code wasn't rerun: attribute unchanged

# Just like def, import and from are executable statements, not compile-time 
# declarations. They are not resolved or run until Python reaches them while
# executing your program.

# Also, like def, the import and from are implicit assignments:
# - import assigns an entire module object to a single name.
# - from assigns one or more names to objects of the same names in another 
# module.

# Names copied with a from become references to shared objects; as with
# function arguments, reassigning a copied name has no effect on the module
# from which it was copied, but changing a shared mutable object through 
# a copied name can also  change it in the module from which it was imported.

from import_files.simple_3 import x,y # Hello_3, from also runs a normal import operation, see below
print(x, y)                           # (1, [1, 2])
x = 42                                # Changes local x only
y[0] = 42                             # Changes share mutable in place

import import_files.simple_3
print(import_files.simple_3.x)        # 1
print(import_files.simple_3.y)        # [42, 2]

# IMPORTANT
# There is no link from a name copied with FROM back to the file it came from.
# To really change a global name in another file, you must use IMPORT.

import import_files.simple_3
import_files.simple_3.x = 42          # Changes in other module
from import_files.simple_3 import x
print(x)                              # 42

# from only copies names from one module to another; it does not assign the
# module name itself. At least conceptually, a from statement like this one:

# from module import name1, name2     # Copy these two names out (only)

# is equivalent to this statement sequence:

# import module                       # Fetch the module object
# name1 = module.name1                # Copy names out by assignment
# name2 = module.name2
# del module                          # Get rig of the module name

# Like all assignments, the from statement creates new variables in the importer, which
# initially refer to objects of the same names in the imported file. Only the names are
# copied out, though, not the objects they reference, and not the name of the module
# itself. When we use the from * form of this statement (from module import *), the
# equivalence is the same, but all the top-level names in the module are copied over to
# the importing scope this way.

# Probably the best real-world advice here is to generally prefer import to from for simple
# modules, to explicitly list the variables you want in most from statements, and to limit
# the from * form to just one import per file. That way, any undefined names can be
# assumed to live in the module referenced with the from *.

# The only time you really must use import instead of from is when you must use the same
# name defined in two different modules.

