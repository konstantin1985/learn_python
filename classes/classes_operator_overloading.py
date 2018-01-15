

# Specially named methods such as __init__, __add__, and __str__ are inherited by
# subclasses and instances, just like any other names assigned in a class. 
# If they re not coded in a class, Python looks for such names in all its 
# superclasses, as usual.

# Operator overloading methods are also all optional-if you
# don't code or inherit one, that operation is simply unsupported by your class, and
# attempting it will raise an exception. Some built-in operations, like printing, 
# have defaults 

# Although expressions trigger operator methods, be careful not to 
# assume that there is a speed advantage to cutting out the middleman and
# calling the operator method directly. In fact, calling the operator method
# directly might be twice as slow, presumably because of the overhead of
# a function call, which Python avoids or optimizes in built-in cases.
# x = L.__len__() is  twice slower than x = len(L)

# SUMMARY:

# 1. Classes can support iteration by defining (or inheriting) __getitem__ or __iter__.
# In all iteration contexts, Python tries to use __iter__ first, which returns an object
# that supports the iteration protocol with a __next__ method: if no __iter__ is found
# by inheritance search, Python falls back on the __getitem__ indexing method.

# 2. The __str__ and __repr__ methods implement object print displays. The former is
# called by the print and str built-in functions; the latter is called by print and str
# if there is no __str__, and always by the repr built-in, interactive echoes, and nested
# appearances. That is, __repr__ is used everywhere, except by print and str when
# a __str__ is defined. A __str__ is usually used for user-friendly displays;
# __repr__ gives extra details or the object's as-code form.

# 3. Slicing is caught by the __getitem__ indexing method: it is called with a slice object,
# instead of a simple integer index, and slice objects may be passed on or inspected
# as needed. In Python 2.X, __getslice__ (defunct in 3.X) may be used for two-limit
# slices as well.

# 4. In-place addition tries __iadd__ first, and __add__ with an assignment second. The
# same pattern holds true for all binary operators. The __radd__ method is also avail-
# able for right-side addition.

print("-" * 20 + "#0 Constructors and Expressions: __init__ and __sub__" + "-" * 20)

# Technically, instance creation first triggers the __new__ method, which
# creates and returns the new instance object, which is then passed into
# __init__ for initialization. Since __new__ has a built-in implementation
# and is redefined in only very limited roles, though, nearly all Python
# classes initialize by defining an __init__ method.

class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

X = Number(5)
Y = X - 2
print(Y.data)                                                        # 3

# To make __sub__ works for integers and Number it seems that the typecheck is required
# if isinstance(other, int):

print("-" * 20 + "#1 Indexing and Slicing: __getitem__ and __setitem__" + "-" * 20)

# When an instance X appears in and indexing expression like X[i], Python calls the 
# __getitem__ method inherited by the instance, passing X to the first argument and 
# the index in brackets to the second argument

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print X[2]               #4

for i in range(5):
    print(X[i])          #0 1 4 9 16

# Previous class won't handle slicing because its math assumes integer indexes are passed
# print(X[1:3])                                                      # TypeError: unsupported operand type(s) for ** or pow(): 'slice' and 'int'
 
class NewIndexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):                                    # Called for index or slice
        print('getitem:', index)                                     # 
        return self.data[index]                                      # Perform index or slice

NX = NewIndexer()
print(NX[0])                                                         # ('getitem:', 0)  5
print(NX[-1])                                                        # ('getitem:', -1) 9
print(NX[2:4])                                                       # ('getitem:', slice(2, 4, None)) [7, 8]
print(NX[1:])                                                        # ('getitem:', slice(1, 2147483647, None)) [6, 7, 8, 9]
# print(NX[:-1])                                                     # AttributeError: NewIndexer instance has no attribute '__len__' - may be ok in Python 3.X

# Where needed, __getitem__ can test the type of its argument, and extract slice object
# bounds-slice objects have attributes start, stop, and step, any of which can be None
# if omitted

# If used, the __setitem__ index assignment method similarly intercepts both index and
# slice assignments

class NewNewIndexer:
    
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

    def __setitem__(self,index,value):
        print('__setitem__', index, value)

NNX = NewNewIndexer()                                                
NNX[99]                                                              # ('indexing', 99)
NNX[1:99:2]                                                          # ('slicing', 1, 99, 2)
NNX[1:]                                                              # ('slicing', 1, 2147483647, None)

NNX[1] = 100                                                         # ('__setitem__', 1, 100)
NNX[2:4] = 'ab'                                                      # ('__setitem__', slice(2, 4, None), 'ab')

print("-" * 20 + "#2 Index iteration __getitem__" + "-" * 20)

# __getitem__ also turns out to be one way to overload iteration in Python-if this method is
# defined, for loops call the class's __getitem__ each time through, with successively
# higher offsets

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Spam"

print(X[1])                                                          # p
for item in X:
    print(item),                                                     # S p a m

# Any class that supports for loops automatically supports all iteration contexts in Python

print('p' in X)                                                      # True
print([c for c in X])                                                # ['S', 'p', 'a', 'm']
print(list(map(str.upper, X)))                                       # ['S', 'P', 'A', 'M']
(a,b,c,d) = X                                                        # Sequence assignment
print(a, c, d)                                                       # ('S', 'a', 'm')
print(list(X))                                                       # ['S', 'p', 'a', 'm']
print(tuple(X))                                                      # ('S', 'p', 'a', 'm')
print(''.join(X))                                                    # Spam
print(X)                                                             # <__main__.StepperIndex instance at 0xb733d7cc>

print("-" * 20 + "#3 Iterable Objects: __iter__ and __next__" + "-" * 20)

# Today, all iteration contexts in Python will try the __iter__ method first,
# before trying __getitem__. That is, they prefer the iteration protocol we learned about
# in Chapter 14 to repeatedly indexing an object; only if the object does not support the
# iteration protocol is indexing attempted instead. Generally speaking, you should prefer
# __iter__ too-it supports general iteration contexts better than __getitem__ can.

# Technically, iteration contexts work by passing an iterable object to the iter built-in
# function to invoke an __iter__ method, which is expected to return an iterator object.
# If it's provided, Python then repeatedly calls this iterator object's __next__ method to
# produce items until a StopIteration exception is raised. A next built-in function is also
# available as a convenience for manual iterations-next(I) is the same as I.__next__().

class Squares(object):
    
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    
    # Here, the iterator object returned by __iter__ is simply the instance self, because the
    # __next__ method is part of this class itself. In more complex scenarios, the iterator
    # object may be defined as a separate class and object with its own state information to
    # support multiple active iterations over the same data
    
    def __iter__(self):                                              # Get iterator object on iter
        print("__iter__")
        return self

    def __next__(self):                                              # Python 3.x: __next__, Python 2.x: next
        print("__next__")                                            # Return a square on each iteration
        if self.value == self.stop:                                  # Also called by next built-in
            print("StopIteration")
            raise StopIteration
        self.value += 1
        return self.value ** 2

    next = __next__                                                  # 3.x/2.x compatibility

for i in Squares(1, 5):
    print(i)

# __iter__
# __next__
# 1
# __next__
# 4
# __next__
# 9
# __next__
# 16
# __next__
# 25
# __next__
# StopIteration


# Because __iter__ objects retain explicitly managed state between
# next calls, they can be more general than __getitem__.

# Manual iterations work the same on user-defined iterables as they do on built-in types

X = Squares(1, 5)
I = iter(X)
print next(I)
print next(I)
print next(I)
print next(I)
print next(I)
#print next(I) #StopIteration exception

# On the other hand, iterables based on __iter__ can sometimes be more complex and
# less functional than those based on __getitem__. They are really designed for iteration,
# not random indexing-in fact, they don't overload the indexing expression at all, though you 
# can collect their items in a sequence such as a list to enable other operations:

X = Squares(1, 5)
# X[1]                                                               # TypeError: 'Squares' object does not support indexing
print list(X)[1]                                                     # 4

print("-" * 20 + "#4 Iterators Single versus multiple scans" + "-" * 20)

# Unlike our prior __getitem__ example, though, we also need to be aware that 
# a class's __iter__ may be designed for a single traversal only, not
# many. Classes choose scan behavior explicitly in their code.

# For example, because the current Squares class's __iter__ always returns self with just
# one copy of iteration state, it is a one-shot iteration; once you've iterated over an 
# instance of that class, it's empty. Calling __iter__ again on the same instance returns
# self again, in whatever state it may have been left. You generally need to make a new
# iterable instance object for each new iteration

X = Squares(1, 5)
print([n for n in X])                                                # [1, 4, 9, 16, 25]
print([n for n in X])                                                # []

print([n for n in Squares(1, 5)])                                    # [1, 4, 9, 16, 25]
print(list(Squares(1, 3)))                                           # [1, 4, 9]

print(":".join(map(str, Squares(1, 5))))                             # 1:4:9:16:25

# Just like single-scan built-ins such as map, converting to a list supports multiple scans
# as well, but adds time and space performance costs

X = Squares(1, 5)
print(tuple(X), tuple(X))                                            # (1, 4, 9, 16, 25) ()

X = list(Squares(1, 5))
print(tuple(X), tuple(X))                                            # (1, 4, 9, 16, 25) (1, 4, 9, 16, 25)

print("-" * 20 + "#5 Iterators Classes versus generators" + "-" * 20)

# Unlike classes, generator functions and expressions implicitly save their state and create
# the methods required to conform to the iteration protocol-with obvious advantages
# in code conciseness for simpler examples like these. 

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

for i in gsquares(1, 5):
    print(i),                                                        # 1 4 9 16 25

for i in (x ** 2 for x in range(1, 6)):
    print(i),                                                        # 1 4 9 16 25

print [x ** 2 for x in range(1, 6)]                                  # [1, 4, 9, 16, 25]

print("-" * 20 + "#6 Multiple Iterators on One Object" + "-" * 20)

# Here, the outer loop grabs an iterator from the string by calling iter, and each nested
# loop does the same to get an independent iterator. Because each active iterator has its
# own state information, each loop can maintain its own position in the string, regardless
# of any other active loops.

# Generator functions and expressions, as well as built-ins like map and zip, proved to be 
# single-iterator objects, thus supporting a single active scan. By contrast, the range built-in,
# and other built-in types like lists, support multiple active iterators with independent
# positions.

S = 'ace'
for x in S:
    for y in S:
        print(x + y),                                                # aa ac ae ca cc ce ea ec ee
print()

# To achieve the multiple-iterator effect, __iter__ simply needs to define a new stateful
# object for the iterator, instead of returning self for each iterator request.

# The following SkipObject class, for example, defines an iterable object that skips every
# other item on iterations. Because its iterator object is created anew from a supplemental
# class for each iteration, it supports multiple active loops directly

class SkipObject:
    
    def __init__(self, wrapped):                                     # Save item to be used
        self.wrapped = wrapped
        
    def __iter__(self):
        return SkipIterator(self.wrapped)                            # New iterator each time
    

class SkipIterator:
    
    def __init__(self, wrapped):
        self.wrapped = wrapped                                       # Iterator state information
        self.offset = 0
        
    def __next__(self):
        if self.offset >= len(self.wrapped):                         # Terminate iteration
            raise StopIteration
        else:
            item = self.wrapped[self.offset]                         # else return and skip
            self.offset += 2
            return item
    
    next = __next__                                                  # Python 2.X: next, Python 3.X: __next__ 

alpha = 'abcdef'
skipper = SkipObject(alpha)
I = iter(skipper)
print(next(I), next(I), next(I))                                     # ('a', 'c', 'e')

for x in skipper: 
    for y in skipper:
        print(x + y),                                                # aa ac ae ca cc ce ea ec ee
print()

#Alternative with simple for loops
S = 'abcdef'
for x in S[::2]:
    for y in S[::2]:
        print(x + y),                                                # aa ac ae ca cc ce ea ec ee
print()


# This isn't quite the same, though, for two reasons. First, each slice expression here will
# physically store the result list all at once in memory; iterables, on the other hand, pro-
# duce just one value at a time, which can save substantial space for large result lists.
# Second, slices produce new objects, so we're not really iterating over the same object in
# multiple places here. To be closer to the class, we would need to make a single object
# to step across by slicing ahead of time.

S = 'abcdef'
S = S[::2] 
print S                                                              # ace
for x in S:
    for y in S:
        print(x + y),                                                # aa ac ae ca cc ce ea ec ee
print()

# We could use this technique with a database object, for example, to support iterations
# over large database fetches, with multiple cursors into the same query result

print("-" * 20 + "#7 Coding Alternative: __iter__ plus yield" + "-" * 20)

# Because generator functions automatically save local variable state and create 
# required iterator methods, they fit this role well, and complement the state 
# retention and other utility we get from classes.

# As a review, recall that any function that contains a yield statement is turned into a
# generator function. When called, it returns a new generator object with automatic 
# retention of local scope and code position, an automatically created __iter__ method
# that simply returns itself, and an automatically created __next__ method (next in 2.X)
# that starts the function or resumes it where it last left off

def gen(x):
    for i in range(x):
        yield i ** 2

G = gen(3)                                                           # Create a generator with __iter__ and __next__
print(G.__iter__() == G)                                             # True
I = iter(G)                                                          # Runs __iter__: generator returns itself
print(next(I), next(I))                                              # (0, 1)
print(list(gen(5)))                                                  # [0, 1, 4, 9, 16]

# This is still true even if the generator function with a yield happens to be a method
# named __iter__: whenever invoked by an iteration context tool, such a method will
# return a new generator object with the requisite __next__. As an added bonus, generator
# functions coded as methods in classes have access to saved state in both instance 
# attributes and local scope variables.

class Squares2:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

# For loops and other iteration tools iterate through instances of this class automatically

for i in Squares2(0, 4):
    print(i),                                                        # 0 1 4 9 16
print()

# Running our class instance through iter obtains the result of calling
# __iter__ as usual, but in this case the result is a generator object with an automatically
# created __next__ of the same sort we always get when calling a generator function that
# contains a yield. The only difference here is that the generator function is automatically
# called on.

S = Squares2(1, 5)
print(S)                                                             # <__main__.Squares2 instance at 0xb73012ec>

I = iter(S) 
print(I)                                                             # <generator object __iter__ at 0xb72724dc>

print(next(I))                                                       # 1
print(next(I))                                                       # 4
print(next(I))                                                       # 9
print(next(I))                                                       # 16
print(next(I))                                                       # 25
try:
    next(I)
except StopIteration:
    print("StopIteration")                                           # StopIteration

# It may also help to notice that we could name the generator method something other
# than __iter__ and call manually to iterate-Squares(1,5).gen(), for example

class Squares3():
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
            
S = Squares3(1, 5)
I = iter(S.gen())
print(next(I))                                                       # 1
print(next(I))                                                       # 4
print(next(I))                                                       # 9

print("-" * 20 + "#8 Multiple iterators with yield" + "-" * 20)

# Besides its code conciseness, the user-defined class iterable of the prior section based
# upon the __iter__/yield combination has an important added bonus-it also supports
# multiple active iterators automatically. This naturally follows from the fact that each
# call to __iter__ is a call to a generator function, which returns a new generator with its
# own copy of the local scope for state retention

class Squares4:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

S = Squares4(1, 5)
I = iter(S)
print(next(I), next(I))                                              # 1, 4
J = iter(S)
print(next(J))                                                       # 1
print(next(I))                                                       # 9

# Although generator functions are single-scan iterables, the implicit calls to __iter__ in
# iteration contexts make new generators supporting new independent scans

S = Squares4(1, 4)
for i in S:                                                          # for calls __iter__
    for j in S:                                                      # for calls __iter__
        print('%s:%s' % (i, j)),                                     # 1:1 1:4 1:9 1:16 4:1 4:4 4:9 4:16 9:1 9:4 9:9 9:16 16:1 16:4 16:9 16:16
print()

# To do the same without yield requires a supplemental class that stores iterator state
# explicitly and manually, using techniques of the preceding section

class Squares5:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    # No problem that class Squares5Iterator is defined later.
    # Name Squares5Iterator has to be known when actually CALL this method
    # and we call it BELOW the declaration of Squares5Iterator class 
    def __iter__(self):
        return Squares5Iterator(self.start, self.stop)                 

class Squares5Iterator:
    
    def __init__(self, start, stop):
        self.current = start - 1
        self.stop = stop
        
    def next(self):
        self.current += 1
        if self.current > self.stop:
            raise StopIteration
        return self.current * 2

for i in Squares5(1, 5):
    print('%s' % i),                                                 # 2 4 6 8 10
print()

print("-" *  20 + "#9 Membership: __contains__, __iter__, and __getitem__" + "-" * 20)

# Operator overloading is often layered: classes may provide specific methods, 
# or more general alternatives used as fallback options. For example:
# - Comparisons in Python 2.X use specific methods such as __lt__ for "less than" if
#   present, or else the general __cmp__. Python 3.X uses only specific methods, not
#   __cmp__, as discussed later in this chapter.
# - Boolean tests similarly try a specific __bool__ first (to give an explicit True/False
#   result), and if it's absent fall back on the more general __len__ (a nonzero length
#   means True). As we'll also see later in this chapter, Python 2.X works the same but
#   uses the name __nonzero__ instead of __bool__.

# In the iterations domain, classes can implement the in membership operator as an
# iteration, using either the __iter__ or __getitem__ methods. To support more specific
# membership, though, classes may code a __contains__ method - when present, this
# method is preferred over __iter__, which is preferred over __getitem__. The 
# __contains__ method should define membership as applying to keys for a mapping (and can
# use quick lookups), and as a search for sequences.

class Iters:
    
    def __init__(self, value):
        self.data = value
        
    def __getitem__(self, i):                                        # Fallback for iteration
        print("get[%s]: " % i),                                      # Also for index, slice
        return self.data[i]
    
    def __iter__(self):                                              # Preferred for iteration 
        print('iter=> '),                                            # Allows only one active iterator
        self.ix = 0
        return self
    
    def __next__(self):
        print("next:"),
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    
    def __contains__(self, x):                                       # Preferred for 'in'
        print('contains: '),
        return x in self.data
    
    next = __next__                                                  # 2.X/2.X compatibility 

X = Iters([1, 2, 3, 4, 5])                                           # Make instance

print(3 in X)                                                        # contains:  True

for i in X:
    print(i),                                                        # iter=>  next: 1 next: 2 next: 3 next: 4 next: 5 next: ()
print()

print([i**2 for i in X])                                             # iter=>  next: next: next: next: next: next: [1, 4, 9, 16, 25]

print(list(map(bin, X)))                                             # iter=>  next: next: next: next: next: next: ['0b1', '0b10', '0b11', '0b100', '0b101']

# Manual iteration
I = iter(X)
while True:
    try:
        print(next(I)),                                              # iter=>  next: 1 next: 2 next: 3 next: 4 next: 5 next: () 
    except StopIteration:
        break   
print()

# As is, the class in this file has an __iter__ that supports multiple scans, but only a single
# scan can be active at any point in time (e.g., nested loops won't work), because each
# iteration attempt resets the scan cursor to the front. 

# The following is equivalent but allows multiple active scans

class Iters:
    
    def __init__(self, value):
        self.value = value
    
    def __getitem__(self, i):                                      # slice object also works here 
        print("get[%s]" % i),             
        return self.value[i]
    
    # If a yield statement is encountered, the state of the function is
    # frozen, and the value of expression_list is returned to .next()'s caller.
    def __iter__(self):
        print("iter=>"),
        for x in self.value:
            yield x                                                # when next() is called
        
    def __contains__(self, x):
        print("contains"),
        return x in self.value

I = Iters([10, 20, 30, 40, 50])

print(30 in I)                                                     # contains True

for i in I:
    print(i),                                                      # iter=> 10 20 30 40 50
print()

# On both Python 3.X and 2.X, when either version of this file runs its output is as follows
# - the specific __contains__ intercepts membership, the general __iter__ catches other
# iteration contexts such that __next__ (whether explicitly coded or implied by yield)

# Slice expressions trigger __getitem__ with a slice object containing bounds, both for 
# built-in types and user-defined classes, so slicing is automatic in our class:

print(I[1:3])                                                      # get[slice(1, 3, None)] [20, 30]


print("-" *  20 + "#10 Attribute Access: __getattr__ and __setattr__" + "-" * 20)

# In Python, classes can also intercept basic attribute access (a.k.a. qualification) when
# needed or useful. Specifically, for an object created from a class, the dot operator 
# expression object.attribute can be implemented by your code too, for reference, 
# assignment, and deletion contexts.

# The __getattr__ method intercepts attribute references. It's called with the attribute
# name as a string whenever you try to qualify an instance with an undefined (nonexistent)
# attribute name. It is not called if Python can find the attribute using its inheritance tree
# search procedure.

# Because of its behavior, __getattr__ is useful as a hook for responding to attribute
# requests in a generic fashion. It's commonly used to delegate calls to embedded (or
# "wrapped") objects from a proxy controller object-of the sort introduced in 
# Chapter 28's introduction to delegation. This method can also be used to adapt classes to an
# interface, or add accessors for data attributes after the fact-logic in a method that
# validates or computes an attribute after it's already being used with simple dot notation

# In effect, age becomes a dynamically computed attribute - its value is
# formed by running code, not fetching an object.

# The basic mechanism underlying these goals is straightforward - the following class
# catches attribute references, computing the value for one dynamically, and triggering
# an error for others unsupported with the raise statement

class Empty:
    
    a = 555
    
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
        
X = Empty()
print(X.age)                                                       # 40
print(X.a)                                                         # 555, __getattr__ isn't invoked

try:
    print X.name
except AttributeError, e:
    print('Error:', e)                                             # ('Error:', AttributeError('name',))

print("-" * 20 + "#11 Attribute Assignment and Deletion" + "-" * 20)

# In the same department, the __setattr__ intercepts all attribute assignments. If this
# method is defined or inherited, self.attr = value becomes self.__setattr__('attr',
# value). Like __getattr__, this allows your class to catch attribute changes, 
# and validate or transform as desired.

# This method is a bit trickier to use, though, because assigning to any self attributes
# within __setattr__ calls __setattr__ again, potentially causing an infinite recursion
# loop (and a fairly quick stack overflow exception!). 
# Remember, this catches all attribute assignments.

# IMPORTANT:
# If you wish to use this method, you can avoid loops by coding instance attribute 
# assignments as assignments to attribute dictionary keys. That is, use
# self.__dict__['name'] = x, not self.name = x; because you're not assigning to
# __dict__ itself, this avoids the loop

class AccessControl:
    
    a = 5
    
    def __setattr__(self, attr, value):
        print("__setattr__ is invoked")
        if attr == 'age':
            self.__dict__[attr] = value + 10
            #self.age = value + 10                                 # error: recursion
        else:
            raise AttributeError(attr + ' not allowed')

X = AccessControl()
X.age = 40                                                         # __setattr__ is invoked
print(X.age)                                                       # 50

try:
    X.name = "Bob"                                                 # __setattr__ is invoked
except AttributeError, e:
    print('Error:', e)                                             # ('Error:', AttributeError('name not allowed',))

# __setattr__ catched all attribute assignments even if the 
# attribute already exists
try:
    X.a = 10                                                       # __setattr__ is invoked
except AttributeError, e:
    print('Error:', e)                                             # ('Error:', AttributeError('a not allowed',))

# If you change the __dict__ assignment in this to either of the following, it triggers the
# infinite recursion loop and exception-both dot notation and its setattr built-in 
# function equivalent (the assignment analog of getattr) fail when age is assigned outside 
# the class:
# self.age = value + 10               # Loops
# setattr(self, attr, value + 10)     # Loops (attr is 'age')

print("-" * 20 + "#12 Emulating Privacy for Instance Attributes: Part 1" + "-" * 20)

# One of the ways to have private attributes (it's clumsy)

class PrivacyExc(Exception): pass

class Privacy:
    
    def __setattr__(self, attr, value):
        if attr in self.privates:
            raise PrivacyExc()
        else:
            self.__dict__[attr] = value 
    
class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__["name"] = "Tom"
        
x = Test1()
y = Test2()
x.name = 'Bob'
# y.name = 'Sue'                                                   # PrivacyExc is invoked
print(x.name)                                                      # Bob

y.age = 30
# x.age = 40                                                       # PrivacyExc is invoked
print(y.age)                                                       # 30

print("-" * 20 + "#13 String Representation: __repr__ and __str__" + "-" * 20)

# Excellent explanation of __repr__ vs __str__
# https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
# The default implementation is useless
# __repr__ goal is to be unambiguous
# __str__ goal is to be readable
# Container's __str__ uses contained objects' __repr__
# if __repr__ is defined, and __str__ is not, the object will behave as though __str__=__repr__

# Summary:
# Implement __repr__ for any class you implement. This should be second nature.
# Implement __str__ if you think it would be useful to have a string version which
# errs on the side of more readability in favor of more ambiguity.
# __repr__ is used everywhere, except by print and str when a __str__ is defined

class adder:
    def __init__(self, value = 0):
        self.data = value
    def __add__(self, other):
        print("__add__")
        # return adder(self.data + other)                          # self.data = 5, other = 5
        self.data += other

x = adder()
x + 5                                                              # __add__
print(x.data)                                                      # 5
print(x)                                                           # <__main__.adder instance at 0xb728364c>
print(str(x), repr(x))                                             # ('<__main__.adder instance at 0xb728364c>', '<__main__.adder instance at 0xb728364c>')

print('-' * 10)

class addrepr(adder):
    def __repr__(self):
        return "addrepr(%s)" % self.data

x = addrepr()
x + 7                                                              # __add__             
print(x.data)                                                      # 7
print(x)                                                           # addrepr(7)
print(str(x), repr(x))                                             # addrepr(7) addrepr(7) -  runs __repr__ for both

print('-' * 10)

class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
        
x = addstr()
x + 8                                                              # __add__
print(x.data)                                                      # 8
print(x)                                                           # [Value: 8]
print(str(x))                                                      # [Value: 8]
print(repr(x))                                                     # <__main__.addstr instance at 0xb738b46c> - __str__ doesn't work instead of __repr__

print('-' * 10)

class addboth(adder):

    def __str__(self):
        return '[Value: %s]' % self.data
    
    def __repr__(self):
        return 'addboth(%s)' % self.data

x = addboth()
x + 9                                                              # __add__
print(x.data)                                                      # 9
print(x)                                                           # [Value: 9]
print(str(x))                                                      # [Value: 9]
print(repr(x))                                                     # addboth(9)

l = [addboth(3), addboth(5)]      
print(l)                                                           # [addboth(3), addboth(5)] Container's __str__ uses contained objects' __repr__

print('-' * 10)

print('%.2f'    % 100500.199)                                      # 100500.20
print('%08d'    % 100500)                                          # 00100500
print('%010f'   % 100500)                                          # 100500.000000 - because 10 leading '0' is for the whole number (and even - sign and even .)!
print('%f'      % 100500)                                          # 100500.000000
print('%010.2f' % 100500)                                          # 0100500.00    - because 10 leading '0' is for the whole number (and even - sign and even .)!

print('-' * 10)

# 3 points to remember

# First, __str__ and __repr__ must both return strings; other result types are not converted 
# and raise errors, so be sure to run them through a to-string converter (e.g., str or %) if needed

class Printer:
    
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
objs = [Printer(2), Printer(3)]

# Second, depending on a container's string-conversion logic, the user-friendly display
# of __str__ might only apply when objects appear at the top level of a print operation;
# objects nested in larger objects might still print with their __repr__ or its default.

for x in objs:
    print(x)                                                       # 2 3
       
print(objs)                                                        # [<__main__.Printer instance at 0x887f60c>, <__main__.Printer instance at 0x887f62c>]        

# To ensure that a custom display is run in all contexts regardless of the container, code
# __repr__ , not __str__ ; the former is run in all cases if the latter doesn't apply, including
# nested appearances:

class PrinterRepr:
    
    def __init__(self, val):
        self.val = val
    
    def __repr__(self):
        return str(self.val)
    
objs = [PrinterRepr(2), PrinterRepr(3)]

for x in objs:
    print(x)                                                       # 2 3

print(objs)                                                        # [2, 3]

print("-" * 20 + "#14 Right-Side and In-Place Uses: __radd__ and __iadd__" + "-" * 20)

# The __add__ methods coded so far technically do not support the useinstance objects on 
# the right side of the + operator

x = adder(5)
x + 5
# 5 + x                                                            # TypeError: unsupported operand type(s) for +: 'int' and 'instance'

# To implement more general expressions, and hence support commutative-style operators, 
# code the __radd__ method as well. Python calls __radd__ only when the objectthe right side 
# of the + is your class instance, but the object on the left is not an instance of your class. 
# The __add__ method for the object on the left is called instead in all other cases

class Commuter1:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

# Note that x and y are instances of the same class here; when
# instances of different classes appear mixed in an expression, Python prefers the class
# of the one on the left. When we add the two instances together, Python runs __add__,
# which in turn triggers __radd__ by simplifying the left operand.

x = Commuter1(88)
y = Commuter1(99)

print(x + 1)                                                       # ('add', 88, 1) 89
print(1 + y)                                                       # ('radd', 99, 1) 100
print(x + y)

# ('add', 88, <__main__.Commuter1 instance at 0x86c31ac>) - left instance invokes __add__
# ('radd', 99, 88) - return self.val + other in __add__ invokes __radd__
# 187

# For truly commutative operations that do not require special-casing by position, it is
# also sometimes sufficient to reuse __add__ for __radd__:

# REUSE CASE #1: Call __add__ from __radd__ explicitly

class Commuter2:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        return self.__add__(other)

# REUSE CASE #2: Swap order and re-add

class Commuter3:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        return self + other

# REUSE CASE #3: __radd__ as an alias for __add__        
        
class Commuter4:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    __radd__ = __add__   


x = Commuter2(11)
y = Commuter2(22)

print(x + 1)                                                       # 12
print(1 + y)                                                       # 23
print(x + y)                                                       # 33

x = Commuter3(44)
y = Commuter3(55)

print(x + 1)                                                       # 45
print(1 + y)                                                       # 56
print(x + y)                                                       # 99

x = Commuter4(77)
y = Commuter4(88)

print(x + 1)                                                       # 78
print(1 + y)                                                       # 89
print(x + y)                                                       # 165


print("-" * 20 + "#15 Propagating class type" + "-" * 20)

class Commuter5:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        if isinstance(other, Commuter5):                           # Type test to avoid object nesting 
            other = other.val
        return Commuter5(self.val + other)                         # Result is another Commuter5

    def __radd__(self, other):
        return Commuter5(other + self.val)
    
    def __str__(self):
        return '<Commuter5: %s>' % self.val
    
x = Commuter5(88)
y = Commuter5(99)
print(x + 10)                                                      # <Commuter5: 98>
print(10 + y)                                                      # <Commuter5: 109>

z = x + y
print(z)                                                           # <Commuter5: 187>
print(z + 10)                                                      # <Commuter5: 197>
print(z + z)                                                       # <Commuter5: 374>
print(z + z + 1)                                                   # <Commuter5: 375>

# If you uncomment, you'll see that the last part of the preceding test winds up 
# differing and nesting objects-which still do the math correctly, but kick off pointless
# recursive calls to simplify their values, and extra constructor calls build results

# To also implement += in-place augmented addition, code either an __iadd__ or an
# __add__. The latter is used if the former is absent. The __iadd__ method allows 
# for more efficient in-place changes be coded where applicable (return self instead of
# a new instance)

class Number:

    def __init__(self, val):
        self.val = val
    
    def __iadd__(self, other):                                     # __iadd__ explicit
        self.val += other
        return self                                                # Usually return self!!!

x = Number(5)
x += 1
x += 1
print(x.val)                                                       # 7

# For mutable objects, this method can often specialize for quicker in-place changes

y = Number([1])
y += [2]
y += [3]
print(y.val)                                                       # [1, 2, 3]

# The normal __add__ method is run as a fallback, but may not be able optimize in-place cases

class Number:
    
    def __init__(self, val):
        self.val = val
        
    def __add__(self, other):
        return Number(self.val + other) 

x = Number(7)
x += 1
x += 1
print(x.val)                                                       # 9

# Though we've focused on + here, keep in mind that every binary operator has similar
# right-side and in-place overloading methods that work the same (e.g., __mul__,
# __rmul__, and __imul__)

print("-" * 20 + "#16 Call Expressions: __call__" + "-" * 20)

# Python runs a __call__ method for function call expressions applied to your instances, 
# passing along whatever positional or keyword arguments were sent. This allows instances
# to conform to a function-based API

class Prod:
    
    def __init__(self, value):
        self.value = value
    
    def __call__(self, other):
        return self.value * other
    
x = Prod(2)                                                        # "Remembers" 2 in state
print x(3)                                                         # 3 (passed) * 2 (state)
print x(4)                                                         # 4 (passed) * 2 (state)

# __call__ can become more useful when interfacing with APIs (i.e., libraries)
# that expect functions-it allows us to code objects that conform to an expected
# function call interface, but also retain state information, and other class assets
# such as inheritance. In fact, it may be the third most commonly used operator overloading
# method, behind the __init__ constructor and the __str__ and __repr__ display-format
# alternatives.

print("-" * 20 + "#17 Function Interfaces and Callback-Based Code" + "-" * 20)

# Bound vs unbound class methods
# https://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static

# If you want an event handler to retain state between events, you can register 
# either a class's bound method, or an instance that conforms to the expected
# interface with __call__.

# The following class defines an object that supports a function-call interface,
# but also has state information that remembers the color a button should change
# to when it is later pressed

class Callback:
    
    def __init__(self, color):                                     # Function + state information
        self.color = color
        
    def __call__(self):                                            # Support calls with no arguments 
        print('turn', self.color)

# Now, in the context of a GUI, we can register instances of this class as event handlers
# for buttons, even though the GUI expects to be able to invoke event handlers as simple
# functions with no arguments

cb1 = Callback('blue')
cb2 = Callback('green')

# Because it retains state as instance attributes, though, it remembers what 
# to do-it becomes a stateful function object. In fact, many consider such classes 
# to be the best way to retain state information in the Python language

cb1()                                                              # ('turn', 'blue')
cb2()                                                              # ('turn', 'green')

# On the other hand, tools such as closure functions are useful in basic state retention
# roles too

def callback(color):
    def oncall():
        print('turn', color)
    return oncall

cb3 = callback('yellow')
cb3()                                                              # ('turn', 'yellow')

# Before we move on, there are two other ways that Python programmers sometimes tie
# information to a callback function like this. One option is to use default arguments in
# lambda functions:

cb4 = (lambda color = 'red' : 'turn ' + color)
print(cb4())                                                       # turn red

# The other is to use bound methods of a class- a bit of a preview, but simple enough to
# introduce here. A bound method object is a kind of object that remembers both the
# self instance and the referenced function. This object may therefore be called later as
# a simple function without an instance:

class Callback:
    
    def __init__(self, color):
        self.color = color
        
    def changeColor(self):
        print('turn', self.color)
        
cb1 = Callback('blue')
cb2 = Callback('yellow')

cb1actual = cb1.changeColor                                        # Bound method: reference, don't call
cb2actual = cb2.changeColor                                        # Bound method: reference, don't call

cb1actual()                                                        # ('turn', 'blue')
cb2actual()                                                        # ('turn', 'yellow')

print("-" * 20 + "#18 Comparisons: __lt__, __gt__, and Others" + "-" * 20)

# Unlike the __add__/__radd__ pairings discussed earlier, there are no right-side 
# variants of comparison methods. Instead, reflective methods are used when only one
# operand supports comparison (e.g., __lt__ and __gt__ are each other's reflection).

# There are no implicit relationships among the comparison operators. The truth of
# == does not imply that != is false, for example, so both __eq__ and __ne__ should
# be defined to ensure that both operators behave correctly.

# In Python 2.X, a __cmp__ method is used by all comparisons if no more specific
# comparison methods are defined; it returns a number that is less than, equal to, or
# greater than zero, to signal less than, equal, and greater than results for the 
# comparison of its two arguments (self and another operand). This method often uses
# the cmp(x, y) built-in to compute its result. Both the __cmp__ method and the
# cmp built-in function are removed in Python 3.X: use the more specific methods
# instead.

class C:
    data = 'spam'
    def __gt__(self, other):                                       # 3.X and 2.X version          
        return self.data > other
    def __lt__(self, other):
        return self.data < other
    
X = C()
print(X > 'ham')                                                   # True (runs __gt__)
print(X < 'ham')                                                   # False (runs __lt__)

print("-" * 20 + "#19 Boolean Tests: __bool__ and __len__" + "-" * 20)

# As mentioned briefly earlier, in Boolean contexts, Python first tries __bool__ to obtain
# a direct Boolean value; if that method is missing, Python tries __len__ to infer a truth
# value from the object's length.


# Python 3.X

# This works as advertised in 3.X. In 2.X, though, __bool__ is ignored and the object is
# always considered true by default:

class Truth1:
    def __bool__(self): 
        print('in __bool__')
        return True
    
X = Truth1()
if X:
    print('yes!')                                                  # 3.X: 'in __bool__' 'yes!' 2.X: 'yes!', object is True by default

print(bool(X))                                                     # 3.X: 'in __bool__' True 2.X: True, object is True by default

# Python 2.X

# The short story here: in 2.X, use __nonzero__ for Boolean values, or return 0 from the
# __len__ fallback method to designate false:

class C1:
    def __nonzero__(self):
        print('in __nonzero__')
        return False

class C2:
    def __len__(self):
        return 0
    
class C3:
    def __len__(self):
        return 5
    
class C4:
    pass

c1 = C1()
print(bool(c1))                                                    # False

c2 = C2()
print(bool(c2))                                                    # False

c3 = C3()
print(bool(c3))                                                    # True

c4 = C4()
print(bool(c4))                                                    # True

print("-" * 20 + "#20 Object Destruction: __del__" + "-" * 20)

# The destructor method __del__, is run automatically when an instance's 
# space is being reclaimed (i.e., at "garbage collection" time):

# The destructor method works as documented, but it has some well-known caveats and
# a few outright dark corners that make it somewhat rare to see in Python code:

# Need: For one thing, destructors may not be as useful in Python as they are in some
# other OOP languages. Because Python automatically reclaims all memory space
# held by an instance when the instance is reclaimed, destructors are not necessary
# for space management.

# Predictability: For another, you cannot always easily predict when an instance will
# be reclaimed. In some cases, there may be lingering references to your objects in
# system tables that prevent destructors from running when your program expects
# them to be triggered. Python also does not guarantee that destructor methods will
# be called for objects that still exist when the interpreter exits.

# Exceptions: In fact, __del__ can be tricky to use for even more subtle reasons. 
# Exceptions raised within it, for example, simply print a warning message to
# sys.stderr (the standard error stream) rather than triggering an exception event,
# because of the unpredictable context under which it is run by the garbage collector
# -it's not always possible to know where such an exception should be delivered.

# Cycles: In addition, cyclic (a.k.a. circular) references among objects may prevent
# garbage collection from happening when you expect it to. An optional cycle 
# detector, enabled by default, can automatically collect such objects eventually, but
# only if they do not have __del__ methods. Since this is relatively obscure, we'll
# ignore further details here; see Python's standard manuals' coverage of both
# __del__ and the gc garbage collector module for more information.

class Life:
    
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)
        
r1 = Life('r1')                                                    # Hello r1
r1.live()                                                          # r1
r1 = 'r2'                                                          # Goodbye r1


