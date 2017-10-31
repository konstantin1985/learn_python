


print('-' * 10 + "A.1. Iterator is exhausted" + '-' * 10)

M = map(lambda x: 2 ** x, range(3))
for i in M:
    print(i), # 1 2 4; ok in p2 and p3
print

# In p2 map() returns list, in p3, map() returns the iterable object
# So here for p3 there won't be anything, because values are exhausted
# during the first pass through the iterable object
for i in M:
    print(i), # 1 2 4 in p2, empty in 3.x - map iterator is empty
print

print('-' * 10 + "A.2. Range iterator" + '-' * 10)

# It's important to see how the range() object differs from the built-ins described in this
# section-it supports len and indexing, it is not its own iterator (you make one with
# iter when iterating manually), and it supports MULTIPLE iterators over its result that
# remember their positions independently

# In p2 range() return list, in p3 range() returns iterable
R = range(5)
print(R)   # p2: [0, 1, 2, 3, 4], p3: range(0, 5)
# next(R)  # TypeError: list object is not an iterator, range() isn't its own iterator

I = iter(R)
print(next(I))  # p2,p3: 0
print(next(I))  # p2,p3: 1
print(next(I))  # p2,p3: 2

print(list(R))  # p2,p3: [0, 1, 2, 3, 4], force list

print(R[1])     # p2,p3: 1, but in a book it says that it's impossible

print('-' * 10 + "A.3. map, zip and filter" + '-' * 10)

# All three not only process iterables, as in 2.X, but also RETURN iterable results in 3.X. 
# Unlike range, though, THEY ARE THEIR OWN ITERATORS-after you step through their results once, 
# they are exhausted.
f = filter(bool, ['abc', '', 'd'])
print(f)  # p2: ['abc', 'd'], p3: <filter object at 0xb70914cc>

# By contrast, in 3.X zip, map, and filter do not support multiple active iterators on the
# same result; because of this the iter call is optional for stepping through such objects'
# results-their iter is themselves (in 2.X these built-ins return multiple-scan lists so the
# following does not apply):
z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(z)
I2 = iter(z)
print(next(I1))  # (1, 10)
print(next(I1))  # (2, 11)
print(next(I2))  # p2: (1, 10), p3: (3, 12)

# We can fix this behavior by invoking list()

print('-' * 10 + "A.4. map, zip and filter" + '-' * 10)

D = {3: 'a', 2: 'b', 1: 'c'}
# next(D)  # TypeError: dict object is not an iterator - dictionary isn't its own iterator

I1 = iter(D)
I2 = iter(D)
print(next(I1))  # 1 (one of the keys, they aren't stored sequentially)
print(next(I1))  # 2 (another key, they aren't stored sequentially)
print(next(I2))  # 1 (no problem here, dictionary isn't an iterator itself)

# "Best practice" key sorting 
for k in sorted(D):
    print(k, D[k]),  # (1, 'c') (2, 'b') (3, 'a')
print()

# Not the best practice, don't work in p3, 
# Book: need to convert with list()
# In practice it works
for k in sorted(D.keys()): 
    print(k, D[k]),
print()

# To learn about iterators later:
# User-defined functions can be turned into iterable generator functions, with yield statements.
# List comprehensions morph into iterable generator expressions when coded in parentheses.
# User-defined classes are made iterable with __iter__ or __getitem__ operator over-loading.

