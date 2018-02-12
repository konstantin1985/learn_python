


# USEFUL LINKS:
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute

# GENERAL INFORMATION:
# - In Python, you can access the attributes of any object that
#   has attributes using the qualification (a.k.a. attribute fetch)
#   syntax object.attribute
# - Qualification is really an expression that returns the value
#   assigned to an attribute name assiciated with an object.


# Attribute methods. Write a class called Attrs with methods that intercept
# every attribute qualification (both fetches and assignments), and print
# messages listing their arguments to stdout. Create an Attrs instance, and
# experiment with qualifying it interactively. 

class Attrs:
    
    def __getattr__(self, attrname):
        print('__getattr__: %s', (attrname,))
    
    def __setattr__(self, attrname, value):
        print('__setattr__: %s, value %s', (attrname, value))
    
a = Attrs()

a.some_attr                                                              # ('__getattr__: %s', ('some_attr',))
a.another_attr = 10                                                      # ('__setattr__: %s, value %s', ('another_attr', 10))

# What happens when you try to use the instance in expressions? 
# Try adding, indexing, and slicing the instance of your class. 
 
# a[1]                                                                   # Python 2.X: ('__getattr__: %s', ('__getitem__',)) TypeError: 'NoneType' object is not callable
# a[1:2]                                                                 # Python 2.X: ('__getattr__: %s', ('__getslice__',)) TypeError: 'NoneType' object is not callable
# a + 5                                                                  # Python 2.X: ('__getattr__: %s', ('__coerce__',)) TypeError: 'NoneType' object is not callable
 
# In Python 3.X the errors are different (see explanation below):
# TypeError: 'Attrs' object does not support indexing
# TypeError: 'Attrs' object is not subscriptable
# TypeError: unsupported operand type(s) for +: 'Attrs' and 'int'
 
# (Note: a fully generic approach based upon __getattr__ will work in 2.X's
# classic classes but not in 3.X's new-style classes-which are optional in
# 2.X - for reasons noted in Chapter 28, Chapter 31, and Chapter 32, and 
# summarized in the solution to this exercise.)

# - As noted in Chapter 32 and elsewhere, getattr__ is not called for built-in
#   operations in Python 3.X (and in 2.X if new-style classes are used), so the
#   expressions aren't intercepted at all here; in new-style classes, a class
#   like this must redefine __X__ operator overloading methods explicitly.


