

print('-' * 10 + "A.1. Basic information" + '-' * 10)


# https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package
# A module is a single file (or files) that are imported under one import and used. e.g.
# import my_module
# A package is a collection of modules in directories that give a package hierarchy (containing an additional __init__.py file)
# from my_package.timing.danger.internets import function_of_love

# https://www.learnpython.org/en/Modules_and_Packages
# Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty,
# and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

# IMPORTANT:

# There is no __init__.py in the folder pack0, so we can't import the package (folder) it as a module
# We can't also import modules from within pack0 folder!!!
# import pack0                 # ImportError: No module named pack0
# import pack0.mod             # ImportError: No module named pack0.mod (MOST IMPORTANT)

import pack1                   # Package (folder) can be imported as a module, because there is __init__.py
print(pack1)                   # <module 'pack1' from '/home/konstantin/Sphinx/learn_python/modules/module_package/pack1/__init__.py'>
# print(pack1.mod.x)           # AttributeError: 'module' object has no attribute 'mod'

import pack1.mod               # Possible only because there is __init__.py in pack1 folder, so pack1 is a package
print(pack1.mod.x)             # 200

# Root directory may have no __init__.py

# The leftmost component in a package import path is still relative to a
# directory included in the sys.path module search path list.
# import dir1.dir2.mod

# You cannot use an invalid statement like this:
# import C:\mycode\dir1\dir2\mod
#     Error: illegal syntax
# But you can add C:\mycode to your PYTHONPATH variable or a .pth file, and say this in your script:
# import dir1.dir2.mod

# One way or another, though, your module search path must include all the directories containing leftmost
# components in your code's package import statements.


print('-' * 10 + "A.2. Package __init__.py Files" + '-' * 10)

# For a directory structure such as this:
# dir0\dir1\dir2\mod.py
# and an import statement of the form:
# import dir1.dir2.mod
# the following rules apply:

# - dir1 and dir2 both must contain an __init__.py file.
# - dir0, the container, does not require an __init__.py file; this file will simply be ignored if present.
# - dir0, not dir0\dir1, must be listed on the module search path sys.path.

#To satisfy the first two of these rules, package creators must create files of the sort we'll
# explore here. To satisfy the latter of these, dir0 must be an automatic path component
# (the home, libraries, or site-packages directories), or be given in PYTHONPATH or .pth file
# settings or manual sys.path changes.

# In more detail, the __init__.py file serves as a hook for package initialization-time 
# actions, declares a directory as a Python package, generates a module namespace for a
# directory, and implements the behavior of from * (i.e., from .. import *) statements
# when used with directory imports:

# - Package initialization
#   The first time a Python program imports through a directory, it automatically runs
#   all the code in the directory's __init__.py file. Because of that, these files are a
#   natural place to put code to initialize the state required by files in a package. For
#   instance, a package might use its initialization file to create required data files, open
#   connections to databases

# - Module usability declarations
#   Package __init__.py files are also partly present to declare that a directory is a
#   Python package. In this role, these files serve to prevent directories with common
#   names from unintentionally hiding true modules that appear later on the module
#   search path.

# - Module namespace initialization
#   In the package import model, the directory paths in your script become real nested
#   object paths after an import. For instance, in the preceding example, after the im-
#   port the expression dir1.dir2 works and returns a module object whose namespace
#   contains all the names assigned by dir2's __init__.py initialization file. Such files
#   provide a namespace for module objects created for directories, which would
#   otherwise have no real associated module file.

# - from * statement behavior
#   As an advanced feature, you can use __all__ lists in __init__.py files to define what
#    is exported when a directory is imported with the from * statement form. In an
#   __init__.py file, the __all__ list is taken to be the list of submodule names that
#   should be automatically imported when from * is used on the package (directory)
#   name. If __all__ is not set, the from * statement does not automatically load sub-
#   modules nested in the directory; instead, it loads just names defined by assignments
#   in the directory's __init__.py file, including any submodules explicitly imported by
#   code in this file.

import dir1.dir2.mod                    # First imports run init files

# dir1 init
# dir2 init
# in mod.py

import dir1.dir2.mod                    # Later imports do not run init files

# Just like module files, an already imported directory may be passed to 
# reload to force reexecution of that single item.

from imp import reload                  # only necessary in Python 3.X
rv = reload(dir1)                       # dir1 init
print(rv)                               # <module 'dir1' from '/home/konstantin/Sphinx/learn_python/modules/module_package/dir1/__init__.pyc'>

rv = reload(dir1.dir2)                  # dir2 init
print(rv)                               # <module 'dir1.dir2' from '/home/konstantin/Sphinx/learn_python/modules/module_package/dir1/dir2/__init__.pyc'>

# Once imported, the path in your import statement
# becomes a NESTED OBJECT PATH in your script.

print(dir1)                             # <module 'dir1' from '/home/konstantin/Sphinx/learn_python/modules/module_package/dir1/__init__.pyc'>
print(dir1.dir2)                        # <module 'dir1.dir2' from '/home/konstantin/Sphinx/learn_python/modules/module_package/dir1/dir2/__init__.pyc'>
print(dir1.dir2.mod)                    # <module 'dir1.dir2.mod' from '/home/konstantin/Sphinx/learn_python/modules/module_package/dir1/dir2/mod.pyc'>

# dir1.x refers to the variable x assigned in dir1\__init__.py, much as mod.z refers to
# the variable z assigned in mod.py:
print(dir1.x)                           # 1
print(dir1.dir2.y)                      # 2
print(dir1.dir2.mod.z)                  # 3

# mod.z                                 # NameError: name 'mod' is not defined

# If you ever restructure your directory tree, the from statement
# requires just one path update in your code, whereas imports may
# require many.

from dir1.dir2 import mod
print(mod.z)                            # 3

from dir1.dir2.mod import z
print(z)                                # 3

import dir1.dir2.mod as mod
print(mod.z)                            # 3

from dir1.dir2.mod import z as modz
print(modz)                             # 3

# Package imports can also greatly simplify your PYTHONPATH and .pth file search path
# settings. In fact, if you use explicit package imports for all your cross-directory imports,
# and you make those package imports relative to a common root directory where all
# your Python code is stored, you really only need a single entry on your search path: the
# common root.

# Any directory with an __init__.py file is considered a Python package. The different modules
# in the package are imported in a similar manner as plain modules, but with a special behavior
# for the __init__.py file, which is used to gather all package-wide definitions.

# A file modu.py in the directory pack/ is imported with the statement import pack.modu. 
# This statement will look for an __init__.py file in pack, execute all of its top-level statements.
# Then it will look for a file named pack/modu.py and execute all of its top-level statements.
# After these operations, any variable, function, or class defined in modu.py is available in the pack.modu namespace.

# Leaving an __init__.py file empty is considered normal and even a good practice, 
# if the package's modules and sub-packages do not need to share any code.



 




