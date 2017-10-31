# Assignments create object references.
# They always create references to objects instead of copying the objects. 
# Because of that, Python variables are more like pointers than data storage areas.

# Names are created when first assigned

# Names must be assigned before being referenced

# Some operations perform assignments implicitly 
# (without = statement), like function and class definition

print('-' * 10 + "A.1. Positional assignment" + '-' * 10)

spam, ham = 'yum', 'YUM'
print(spam, ham)  # ('yum', 'YUM')

[spam, ham] = ['a', 'b']
print(spam, ham)  # ('a', 'b')

# A way to swap value of two variables without creating a temporary variable
nudge = 1
wink = 2
nudge, wink = wink, nudge  # tuples: swap values
print(nudge, wink)         # (2, 1)

print('-' * 10 + "A.2. Sequence assignment" + '-' * 10)
# Any sequence of names can be assigned to any sequence of values,
# and Python assigns the items one at a time by.

a, b, c, d = 'spam'
print(a, b, c, d) # ('s', 'p', 'a', 'm')

# Accept any type of sequence (iterable) on the right as long as it is of the same
# length as the sequence on the left.
[a, b, c] = (1, 2, 3)
print(a, c)  # (1, 3)
(a, b, c) = "ABC"
print(a, c)  # ('A', 'C')

# We can use slicing
s = "SPAM"
a, b, c = list(s[:2]) + [s[2:]]
print(a, b, c)    # ('S', 'P', 'AM')

# Python pairs the first string on the right ('SP') with the first tuple on the left ((a, b))
# and assigns one character at a time, before assigning the entire second string ('AM') to
# the variable c all at once.
s = "SPAM"
(a, b), c = s[:2], s[2:]
print(a, b, c)    # ('S', 'P', 'AM')

# Python equivalent to the enumerated data types
red, green, blue = range(3)
print(red, blue)  # (0, 2)
# list(range(3))  # in Python 3.x

# Splitting a sequence into its front and the rest
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

print('-' * 10 + "A.3. Multitarget assignment" + '-' * 10)

a = b = c = 'spam'
print(a, b, c)  # ('spam', 'spam', 'spam')

# Here, changing b only changes b because numbers are immutable.
a = b = 0
b = b + 1
print(a, b)  # (0, 1)

# Different for mutable objects
a = b = []
b.append(42)
print(a, b)  # ([42], [42])

# Can fix it by initialing mutable objects in separate statements
a = []  # or a, b = [], []
b = []
b.append(42)
print(a, b)  # ([], [42])

print('-' * 10 + "A.4. Augmented assignment" + '-' * 10)

L = [1, 2]
L = L + [3]  # concatenate slower
print(L)
L.append(4)
print(L)     # faster, but in place
L = L + [5, 6]
print(L)     # [1, 2, 3, 4, 5, 6]
L.extend([7, 8])
print(L)     # [1, 2, 3, 4, 5, 6, 7, 8]

# When we use augmented assignment to extend a list,
# Python automatically calls the quicker extend method
L += [9, 10]
print(L)     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# += for a list is like extend, not like + and =
L = []
# L = [] + 'spam'  # TypeError: can only concatenate list (not "str") to list
L.extend('abc')    # ['a', 'b', 'c']
print(L)
L += 'spam'
print(L)           # ['a', 'b', 'c', 's', 'p', 'a', 'm']

# + concatenation always makes a new object, += is an in-place change
L = [1, 2]
M = L             # L and M reference the same object
L = L + [3, 4]    # concatenation makes a new object
print(L, M)       # ([1, 2, 3, 4], [1, 2])

L = [1, 2]
M = L
L += [3, 4]
print(L, M)       # ([1, 2, 3, 4], [1, 2, 3, 4])

# This only matters for mutables like lists and dictionaries, and it is a fairly obscure case
# (at least, until it impacts your code!). As always, make copies of your mutable objects
# if you need to break the shared reference structure.

print('-' * 10 + "A.5. Objects vs names" + '-' * 10)
# Objects have a type (e.g., integer, list) and may be mutable or not. Names (a.k.a. variables), on the other hand,
# are always just references to objects; they have no notion of mutability and have no
# associated type information, apart from the type of the object they happen to reference
# at a given point in time.



