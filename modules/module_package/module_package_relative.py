

# Good information on relative imports
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

# Relative imports use the module's name to determine where it is in a package. 
# When you use a relative import like from .. import foo, the dots indicate to step 
# up some number of levels in the package hierarchy. 

# However, if your module's name is __main__, it is not considered to be in a package. 
# Its name has no dots, and therefore you cannot use from .. import statements inside it.
# If you try to do so, you will get the "relative-import in non-package" error.



print('-' * 10 + "A.1. Basic information" + '-' * 10)

# Imports within the package can be relative to the package.

# The way this works is version-dependent: Python 2.X implicitly searches package 
# directories first on imports, while 3.X requires explicit relative import syntax
# in order to import from the package directory.

# Imports with dots: In both Python 3.X and 2.X, you can use leading dots in from
# statements' module names to indicate that imports should be relative-only to the
# containing package-such imports will search for modules inside the package 
# directory only and will not look for same-named modules located elsewhere on the
# import search path (sys.path). The net effect is that package modules override
# outside modules.

# Imports without dots: In Python 2.X, normal imports in a package's code without
# leading dots currently default to a relative-then-absolute search path order-that
# is, they search the package's own directory first. However, in Python 3.X, normal
# imports within a package are absolute-only by default-in the absence of any 
# special dot syntax, imports skip the containing package itself and look elsewhere on
# the sys.path search path.

# For example, in both Python 3.X and 2.X a statement of the form:
# from . import spam           # Relative to this package
# instructs Python to import a module named spam located in the same package directory
# as the file in which this statement appears. 

# Similarly, this statement:
# from .spam import name
# means "from a module named spam located in the same package as the file that contains
# this statement, import the variable name."

# The behavior of a statement without the leading dot depends on which version of
# Python you use. In 2.X, such an import will still default to the original relative-then-
# absolute search path order (i.e., searching the package's directory first), unless a
# statement of the following form is included at the top of the importing file (as its first 
# executable statement):
# from __future__ import absolute_import
# Use 3.X relative import model in 2.X

# For instance, in 3.X's model, a statement of the following form will always find a string
# module somewhere on sys.path, instead of a module of the same name in the package:
# import string            # Skip this package's version

# By contrast, without the from __future__ statement in 2.X, if there's a local string
# module in the package, it will be imported instead. To get the same behavior in 3.X,
# and in 2.X when the absolute import change is enabled, run a statement of the following
# form to force a relative import:
# from . import string   # Searches this package only

# Notice that leading dots can be used to force relative imports only with the from 
# statement, not with the import statement.

# Code located in some module A.B.C can use any of these forms:
# from . import D         # Imports A.B.D   (. means A.B)
# from .. import E        # Imports A.E     (.. means A)

# from .D import X        # Imports A.B.D.X (. means A.B)
# from ..E import X       # Imports A.E.X   (.. means A)


# With this form, the containing package is searched automatically, regardless of
# the search path settings, search path order, and directory nesting. 
# from . import string

# - Relative imports apply to imports within packages only
# - Relative imports apply to the from statement only, not import statements

# In sum, Python imports select between relative (in the containing directory) and 
# absolute (in a directory on sys.path - 5 components of sys.path) resolutions 
# as follows:
# Dotted imports: from . import m
# Are relative-only in both 2.X and 3.X
# Nondotted imports: import m, from m import x
# Are relative-then-absolute in 2.X, and absolute-only in 3.X

# If we add a module of the same name 'string.py' in the directory we're working in,
# it is selected instead, because the first entry on the module search path is the
# current working directory (CWD)
import string             # Home directory string
print(string)             # <module 'string' from '/home/konstantin/Sphinx/learn_python/modules/module_package/string.py'>

# from . import string    # ValueError: Attempted relative import in non-package

print('-' * 10 + "A.2. Imports within packages" + '-' * 10)


# The first file (spam.py) in this package tries to import the second (eggs.py) 
# with a normal import statement. Because this is taken to be relative 
# in 2.X but absolute in 3.X, it fails in the latter. That is, 2.X searches
# the containing package first, but 3.X does not.

# IMPORTANT EXAMPLE

# import pkg.spam
# In Python 2.X:
# <module 're' from '/usr/lib/python2.7/re.pyc'>
# 99999
# In Python 3.X:
# import pkg.spam
# ImportError: No module named 'eggs'

# To make this work in both 2.X and 3.X, change the first file to use
# the special relative import syntax, so that its import searches the
# package directory in 3.X too

import pkg.spam_relative
# Works in Python 2.X and Python 3.X: 
# Because in spam_relative.py the import of eggs.py is relative
# <module 'string' from '/home/konstantin/Sphinx/learn_python/modules/module_package/string.pyc'>
# 99999

# Although you can skip the package directory with an absolute import
# in 3.X, you still can't skip the home directory of the program that 
# imports the package. So the file 'string.py' above is a local to the
# home directory of the program file (same in P3 and P2)

# If sting.py isn't in the home directory of the program, but in
# pkg/string.py then Python 3.X will import the SYSTEM 'string.py', but
# Python 2.X will import LOCAL 'pkg/string.py' - incompatible behavior

# IMPORTANT IDEA

# If we delete the 'pkg2/string.py' file and any associated byte code 
# in this example now, the RELATIVE import (from . import string) in 
# spam.py fails in both 3.X and 2.X, instead of falling back on the
# standard library (or any other) version of this module

# import pkg2.spam_relative    # ImportError: cannot import name string

# When absolute syntax is used, though, the module we get varies per version again. 2.X
# interprets this as relative to the package first, but 3.X makes it "absolute," which in this
# case really just means it skips the package and loads the version relative to the CWD
# - not the version in the standard library

import pkg3.spam
# Python 2.X
# <module 'pkg3.string' from '...module_package/pkg3/string.py'>
# Python 3.X (absolute = sys.path, first look in program home i.e. CWD)
# <module 'string' from '...module_package/string.py'>

# As you can see, although packages can explicitly request modules within
# their own directories with dots, their "absolute" imports are otherwise
# still relative to the rest of the normal module search path. In this case,
# a file in the program using the package hides the standard library module 
# the package may want. 

print('-' * 10 + "A.3. Pitfalls of relative import" + '-' * 10)

# Python 3.X and 2.X do not allow from . relative syntax to be used unless the
# importer is being used as part of a package (i.e., is being imported from
# somewhere else).

# Python 3.X does not search a package module's own directory for imports,
# unless from . relative syntax is used (or the module is in the current
# working directory or main script's home directory).

# from . import mod           # Not allowed in nonpackage mode in both 2.X and 3.X
# import mod                  # Does not search file's own directory in package mode in 3.X

# Alternatively, you can attempt manual sys.path changes (a generally brittle and error-
# prone task), or always use full package paths in absolute imports instead of either
# package-relative syntax or simple imports, and assume the package root is on the 
# module search path

# Of all these schemes, the last-full package path imports -
# may be the most portable and functional

# PROBLEM DESCRIPTION:

# OK as a program

# python pkg4/main.py
# EggsEggsEggs
# python pkg4/spam.py
# EggsEggsEggs
# python3 pkg4/main.py
# EggsEggsEggs
# python3 pkg4/spam.py
# EggsEggsEggs

# import pkg4.spam
# Python 2.X: EggsEggsEggs - plain imports search package directory first
# Python 3.X: ImportError: No module named 'eggs' - plain imports search only CWD plus sys.path

# Relative import won't help here

# The following retains the single directory for both a main top-level
# script and package modules, and adds the required dots - in both 
# 2.X and 3.X this now works when the directory is imported as a package,
# but fails when it is used as a program directory

import pkg5.spam               # OK as a package but not program in 3.X and 2.X
# EggsEggsEggs

# python pkg\main.py           # SystemError: ... cannot perform relative import
# python pkg\spam.py           # SystemError: ... cannot perform relative import
# Because relative import works only in packages, but we run pkg/main.py that is
# inside the package but don't consider its folder as a package

# MOST IMPORTANT IN THE PROBLEM: relative import works only in package mode
#  by 3.X and 2.X. When main.py is in the package (without subdir) and if you
#  run main.py then relative import doesn't work

# PROBLEM FIX 1: subdirectory

# one solution is to isolate ALL BUT THE MAIN files used only by the program
# in a subdirectory - this way, your intrapackage imports still work in Pythons,
# you can use the top directory as a standalone program, and the nested 
# directory still serves as a package for use from other programs

# python pkg6\main.py           # From main script: same result in 2.X and 3.X
# EggsEggsEggs

import pkg6.sub.spam
# EggsEggsEggs

# The potential downside of this scheme is that you won't be able to run package
# modules directly to test them with embedded self-test code, though tests can 
# be coded separately in their parent directory instead:
# py -3 pkg\sub\spam.py         # But individual modules can't be run to test
# SystemError: ... cannot perform relative import

# PROBLEM FIX 2: full path

# Alternatively, full path package import syntax would address this case too -
# it requires the directory above the package root to be in your path, though
# this is probably notextra requirement for a realistic software package.
# Most Python packages will either require this setting, or arrange for it to
# be handled automatically with install tools (such as distutils, which may 
# store a package's code in a directory on the default module search path such
# as the site-packages root

# c:\code> set PYTHONPATH=C:\code
# c:\code> python pkg7\main.py   # From main script: Same result in 2.X and 3.X
# EggsEggsEggs

import pkg7.spam                 # EggsEggsEggs

# In sum, unless you're willing and able to isolate your modules in subdirectories below
# scripts, full package path imports are probably preferable to package-relative imports
# -though they're more typing, they handle all cases, and they work the same in 2.X
# and 3.X. There may be additional workarounds that involve extra tasks (e.g., manually
# setting sys.path in your code), but we'll skip them here because they are more obscure
# and rely on import semantics, which is error-prone; full package imports rely only on
# the basic package mechanism.


