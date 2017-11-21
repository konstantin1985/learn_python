
# The first time this module is imported (or run as a program), Python executes its
# statements from top to bottom. Some statements create names in the module's 
# namespace as a side effect, but others do actual work while the import is going on. 
# For instance, the two print statements in this file execute at import time

print('starting to load...')

import sys

name = 42

def func(): pass

class klass: pass

print('done loading.')

