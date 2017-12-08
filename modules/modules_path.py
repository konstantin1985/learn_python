

# MODULE SEARCH PATH


# The first and third elements of the search path are defined automatically. 
# Because Python searches the concatenation of these components from first to last, 
# though, the second and fourth elements can be used to extend the path to include
# your own source code directories.

# 1. The home directory of the program

# When you're running a program, this entry is the directory containing your
# program's top-level script file. Be careful not to accidentally hide library 
# modules (by your files) if you need them in your program


# 2. PYTHONPATH directories (if set)

# Next, Python searches all directories listed in your PYTHONPATH environment variable
# setting, from left to right (assuming you have set this at all: it's not preset for
# you). In brief, PYTHONPATH is simply a list of user-defined and platform-specific
# names of directories that contain Python code files.

# 3. Standard library directories

# Next, Python automatically searches the directories where the standard library
# modules are installed on your machine. Because these are always searched, they
# normally do not need to be added to your PYTHONPATH or included in path files

# 4. The contents of any .pth files (if present)

# Next, a lesser-used feature of Python allows users to add directories to the module
# search path by simply listing them, one per line, in a text file whose name ends
# with a .pth suffix (for "path").

# On Unix-like systems, this file might be located in usr/local/lib/python3.3/site-packages 
# or /usr/local/lib/site-python instead.

# When such a file is present, Python will add the directories listed on each line of
# the file, from first to last, near the end of the module search path list-currently,
# after PYTHONPATH and standard libraries, but before the site-packages directory
# where third-party extensions are often installed. 

# 5. The site-packages home of third-party extensions

# Finally, Python automatically adds the site-packages subdirectory of its standard
# library to the module search path. By convention, this is the place that most third-
# party extensions are installed

# Because their install directory is always part of the module search path, clients
# can import the modules of such extensions without any path settings.

# /usr/local/lib/python3.6/site-packages

import sys

print('-' * 10 + "A.1. sys.path" + '-' * 10)

# If you want to see how the module search path is truly configured on your machine,
# you can always inspect the path as Python knows it by printing the built-in sys.path

# This list of directory name strings is the actual search path within Python; 
# on imports, Python searches each directory in this list from left to right, 
# and uses the first file match it finds.

# Really, sys.path is the module search path. Python configures it at program startup,
# automatically merging the home directory of the top-level file (or an empty string to
# designate the current working directory), any PYTHONPATH directories, the contents of
# any .pth file paths you've created, and all the standard library directories. The result 
# is a list of directory name strings that Python searches on each import of a new file.

print(sys.path)


# ['/home/konstantin/Sphinx/learn_python/modules', 
#  '/home/konstantin/Sphinx/learn_python', 
#  '/home/konstantin/Sphinx/learn_python/strings', 
#  '/home/konstantin/Sphinx/learn_python/exceptions', 
#  '/home/konstantin/Sphinx/learn_python/linux', 
#  '/home/konstantin/Sphinx/learn_python/importing', 
#  '/home/konstantin/Sphinx/learn_python/types_python', 
#  '/home/konstantin/Sphinx/learn_python/rest',
#  '/home/konstantin/Sphinx/learn_python/book1', 
#  '/home/konstantin/Sphinx/learn_python/pipes', 
#  '/home/konstantin/Sphinx/learn_python/hashing', 
#  '/usr/lib/python2.7/site-packages/netsnmp_python-1.0a1-py2.7-linux-i686.egg', 
#  '/usr/lib/python2.7', 
#  '/usr/lib/python2.7/plat-linux2', 
#  '/usr/lib/python2.7/lib-dynload', 
#  '/usr/lib/python2.7/site-packages', 
#  '/usr/lib/python2.7/site-packages/gtk-2.0', 
#  '/usr/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg-info',
#  '/usr/lib/python2.7/site-packages/setuptools-18.1-py2.7.egg',
#  '/home/konstantin/Programs/Sphinx-current/PythonTestProject', 
#  '/usr/lib/python2.7/site-packages/RBTools-0.7.5-py2.7.egg', 
#  '/usr/lib/python27.zip', 
#  '/usr/lib/python2.7/lib-tk', 
#  '/usr/lib/python2.7/lib-old', 
#  '/usr/local/lib/python2.7/site-packages']

# As you'll see by example later in this part of the book, by
# modifying the sys.path list, you can modify the search path for all future imports made 
# in a program’s run. Such changes last only for the duration of the script.


print('-' * 10 + "A.2. Module file selection" + '-' * 10)

# Keep in mind that filename extensions (e.g., .py) are omitted from import statements
# intentionally. Python chooses the first file it can find on the search path that matches
# the imported name. In fact, imports are the point of interface to a host of external
# components-source code, multiple flavors of byte code, compiled extensions, and
# more. Python automatically selects any type that matches a module's name.

# For example, an import statement of the form import b might today load or resolve to:
# - A source code file named b.py
# - A byte code file named b.pyc
# - An optimized byte code file named b.pyo (a less common format)
# - A directory named b, for package imports (described in Chapter 24)
# - A compiled extension module, coded in C, C++, or another language, and dynamically 
# linked when imported (e.g., b.so on Linux, or b.dll or b.pyd on Cygwin and Windows)

# Some standard modules we will use in this book are actually coded in C, not Python;
# because they look just like Python-coded module files, their clients don't have to care.

# If you have both a b.py and a b.so in different directories, Python will always load the
# one found in the first (leftmost) directory of your module search path during the left-
# to-right search of sys.path. 


print('-' * 10 + "A.3. Import hooks" + '-' * 10)

# It is possible to redefine much of what an import operation does
# in Python, using what are known as import hooks. These hooks can be used to make
# imports do various useful things, such as loading files from archives, performing 
# decryption, and so on.

print('-' * 10 + "A.4. distutils and eggs" + '-' * 10)

# Third-party extensions for Python typically use the distutils tools in the standard
# library to automatically install themselves, so no path configuration is required 
# to use their code.

# Systems that use distutils generally come with a setup.py script, which is run to install
# them; this script imports and uses distutils modules to place such systems in a direc-
# tory that is automatically part of the module search path (usually in the 
# Lib\site-packages subdirectory of the Python install tree, wherever that resides on 
# the target machine).

# Also check out the third-party open source eggs system, which adds dependency checking
# for installed Python software.

# EGG: https://stackoverflow.com/questions/2051192/what-is-a-python-egg
# The .egg file itself is essentially a .zip file.

print('-' * 10 + "A.4. Namespace" + '-' * 10)

# A namespace is a self-contained package of variables, which are known as the
# attributes of the namespace object. A module's namespace contains all the names
# assigned by code at the top level of the module file









