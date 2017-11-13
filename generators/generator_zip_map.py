
print("-" * 20 + "#1 zip and map" + "-" * 20)

# list() is used for compatibility with Python 3.X

S1 = 'abc'
S2 = 'xyz123'
# [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(list(zip(S1, S2)))             

# 1-ary tuples
# [(-2,), (-1,), (0,), (1,), (2,)]
print(list(zip([-2, -1, 0, 1, 2])))

rv = map(abs, [-2, -1, 0, 1, 2])
print(list(rv))  # [2, 1, 0, 1, 2]

# map passes paired items to function
rv = map(pow, [1, 2, 3, 4], [1, 2, 3, 4])
print(list(rv))  # [1, 4, 27, 256]

# This works differently in Python 3.X and 2.X
# rv = map(pow, [1, 2, 3], [1, 2, 3, 4])
# [1, 4, 27] in Python 3.X - truncation
# TypeError: in Python 2.X


print("-" * 20 + "#2 Coding your own map" + "-" * 20)

# In function definition * is pack to tuple
# In function invocation * is unpack arguments from tuple 

def mymap1(func, *seqs):
    res = []
    # print('seqs: ', seqs)      #  seqs = ([0, 1, 2, 3], [2, 2, 2, 2])
    for x in zip(*seqs):         # *seqs =  [0, 1, 2, 3], [2, 2, 2, 2]
        res.append(func(*x))     # x = (0, 2)....(3, 2), invoke func
    return res

print(mymap1(abs, [-2, -1, 0, 1, 2]))           #[2, 1, 0, 1, 2]
print(mymap1(pow, [0, 1, 2, 3], [2, 2, 2, 2]))  #[0, 1, 4, 9] 

def mymap2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap2(abs, [-2, -1, 0, 1, 2]))           #[2, 1, 0, 1, 2]
print(mymap2(pow, [0, 1, 2, 3], [2, 2, 2, 2]))  #[0, 1, 4, 9] 

# Both of the preceding mymap versions build result lists all at once,
# though, and this can waste memory for larger lists. Now that we know 
# about generator functions and expressions, it's simple to recode both 
# these alternatives to produce results on demand instead

def mymap3(func, *seqs):
    for x in zip(*seqs):
        yield func(*x)

print(list(mymap3(abs, [-2, -1, 0, 1, 2])))           #[2, 1, 0, 1, 2]
print(list(mymap3(pow, [0, 1, 2, 3], [2, 2, 2, 2])))  #[0, 1, 4, 9]

def mymap4(func, *seqs):
    return (func(*args) for args in zip(*seqs))

print(list(mymap4(abs, [-2, -1, 0, 1, 2])))           #[2, 1, 0, 1, 2]
print(list(mymap4(pow, [0, 1, 2, 3], [2, 2, 2, 2])))  #[0, 1, 4, 9]

print("-" * 20 + "#3 Coding your own zip" + "-" * 20)

def myzip1(*seqs):
    # print(seqs)                            # ('abc', 'xyz123')
    seqs = [list(S) for S in seqs]        
    # print(seqs)                            # [['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]
    res = []
    while all(seqs):                         # no list in list is empty - so myzip() truncates
        # print('seqs here: ', seqs)
        # seqs here:  [['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]
        # seqs here:  [['b', 'c'], ['y', 'z', '1', '2', '3']]
        # seqs here:  [['c'], ['z', '1', '2', '3']]
        # http://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
        res.append(tuple(S.pop(0) for S in seqs))
    return res

S1, S2 = 'abc', 'xyz123'
print(myzip1(S1, S2))          # [('a', 'x'), ('b', 'y'), ('c', 'z')]

# It's just as easy to turn them into generators with yield so that
# they each return one piece of their result set at a time

def myzip2(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

S1, S2 = 'abc', 'xyz123'
# list() is required to build get all the values
# from the generator
print(list(myzip2(S1, S2)))          # [('a', 'x'), ('b', 'y'), ('c', 'z')]

# An alternative implementation of our zip and map emulators-rather than deleting
# arguments from lists with the pop method, the following versions do their job
# by calculating the minimum and maximum argument lengths

def myzip3(*seqs):
    minlen = min([len(S) for S in seqs])
    return [tuple(x[i] for x in seqs) for i in range(minlen)]

S1, S2 = 'abc', 'xyz123'
print(myzip3(S1, S2))                # [('a', 'x'), ('b', 'y'), ('c', 'z')]

# To turn these functions themselves into generators instead of list builders, use
# parentheses instead of square brackets again. It takes a list call to activate 
# the generators and other iterables to produce their results

def myzip4(*seqs):
    minlen = min([len(S) for S in seqs])
    return (tuple(x[i] for x in seqs) for i in range(minlen))

S1, S2 = 'abc', 'xyz123'
print(list(myzip4(S1, S2)))          # [('a', 'x'), ('b', 'y'), ('c', 'z')]

print("-" * 20 + "#4 del() vs pop()" + "-" * 20)

# Use del to remove an element by index, pop() to remove it by index if you need
# the returned value, and remove() to delete an element by value. 
# The latter requires searching the list, and raises ValueError if no such value 
# occurs in the list.

a = ['a', 'b', 'b', 'c', 'd']
#remove first occurence
b = a.remove('b')
print(a)                # ['a', 'b', 'c', 'd'
print(b)                # None

a = ['a', 'b', 'b', 'c', 'd']
b = a.pop(0)
print(a)               # ['b', 'b', 'c', 'd']
print(b)               # a

a = ['a', 'b', 'b', 'c', 'd']
del a[3]
print(a)               # ['a', 'b', 'b', 'd']


'''
print "-"*20 + "#6 set and dict comprehensions" + "-"*20

print {x * x for x in range(10)}       #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
print {x: x * x for x in range(10)}    #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


print "-"*20 + "#7 Scopes and Comprehension Variables" + "-"*20


# Python 2.X is the same in this regard, except that list comprehension variables are not
# localized-they work just like for loops and keep their last iteration values, but are also
# open to unexpected clashes with outside names. Generator, set, and dictionary forms
# localize names as in 3.X:


x = 99
[x for x in range(5)]
print x  #4 in python 2, 99 in python 3

x = 99
for x in range(5): pass
print x  #4

x = 99
(x for x in range(5))
print x  #99

print "-"*20 + "#8 Comprehending Set and Dictionary Comprehensions" + "-"*20

print {xx * xx for xx in range(10)}             #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
print set(xx * xx for xx in range(10))          #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])

print {xx: xx * xx for xx in range(10)}         #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print dict((xx, xx * xx) for xx in range(10))   #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#print xx #NameError: name 'xx' is not defined
'''
