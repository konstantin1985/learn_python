


# In sum, variables are created when assigned, can reference any type of object, and must
# be assigned before they are referenced. This means that you never need to declare names
# used by your script, but you must initialize names before you can update them; coun-
# ters, for example, must be initialized to zero before you can add to them.

# Names and objects after running the assignment a = 3. Variable a becomes a reference to
# the object 3. Internally, the variable is really a pointer to the object's memory space created by running
# the literal expression 3.
a = 3

# Variables are entries in a system table, with spaces for links to objects.
# Objects are pieces of allocated memory, with enough space to represent the values
# for which they stand.
# References are automatically followed pointers from variables to objects.

# Each object also has two standard header fields: a type designator used to
# mark the type of the object, and a reference counter used to determine when it's OK to
# reclaim the object.

# Names have no types; as stated earlier, types live with objects, not names. In the pre-
# ceding listing, we've simply changed a to reference different objects.
a = 3
a = 'spam'
a = 1.23

# Whenever a name is assigned to a new object, the space
# held by the prior object is reclaimed if it is not referenced by any other name or object.
# This automatic reclamation of objects' space is known as garbage collection

# SHARED REFERENCE: The second command causes Python to create the variable b; the variable a is being used and not
# assigned here, so it is replaced with the object it references (3), and b is made to reference
# that object. The net effect is that the variables a and b wind up referencing the same
# object
a = 3
b = a
a = 'spam'
print(a)   # 'spam', a reference 'spam' object now
print(b)   # 3, b still reference 3 object

# Setting a variable to a new value does not alter the original object, but rather causes the variable to reference an
# entirely different object. The net effect is that assignment to a variable itself can impact
# only the single variable being assigned.
a = 3
b = a
a = a + 2
print(a)   # 5
print(b)   # 3, integers are immutable so they can't be changed in place

# For MUTABLE objects situation is different
# This assignment simply sets L1 to a different object; L2 still references the original list.
L1 = [2, 3, 4]
L2 = L1
L1 = 24
print(L1, L2)   # (24, [2, 3, 4])

# However
# This behavior only occurs for mutable objects that support in-place changes, and is
# usually what you want, but you should be aware of how it works, so that it's expected.

L1 = [2, 3, 4]
L2 = L1
L1[0] = 24
print(L1, L2)   # ([24, 3, 4], [24, 3, 4])

# How to avoid it? Make a copy!
L1 = [2, 3, 4]
L2 = L1[:]       # Make a copy of L1, or list(L1) or copy.copy(L1)
L1[0] = 24
print

# Note that this slicing technique won't work on the other major mutable core types,
# dictionaries and sets, because they are not sequences-to copy a dictionary or set,
# instead use their X.copy() method call (lists have one as of Python 3.3 as well), or pass
# the original object to their type names, dict and set.

# Because of Python's reference model, there are two different ways to check
# for equality in a Python program.
# The first technique here, the == operator, tests whether the two referenced objects have
# the same values; this is the method almost always used for equality checks in Python.
# The second method, the is operator, instead tests for object identity-it returns True
# only if both names point to the exact same object, so it is a much stronger form of
# equality testing and is rarely applied in most programs.
L = [1, 2, 3]
M = L
print(L == M, L is M) # (True, True)

L = [1, 2, 3]
M = [1, 2, 3]
print(L == M, L is M) # (True, False)

# Because small integers and strings are
# cached and reused, though, is tells us they reference the same single object.
x = 42
y = 42
print(x == y, x is y) # (True, True)

# We can get reference count
import sys 
print(sys.getrefcount(1)) # 367 or something like this



