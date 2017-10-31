


print('-' * 10 + "A.1. Counter loops: range" + '-' * 10)

print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
# ([0, 1, 2, 3, 4], [2, 3, 4], [0, 2, 4, 6, 8])

print(list(range(-5, 5)))      # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(list(range(5, -5, -1)))  # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

# Use simple iteration if you can 
# As a general rule, use for instead of while whenever possible, and don't use range calls.
# in for loops except as a last resort. This simpler solution is almost always better. 
A = "spam"
for item in A: print(item),  # s p a m
print

# Because both slice to obtain parts to concatenate, they also work on
# any type of sequence, and return sequences of the same type as that being shuffled-
# if you shuffle a list, you create reordered lists
L = [1, 2, 3]
for i in range(len(L)):
    K = L[i:] + L[:i]
    print(K),  # [1, 2, 3] [2, 3, 1] [3, 1, 2]

# To visit every second character in S, for example, slice with a stride of 2
s = "abcdef"
for x in s[::2]:
    print(x),  # a c e
print

print('-' * 10 + "A.2. Modify list in a loop" + '-' * 10)

# In the next iteration, the loop body sets x to a different object, integer 2, 
# but it does not update the list where 1 originally came from; it's a piece of memory separate from the list.
L = [1, 2, 3, 4]
for x in L:
    x += 1
print(x, L)  # (5, [1, 2, 3, 4])

# To really change the list as we march across it, we need to use indexes so we can assign
# an updated value to each position as we go.
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] += 1
print(L)    # [2, 3, 4, 5]

# List comprehension will probably work faster, but doesn't change in place
L = [1, 2, 3, 4]
[x + 1 for x in L]
print(L)    # [1, 2, 3, 4]

print('-' * 10 + "A.3. Use zip()" + '-' * 10)

# Like range, zip is a list in Python 2.X, but an iterable object in 3.X 
# where we must wrapin a list call to display all its results at once
# The net effect is that we scan both L1 and L2 in our loop. We could achieve a similar
# effect with a while loop that handles indexing manually, but it would require more
# typing and would likely run more slowly than the for/zip approach.
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
for (x, y) in zip(L1, L2):
    print(x, '+', y, '=', x + y)
# (1, '+', 5, '=', 6)
# (2, '+', 6, '=', 8)
# (3, '+', 7, '=', 10)
# (4, '+', 8, '=', 12)

# We could zip() more than 2 items
T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(T3)                       # (7, 8, 9)
print(list(zip(T1, T2, T3)))    # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# zip truncates result tuples at the length of the shortest sequence when the
# argument lengths differ.
s1 = "abc"
s2 = "12345"
print(list(zip(s1, s2)))  # [('a', '1'), ('b', '2'), ('c', '3')]

# We can use zip() to create dictionaries
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))  # {'a': 1, 'c': 3, 'b': 2}

print('-' * 10 + "A.4. Use enumerate()" + '-' * 10)

# The enumerate function returns a generator object-a kind of object that supports the
# iteration protocol.
S = "abc"
E = enumerate(S)
print(next(E))    # (0, 'a')
print(next(E)) 
print(next(E))
# print(next(E))  # StopIteration error

print([c * i for (i, c) in enumerate(S)])  # ['', 'bb', 'ccc']

