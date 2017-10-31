# Assignments always store references to objects, not copies
# of those objects. In practice, this is usually what you want. Because assignments can
# generate multiple references to the same object, though, it's important to be aware that
# changing a mutable object in place may affect other references to the same object else-
# where in your program. If you don't want such behavior, you'll need to tell Python to
# copy the object explicitly.

X = [1, 2, 3]
L = ['a', X, 'b']    # L = ['a', X[:], 'b'] to really copy
D = {'x':X, 'y':2}   # D = {'x':X, 'y':2} to really copy

# At this point, there are three references to the first list created: from the name X, from
# inside the list assigned to L, and from inside the dictionary assigned to D.
# Because lists are mutable, changing the shared list object from any of the three refer-
# ences also changes what the other two reference:

X[1] = 'surprise'
print(L)  # ['a', [1, 'surprise', 3], 'b']
print(D)  # {'y': 2, 'x': [1, 'surprise', 3]}

# You can do real copy and there will not be this behavior
L = [1, 2, 3]
D = {'a':1, 'b':2}
A = L[:]      # or list(L), there is no .copy for lists
B = D.copy()  # or dict(L)

A[1] = 'Ni'
B['c'] = 'spam'
print(L, D)   # ([1, 2, 3], {'a': 1, 'b': 2})

# Copy doesn't work for nested structures
A = ['a0', 'a1']
B = [A, 'b1', 'b2']
C = B[:]
A[0] = "Haha"
B[1] = "foo"
print(C)  # [['Haha', 'a1'], 'b0', 'b1'] - nested list A wasn't copied

# To fully copy a nested structure
import copy
A = ['a0', 'a1']
B = [A, 'b1', 'b2']
C = copy.deepcopy(B)
A[0] = "Haha"
B[1] = "foo"
print(C)  # [['a0', 'a1'], 'b1', 'b2']

# Python comparisons always inspect all parts of compound objects until a
# result can be determined. In fact, when nested objects are present, Python automatically
# traverses data structures to apply comparisons from left to right, and as deeply as
# needed.

# The == operator tests value equivalence. Python performs an equivalence test,
# comparing all nested objects recursively.
# The is operator tests object identity. Python tests whether the two are really the
# same object (i.e., live at the same address in memory).
L1 = [1, (2, 3)]
L2 = [1, (2, 3)]
L3 = L1
print(L1 == L2, L1 is L2)  # (True, False)
print(L1 == L3, L1 is L3)  # (True, True)

# Short strings are normally cached. Of course, because strings are immutable, the object
# caching mechanism is irrelevant to your code-strings can't be changed in place, 
# regardless of how many variables refer
# to them.
S1 = 'spam'
S2 = 'spam'

# As a rule of thumb, the == operator is what you will want to use for almost all equality
# checks; is is reserved for highly specialized roles. 

# Comparison operator is applied to nested, LEFT to RIGHT
a = ['a', ('b', 2, 10)]
b = ['a', ('b', 3, 4)]
print(a > b, a == b, a < b)  # (False, False, True) 

# Nonnumeric mixed-type magnitude comparisons (e.g., 1 < 'spam') are errors in
# Python 3.X. They are allowed in Python 2.X, but use a fixed but arbitrary ordering
# rule based on type name string. 

# Will be an error in Python 3
# print(11 >= '11')  # False, 2.X compares by type name string: int, str
# print(11 <= '11')  # True

# Dictionaries aren't comparable in Python 3
D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
print(D1 == D2)        # False (Python 2/2)
# print(D1 < D2)         # True (Python 2), TypeError (Python 3)

# In Python, as in most programming languages, an integer 0 represents false, and an
# integer 1 represents true.
# - Numbers are false if zero, and true otherwise.
# - Other objects are false if empty, and true otherwise.

print('-' * 10 + "A9" + '-' * 10)


print(0 == False)     # True
print(1 == True)      # True
print(2 == True)      # False

print(0 is False)     # False
print(1 is True)      # False
print(2 is True)      # False

print('-' * 10 + "A10" + '-' * 10)

# Empty objects EVALUATE to False, its "truthiness" value is False.

print([] == False)          # False
print(bool([]) == False)    # True
print(['a'] == True)        # False
print(bool(['a']) == True)  # True

# Boolean results are used automatically by if statements and other selection tools
if []:
    print("Empty. True.")   # Don't go here
else:  
    print("Empty. False.")  # Empty. False.

# None is the only value of a special data type in Python and typically serves as an empty
# placeholder (much like a NULL pointer in C).
# Keep in mind that None does not mean "undefined." That is, None is something, not
# nothing (despite its name!)-it is a real object and a real piece of memory that is created
# and given a built-in name by Python itself.

print('-' * 10 + "A11" + '-' * 10)

L = [None] * 3              # [None, None, None] - good way to initialize list with undefined yet content
print(L)
print(L == None)            # False
print(L is None)            # False

# A call to the built-in function type(X) returns the type object of object X

print('-' * 10 + "A12" + '-' * 10)

print(type([1]) == type([]))  # True
print(isinstance([1], list))  # True

# We can compare non-built-in types with a package 'types'

import types
def f(): pass
print(type(f) == types.FunctionType) # True

# GOTCHAS

print('-' * 10 + "GOTCHA 1: Assignment creates references, not copies" + '-' * 10)
# Need to use copy(), [:] etc
L = [1, 2, 3]
M = ['x', L, 'y']
print(M)                # ['x', [1, 2, 3], 'y']
L[1] = 0
print(M)                # ['x', [1, 0, 3], 'y']

print('-' * 10 + "GOTCHA 2: Repetition adds one level deep" + '-' * 10)
# Repeating a sequence is like adding it to itself a number of times. However, when
# mutable sequences are nested, the effect might not always be what you expect. 
L = [4, 5, 6]
x = L * 3        # like [4, 5, 6] + [4, 5, 6] + [4, 5, 6]
print(x)         # [4, 5, 6, 4, 5, 6, 4, 5, 6]

y = [L] * 3      # like [L] + [L] + [L]
print(y)         # [[4, 5, 6], [4, 5, 6], [4, 5, 6]]

L[1] = 0
print(x)         # [4, 5, 6, 4, 5, 6, 4, 5, 6] - no reference to the original list
print(y)         # [[4, 0, 6], [4, 0, 6], [4, 0, 6]]

# Even more subtly, although Y doesn't share an object with L anymore, it still embeds
# four references to the same copy of it.
L = [1, 2, 3]
Y = [list(L)] * 3
print(Y)
Y[0][1] = 99
print(Y)         # [[1, 99, 3], [1, 99, 3], [1, 99, 3]]

# Repetition, concatenation and slicing copy only the top level of
# their operand objects

print('-' * 10 + "GOTCHA 3: Beware of cyclic data structures" + '-' * 10)
# Reference to itself

L = ['grail']
L.append(L)
print(L)         # ['grail', [...]]

print('-' * 10 + "GOTCHA 4: You can't change an immutable object in place" + '-' * 10)
# Instead, you construct a new object with slicing, concatenation, and so on, and assign it
# back to the original reference, if needed
T = (1, 2, 3)       # Tuple supports slicing
#T[2] = 4           # Error!
T = T[:2] + (4,)    
print(T)            # OK: (1, 2, 4)

print('-' * 10 + 'Exercises' '-' * 10) 

# 1.Immutable types
S = "spam"
# Assignment that changes the string to "slam", using only slicing and concatenation
S = S[0:1] + 'l' + S[2:]
print(S)
# Could you perform the same operation using just indexing and concatenation?
S = "spam"
S = S[0] + 'l' + S[2] + S[3]
print(S)
# How about index assignment?
S = "spam"
#S[1] = 'l'          # TypeError: 'str' object does not support item assignment

# 2. Generic operations

#a. What happens when you try to use the + operator on different/mixed types (e.g., string + list, list + tuple)?
s = 'abc'
l = ['d', 'e']
t = ('f', )
d = {'a':1, 'b':2}
#rv = l + s            # TypeError: can only concatenate list (not "str") to list
#rv = l[0:2] + (40,)   # TypeError: can only concatenate list (not "tuple") to list

#b. Does + work when one of the operands is a dictionary?
#rv = d + s            # TypeError: unsupported operand type(s) for +: 'dict' and 'str'

#c. How about using the keys method on lists? (Hint: what does append assume about its subject object?)
rv = l + d.keys()     
print(rv)              # ['d', 'e', 'a', 'b'], because keys() returns list of keys
#rv = s + d.keys()     # TypeError: cannot concatenate 'str' and 'list' objects 



