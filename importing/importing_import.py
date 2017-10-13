

# When we import the same file multiple times, it is actually executed only once
import importing_to_import # Executed imported_to_import.py
import importing_to_import # nothing


# We can force reload import
# The from statement simply copies a name out of a module
from imp import reload
rv = reload(importing_to_import) # Executed imported_to_import.py
print rv                         # <module 'importing_to_import' from '/home/konstantin/Sphinx/learn_python/importing/importing_to_import.pyc'>

# You need to import the module before using dir
print dir(importing_to_import)   # ['__builtins__', '__doc__', '__file__', '__name__', '__package__']

