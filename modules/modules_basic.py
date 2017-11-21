# In short, modules provide an easy way to organize components into a system by serving
# as self-contained packages of variables known as namespaces. All the names defined at
# the top level of a module file become attributes of the imported module object. As we
# saw in the last part of this book, imports give access to names in a module's global
# scope. That is, the module file's global scope morphs into the module object's attribute
# namespace when it is imported.

# Roles of modules:
# - code reuse
# - system namespace partitioning
# - implement shared services or data (components that are shared across a system and
# hence require only a single copy)

# Cross-file module linking is not resolved until such import statements are executed
# at runtime; their net effect is to assign module names-simple variables like b - to 
# loaded module objects. In fact, the module name used in an import statement serves
# two purposes: it identifies the external file to be loaded, but it also becomes 
# a variable assigned to the loaded module.

# Similarly, objects defined by a module are also created at runtime, as the import is
# executing: import literally runs statements in the target file one at a time to 
# create its contents. Along the way, every name assigned at the top-level of the file
# becomes an attribute of the module, accessible to importers.

# The code b.spam means: Fetch the value of the name spam that lives within the object b.
# This happens to be a callable function in our example, so we pass a string in
# parentheses ('gumby').

# Some C programmers like to compare the Python module import operation to a C
# #include, but they really shouldn't - in Python, imports are not just textual insertions
# of one file into another. They are really runtime operations that perform three distinct
# steps the first time a program imports a given file:
# 1. Find the module's file.
# 2. Compile it to byte code (if needed).
# 3. Run the module's code to build the objects it defines.

# 2. Compile (Maybe)

# During an import operation Python checks both file modification times and the byte
# code's Python version number to decide how to proceed. The former uses file 
# "timestamps," and the latter uses either a "magic" number embedded in the byte code 
# or a filename, depending on the Python release being used.

# If the byte code file is older than the source file (i.e., if you've changed the source)
# or was created by a different Python version, Python automatically regenerates the
# byte code when the program is run.

# If, on the other hand, Python finds a .pyc byte code file that is not older than the
# corresponding .py source file and was created by the same Python version, it skips
# the source-to-byte-code compile step.

# In addition, if Python finds only a byte code file on the search path and no source,
# it simply loads the byte code directly; this means you can ship a program as just
# byte code files and avoid sending source. 

# Notice that compilation happens when a file is being imported. Because of this, you
# will not usually see a .pyc byte code file for the top-level file of your program, 
# unless it is also imported elsewhere-only imported files leave behind .pyc files
# on your machine. The byte code of top-level files is used internally and discarded;
# byte code of imported files is saved in files to speed future imports.

# 3. RUN

# The final step of an import operation executes the byte code of the module. All state-
# ments in the file are run in turn, from top to bottom, and any assignments made to
# names during this step generate attributes of the resulting module object. 

# If any top-level code in a module file does real work, you'll see its results at
# import time. For example, top-level print statements in a module show output when
# the file is imported.

# Any given module is imported only once per process by default. Future imports 
# skip all three import steps and reuse the already loaded module in memory. If you 
# need to import a file again after it has already been loaded (for example, to 
# support dynamic end-user customizations), you have to force the issue with 
# an imp.reload call

# BYTE CODE FILES

# In Python 3.1 and earlier (including all of Python 2.X) byte code is stored in
# files in the same directory as the corresponding source files, normally with the
# filename extension .pyc (e.g., module.pyc). Byte code files are also stamped 
# internally with the version of Python that created them

# In Python 3.2 and later Byte code is instead stored in files in a subdirectory
# named __pycache__, which Python creates if needed, and which is located in the 
# directory containing the corresponding source files. They are given more 
# descriptive names that include text identifying the version of Python that 
# created them (e.g., module.cpython-32.pyc)


print('-' * 10 + "A.1. " + '-' * 10)

