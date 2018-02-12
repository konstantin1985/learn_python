


# USEFUL LINKS:
# https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python

# x = [1, 2, 3]
# x.append([4, 5])
# print (x)                              # [1, 2, 3, [4, 5]]

# x = [1, 2, 3]
# x.extend([4, 5])
# print (x)                              # [1, 2, 3, 4, 5]



# Applies a function to items in a sequence and collects all the results in a new list

print(list(map(abs, [-1, -2, 0, 1, 2]))) # [1, 2, 0, 1, 2]

# When using a list, you can change its contents by assigning to either a particular item
# (offset) or an entire section (slice)

L = ['spam', 'Spam', 'SPAM!']
L[0:2] = ['eat', 'more']
print(L)                                 # ['eat', 'more', 'SPAM!']

L = [1, 4, 5, 3]
L[1:1] = [6, 7]
print(L)                                 # [1, 6, 7, 4, 5, 3]

L = [1]
L[:0] = [2, 3, 4]
print(L)                                 # [2, 3, 4, 1] Insert all at :0, an empty slice at front
L[len(L):] = [5, 6, 7]                   # Insert all at len(L):, an empty slice at end
print(L)                                 # [2, 3, 4, 1, 5, 6, 7]
L.extend([8, 9, 10])
print(L)                                 # [2, 3, 4, 1, 5, 6, 7, 8, 9, 10]

L = [1, 2, 3]
L[1:] = [4, 5, 6]
print(L)                                 # [1, 4, 5, 6]

L = [1, 2, 3]
L[1:1] = [4, 5, 6]
print(L)                                 # [1, 4, 5, 6, 2, 3]


# Methods are functions (really, object attributes that reference functions) 
# that are associated with and act upon particular objects. Methods provide type-specific tools
L = ['eat', 'more', 'SPAM!']
L.append('please')
print(L)                                 # ['eat', 'more', 'SPAM!', 'please']
print(L.sort())                          # ['SPAM!', 'eat', 'more', 'please']

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)
print(L)                                 # ['aBe', 'ABD', 'abc']

# Partly because of such constraints (sort() sort in place and doesn't return a new list), sorting is also 
# available in recent Pythons as a built-in function, which sorts any collection (not just lists) and returns a new list for the result
L = ['abc', 'ABD', 'aBe']
B = sorted(L, key=str.lower, reverse=True)
print(B)                                 # ['aBe', 'ABD', 'abc']

L = [1, 2, 3, 4, 5]
a = L.pop()
print(a, L)                              # (5, [1, 2, 3, 4])
L = [1, 2, 3, 4]
print(L.reverse())                       # None! Because it doesn't return a new list
print(L)                                 # [4, 3, 2, 1]


# For now, it's enough to know that extend adds many items, and append adds one.
# The list pop method is often used in conjunction with append to implement a quick last-
# in-first-out (LIFO) stack structure. The end of the list serves as the top of the stack
L = []
L.append(1)
L.append(2)
print(L)           # [1, 2]
a = L.pop()
print(a, L)        # (2, [1])

# Some methods could work by position
L = ['spam', 'eggs', 'ham']
L.index('eggs')              # 1 - index of the element
L.insert(1, 'toast')
print(L)                     # ['spam', 'toast', 'eggs', 'ham']
L.remove('eggs')
print(L)                     # ['spam', 'toast', 'ham']
L.pop(1)
print(L)                     # ['spam', 'ham']
print(L.count('spam'))       # 1 - number of occurences

# How delete works
L = ['spam', 'eggs', 'ham', 'toast']
del L[0]
print(L)                     # ['eggs', 'ham', 'toast']
del L[1:]
print(L)                     # ['eggs']

print('-' * 10 + "Difference between list() and []" + '-' * 10)
s = "SPAM"
print(list(s[:2]))           # ['S', 'P']
print([s[2:]])               # ['AM']

print('-' * 10 + "Difference between append() and []" + '-' * 10)

# In both cases, concatenation is less prone to the side effects of shared object references
# but will generally run slower than the in-place equivalent.
# Concatenation operations must create a new object, copy in the list on the left, and then
# copy in the list on the right. By contrast, in-place method calls 
# simply add items at the end of a memory block.

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

print('-' * 10 + "Exercises" + '-' * 10)

# 1. Indexing, slicing, and del
L = ['a', 'b', 'c', 'd']
L[2] = []
print(L)                     # ['a', 'b', [], 'd']
# Recall that slice assignment deletes the slice and inserts the new value where it used to be
L[2:3] = []
print(L)                     # ['a', 'b', 'd']
del L[0]
print(L)                     # ['b', 'd']
del(L[1:])                   # ['b']
print(L)
L = ['a', 'b', 'c', 'd']
# L[1:2] = 1                 # TypeError: can only assign an iterable


 
