
print("-" * 20 + "#1 Generator Functions and Generator Expressions" + "-" * 20)

# Generator functions (available since 2.3) are coded as normal def statements, but
# use yield statements to return results one at a time, suspending and resuming their
# state between each.

# Generator expressions (available since 2.4) are similar to the list comprehensions
# of the prior section, but they return an object that produces results on demand
# instead of building a result list.

# Because neither constructs a result list all at once, they save memory space and allow
# computation time to be split across result requests. 


print("-" * 20 + "#2 Generator Functions: yield Versus return" + "-" * 20)

# Generator functions are like normal functions in most respects, and in fact are coded
# with normal def statements. However, when created, they are compiled specially into
# an object that supports the iteration protocol. And when called, they don't return a
# result: they return a result generator that can appear in any iteration context.

# Python for loops, and all other iteration contexts, use this iteration protocol to step
# through a sequence or value generator, if the protocol is supported (if not, iteration
# falls back on repeatedly indexing sequences instead). Any object that supports this
# interface works in all iteration tools.

# To support this protocol, functions containing a yield statement are compiled specially
# as generators - they are not normal functions, but rather are built to return an object
# with the expected iteration protocol methods. When later called, they return a 
# generator object that supports the iteration interface with an automatically created 
# method named __next__ to start or resume execution.

# An iterable object's iterator is fetched initially with the iter built-in function,
# though this step is a no-op for objects that are their own iterator.

# The chief code difference between generator and normal functions is that a generator
# yields a value, rather than returning one-the yield statement suspends the function
# and sends a value back to the caller, but retains enough state to enable the function to
# resume from where it left off. When resumed, the function continues execution 
# immediately after the last yield run. From the function's perspective, this allows its code
# to produce a series of values over time, rather than computing them all at once and
# sending them back in something like a list.

# Generator functions may also have a return statement that, along with falling off the
# end of the def block, simply terminates the generation of values - technically, by raising
# a StopIteration exception after any normal function exit actions. From the caller's
# perspective, the generator's __next__ method resumes the function and runs until either
# the next yield result is returned or a StopIteration is raised.

# The net effect is that generator functions, coded as def statements containing yield
# statements, are automatically made to support the iteration object protocol and thus
# may be used in any iteration context to produce results over time and on demand.

def gensquares(N):
    for i in range(N):
        yield i ** 2

# To end the generation of values, functions either use a return statement with no value
# or simply allow control to fall off the end of the function body.

for i in gensquares(5):
    print(i, ":"),    # (0, ':') (1, ':') (4, ':') (9, ':') (16, ':')
print()   

# Notice that the top-level iter call of the iteration protocol isn't required here because
# generators are their own iterator, supporting just one active iteration scan. To put that
# another way generators return themselves for iter, because they support next directly.
# This also holds true in the generator expressions

y = gensquares(5)
print(iter(y) is y)   # True
print(next(y))        # 0
print(next(y))        # 1
print(next(y))        # 4
print(next(y))        # 9
print(next(y))        # 16
# print(next(y))      # StopIteration

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

# All iteration contexts would work
print tuple(ups('aaa,bbb,ccc'))                            # ('AAA', 'BBB', 'CCC')
print {i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}   # {0: 'AAA', 1: 'BBB', 2: 'CCC'}

print("-" * 20 + "#3 Generator Functions: send Versus next" + "-" * 20)

# When this extra protocol is used, values are sent into a generator G by calling
# G.send(value). The generator's code is then resumed, and the yield expression in the
# generator returns the value passed to send. If the regular G.__next__() method (or its
# next(G) equivalent) is called to advance, the yield simply returns None.

def gen():
    for i in range(10):
        X = yield i  # (*) 
        print(X)     # (**)
        
G = gen()
rv = next(G)       # Nothing is printed, because gen() did "yield 0" and (**) wasn't reached yet 
print rv           # 0  - result of yield 0
rv = G.send(77)    # 77 - X in (*) equals to 77 we print it (**) and go to the next iteration
print rv           # 1  - yield 1
rv = G.send(88)    # 88
print rv           # 2
rv = next(G)       # None - if we don't pass any value with send, then X is None 
print rv           # 3

# There are also throw and close methods!

print("-" * 20 + "#4 Generator Expressions: Iterables Meet Comprehensions" + "-" * 20)


# In fact, at least on a functionality basis, coding a list comprehension is essentially the
# same as wrapping a generator expression in a list built-in call to force it to produce
# all its results in a list at once:

print list(x ** 2 for x in range(4))   #[0, 1, 4, 9]

# Operationally, however, generator expressions are very different from ListCom: instead of 
# building the result list in memory, they return a generator object-an automatically created
# iterable. This iterable object in turn supports the iteration protocol to yield one piece
# of the result list at a time in any iteration context. The iterable object also retains 
# generator state while active-the variable x in the preceding expressions, along with the
# generator's code location.

G = (x ** 2 for x in range(4))
print iter(G) is G   # True, __iter__ returns itself
print next(G)        # 0
print next(G)        # 1
print next(G)        # 4
print next(G)        # 9
#print next(G) #StopIteration

# We don't typically see the next iterator machinery under the hood of a generator
# expression like this because for loops trigger it for us automatically
for num in (x ** 2 for x in range(4)):
    print("%s, %s" % (num, num / 2.0))  # important to divide by 2.0

# 0, 0.0
# 1, 0.5
# 4, 2.0
# 9, 4.5

# Syntactically, parentheses are not required around a generator expression
# that is the sole item already enclosed in parentheses used for other purposes-like those
# of a function call.

print ''.join(x.upper() for x in "aaa,bbb,ccc".split(',')) # AAABBBCCC
print sorted(x ** 2 for x in range(4))                     # parentheses are optional
print sorted((x ** 2 for x in range(4)), reverse = True)   # [9, 4, 1, 0], here parentheses are required

# On the other hand, generator expressions may also run slightly slower than list 
# comprehensions in practice, so they are probably best used only for very large result sets,
# or applications that cannot wait for full results generation.


print("-" * 20 + "#5 Generator Expressions: versus map" + "-" * 20)








print("-" * 20 + "#4 Generators Are Single-Iteration Objects" + "-" * 20)

# A subtle but important point: both generator functions and generator expressions are
# their own iterators and thus support just one active iteration-unlike some built-in
# types, you can't have multiple iterators of either positioned at different locations in the
# set of results.

G = (c * 4 for c in "SPAM")

'''
If you iterate over the results stream manually with multiple iterators, they will all point
to the same position:
'''

I1 = iter(G)
print next(I1)    #SSSS
print next(I1)    #PPPP
I2 = iter(G)
print next(I2)    #AAAA

print list(I1)    #['MMMM']
#print next(I1)   #StopIteration

I3 = iter(G)
#print next(I3)   #StopIteration

I3 = iter(c * 4 for c in "SPAM")
print next(I3)    #SSSS


print "-"*20 + "#5 Generation in Built-in Types, Tools, and Classes" + "-"*20

D = {'a':1, 'b':2, 'c':3}
x = iter(D)
#no order here
print next(x) #a
print next(x) #c
print next(x) #b

for key in D:
    print(key, D[key])

''' 
('a', 1)
('c', 3)
('b', 2)
'''

'''
Iteration contexts like for loops accept any iterable that has the expected methods,
whether user-defined or built-in.
'''

def f(a, b, c):
    print('%s, %s and %s' % (a, b, c))
    
f(0, 1, 2)
f(*range(3))
f(*(i for i in range(3)))


D = dict(a = 'Bob', b = 'dev', c = 40.5)
print D
f(a = 'Bob', b = 'dev', c = 40.5) #Bob, dev and 40.5
f(**D)                            #Bob, dev and 40.5
f(*D)                             #a, c and b

'''
Technically speaking, sequence assignment actually supports any iterable object on the
right, not just any sequence. This is a more general category that includes collections
both physical (e.g., lists) and virtual (e.g., a file's lines), which was defined briefly in
Chapter 4 and has popped up in passing ever since. We'll firm up this term when we
explore iterables in Chapter 14 and Chapter 20.
'''

'''
To generalize a generator expression for an arbitrary subject, wrap it in a simple
function that takes an argument and returns a generator that uses it
'''

s = 'spam'
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print F(s)                      #<generator object <genexpr> at 0xb73603c4>
print list(F(s))                #['spam', 'pams', 'amsp', 'mspa']
print list(F([1, 2, 3]))        #[[1, 2, 3], [2, 3, 1], [3, 1, 2]]

print "-"*20 + "#6 Example: Emulating zip and map with Iteration Tools" + "-"*20

S1 = 'abc'
S2 = 'xyz123'
print zip(S1, S2)       #[('a', 'x'), ('b', 'y'), ('c', 'z')]


#map passes paired items to function, truncates
print map(pow, [0, 1, 2, 3], [2, 2, 2, 2])    #[0, 1, 4, 9]

'''
In function definition * is pack to tuple
In function invocation * is unpack arguments from tuple 
'''

def mymap(func, *seqs):
    res = []
    print 'seqs: ', seqs         # seqs = ([0, 1, 2, 3], [2, 2, 2, 2])
    for x in zip(*seqs):         #*seqs = [0, 1, 2, 3], [2, 2, 2, 2]
        res.append(func(*x))     #x = (0, 2)....(3, 2)
    return res

print mymap(abs, [-2, -1, 0, 1, 2])             #[2, 1, 0, 1, 2]
print mymap(pow, [0, 1, 2, 3], [2, 2, 2, 2])    #[0, 1, 4, 9] 

def myzip(*seqs):
    print seqs                            #('abc', 'xyz123')
    seqs = [list(S) for S in seqs]        
    print seqs                            #[['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]
    res = []
    while all(seqs): #no list in list is empty - so myzip() truncates
        print 'seqs here: ', seqs
        #seqs here:  [['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]
        #seqs here:  [['b', 'c'], ['y', 'z', '1', '2', '3']]
        #seqs here:  [['c'], ['z', '1', '2', '3']]
        #http://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
        res.append(tuple(S.pop(0) for S in seqs))
    return res

S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))          #[('a', 'x'), ('b', 'y'), ('c', 'z')]

'''
Use del to remove an element by index, pop() to remove it by index if you need the returned value, and remove() to delete an element by value. 
The latter requires searching the list, and raises ValueError if no such value occurs in the list.
'''

a = ['a', 'b', 'b', 'c', 'd']
#remove first occurence
b= a.remove('b')      #['a', 'b', 'c', 'd']
print a               #None
print b
#b= a.remove(2)       #ValueError: list.remove(x): x not in list

a = ['a', 'b', 'b', 'c', 'd']
b = a.pop(0)
print a               #['b', 'b', 'c', 'd']
print b               #a

a = ['a', 'b', 'b', 'c', 'd']
del a[3]
print a               #['a', 'b', 'b', 'd']


print "-"*20 + "#7 set and dict comprehensions" + "-"*20

print {x * x for x in range(10)}       #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
print {x: x * x for x in range(10)}    #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


print "-"*20 + "#8 Scopes and Comprehension Variables" + "-"*20

'''
Python 2.X is the same in this regard, except that list comprehension variables are not
localized-they work just like for loops and keep their last iteration values, but are also
open to unexpected clashes with outside names. Generator, set, and dictionary forms
localize names as in 3.X:
'''

x = 99
[x for x in range(5)]
print x  #4 in python 2, 99 in python 3

x = 99
for x in range(5): pass
print x  #4

x = 99
(x for x in range(5))
print x  #99

print "-"*20 + "#9 Comprehending Set and Dictionary Comprehensions" + "-"*20

print {xx * xx for xx in range(10)}             #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])
print set(xx * xx for xx in range(10))          #set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])

print {xx: xx * xx for xx in range(10)}         #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print dict((xx, xx * xx) for xx in range(10))   #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#print xx #NameError: name 'xx' is not defined






