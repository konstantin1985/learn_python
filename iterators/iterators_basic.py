import os

print('-' * 10 + "A.1. Iterator protocol" + '-' * 10)

# An object is considered iterable if it is either a physically stored sequence, or
# an object that produces one result at a time in the context of an iteration tool like a for loop.
# In a sense, iterable objects include both physical sequences and virtual se-
# quences computed on demand.

# Term iterable to refer to an object that supports
# the iter call, and iterator to refer to an object returned by an iterable on
# iter that supports the next(I) call

# This interface is most of what we call the iteration protocol in Python. Any object with
# a __next__ method to advance to a next result, which raises StopIteration at the end
# of the series of results, is considered an iterator in Python. Any such object may also
# be stepped through with a for loop or other iteration tool, because all iteration tools
# normally work internally by calling __next__ on each iteration and catching the StopIt
# eration exception to determine when to exit.

f = open("myfile.txt", 'w')
f.write("First line\n")
f.write("Second line\n")
f.close()

f = open("myfile.txt", 'r')
print(f.next())   # First line
print(f.next())   # Second line
# print(f.next()) # StopIteration

# iterators run at C language speed inside Python, whereas the while loop version runs Python
# byte code through the Python virtual machine.

# In Python 2.X, the iteration method is named
# X.next() instead of X.__next__(). For portability, a next(X) built-in
# function is also available in both Python 3.X and 2.X (2.6 and later), and
# calls X.__next__() in 3.X and X.next() in 2.X.

# Some objects are both iterable and iterator, returning themselves for the iter()
# call, which is then a no-op. For example files, but not lists.
f = open("myfile.txt", 'r')
print(iter(f) is f)  # True

# Lists and many other built-in objects, though, are not their own iterators because they
# do support multiple open iterations-for example, there may be multiple iterations in
# nested loops all at different positions.
L = [1, 2, 3]
print(iter(L) is L)  # False
I = iter(L)
print(I.next())   # 1
print(I.next())   # 2
print(I.next())   # 3
#print(I.next())  # StopIteration

# In 3.x ranges are iterable, i.e. print(R) would give 'range(0, 5)'
# In 2.x it's a list, but we could iterate nevertheless
R = range(100,200)   
I  = iter(R)
print(next(I))  # 100
print(next(I))  # 101
print(next(I))  # 102





print('-' * 10 + "A.2. Iterator and dictionaries" + '-' * 10)

# In recent versions of Python, though, dictionaries are iterables with an iterator that
# automatically returns one key at a time in an iteration context

D = {'a': 1, 'b': 2, 'c': 3}
I = iter(D)     # Get iterator
print(next(I))  # a
print(next(I))  # b
print(next(I))  # c
# print(next(I))  # StopIteration

for key in D:
    print(key, D[key]),  # ('a', 1) ('c', 3) ('b', 2)
print

print('-' * 10 + "A.3. Iterator and popen" + '-' * 10)

P = os.popen('dir')
I = iter(P)
print(next(I)) 



print('-' * 10 + "A.4. Clean files after module" + '-' * 10)

os.remove('myfile.txt')