

print "-"*20 + "#1 Indexing and Slicing: __getitem__ and __setitem__" + "-"*20

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print X[2]               #4

for i in range(5):
    print(X[i])          #0 1 4 9 16

print "-"*20 + "#2 Index iteration __getitem__" + "-"*20

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Spam"

print X[1]                     #p
for item in X:
    print(item),               #S p a m

print 'p' in X                 #True
print [c for c in X]           #['S', 'p', 'a', 'm']
print list(map(str.upper, X))  #['S', 'P', 'A', 'M']
(a,b,c,d) = X                  #Sequence assignment
print a, c, d                  #S a m
print list(X)                  #['S', 'p', 'a', 'm']
print tuple(X)                 #('S', 'p', 'a', 'm')
print ''.join(X)               #Spam
print X                        #<__main__.StepperIndex instance at 0xb733d7cc>

print "-"*20 + "#3 Iterable Objects: __iter__ and __next__" + "-"*20

'''
Today, all iteration contexts in Python will try the __iter__ method first,
before trying __getitem__. That is, they prefer the iteration protocol we learned about
in Chapter 14 to repeatedly indexing an object; only if the object does not support the
iteration protocol is indexing attempted instead. Generally speaking, you should prefer
__iter__ too-it supports general iteration contexts better than __getitem__ can.
'''

class Squares(object):
    
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    
    def __iter__(self):
        print("__iter__")
        return self

    def next(self):           #in Python 3.x it's __next__
        print("__next__")
        if self.value == self.stop:
            print("StopIteration")
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i)

'''
__iter__
__next__
1
__next__
4
__next__
9
__next__
16
__next__
25
__next__
StopIteration
'''

'''
Because __iter__ objects retain explicitly managed state between
next calls, they can be more general than __getitem__.
'''

X = Squares(1, 5)
I = iter(X)
print next(I)
print next(I)
print next(I)
print next(I)
print next(I)
#print next(I) #StopIteration exception

'''
On the other hand, iterables based on __iter__ can sometimes be more complex and
less functional than those based on __getitem__. They are really designed for iteration,
not random indexing-in fact, they don't overload the indexing expression atthough you 
can collect their items in a sequence such as a list to enable other operations:
'''

X = Squares(1, 5)
#X[1]                 #TypeError: 'Squares' object does not support indexing
print list(X)[1]      #4

print "-"*20 + "#4 Iterators Single versus multiple scans" + "-"*20

X = Squares(1, 5)
print([n for n in X])                     #[1, 4, 9, 16, 25]
print([n for n in X])                     #[]

print([n for n in Squares(1, 5)])         #[1, 4, 9, 16, 25]
print(list(Squares(1, 3)))                #[1, 4, 9]

print ":".join(map(str, Squares(1, 5)))   #1:4:9:16:25

X = Squares(1, 5)
print tuple(X), tuple(X) #(1, 4, 9, 16, 25) ()

X = list(Squares(1, 5))
print tuple(X), tuple(X) #(1, 4, 9, 16, 25) (1, 4, 9, 16, 25)


print "-"*20 + "#5 Iterators Classes versus generators" + "-"*20

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

for i in gsquares(1, 5):
    print(i),                              #1 4 9 16 25

for i in (x ** 2 for x in range(1, 6)):
    print(i),                              #1 4 9 16 25

print [x ** 2 for x in range(1, 6)]        #[1, 4, 9, 16, 25]

print "-"*20 + "#6 Multiple Iterators on One Object" + "-"*20

S = 'ace'
for x in S:
    for y in S:
        print(x + y),                      #aa ac ae ca cc ce ea ec ee


class SkipObject:
    
    def __init__(self, wrapped):
        self.wrapped = wrapped
        
    def __iter__(self):
        return SkipIterator(self.wrapped)
    

class SkipIterator:
    
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
        
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item
    

alpha = 'abcdef'
skipper = SkipObject(alpha)
I = iter(skipper)
print(next(I), next(I), next(I))           #('a', 'c', 'e')
print

for x in skipper: 
    for y in skipper:
        print(x + y),                      #aa ac ae ca cc ce ea ec ee
print

#Alternative with simple for loops
S = 'abcdef'
for x in S[::2]:
    for y in S[::2]:
        print(x + y),                      #aa ac ae ca cc ce ea ec ee
print

'''
This isn't quite the same, though, for two reasons. First, each slice expression here will
physically store the result list all at once in memory; iterables, on the other hand, pro-
duce just one value at a time, which can save substantial space for large result lists.
Second, slices produce new objects, so we're not really iterating over the same object in
multiple places here. To be closer to the class, we would need to make a single object
to step across by slicing ahead of time:
'''

S = 'abcdef'
S = S[::2]
print S                                    #'ace'
for x in S:
    for y in S:
        print(x + y)


print "-"*20 + "#7 Coding Alternative: __iter__ plus yield" + "-"*20

'''
Because generator functions automati-
cally save local variable state and create required iterator methods, they fit this role
well, and complement the state retention and other utility we get from classes.
'''

def gen(x):
    for i in range(x): yield i ** 2

G = gen(5)
print G.__iter__() == G     #True
I = iter(G)
print next(I), next(I)      #0 1
list(gen(5))                #[0, 1, 4, 9, 16]

class Squares2:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

for i in Squares2(0, 4):
    print(i),              #0 1 4 9 16

'''
Running our class instance through iter obtains the result of calling
__iter__ as usual, but in this case the result is a generator object with an automatically
created __next__ of the same sort we always get when calling a generator function that
contains a yield. The only difference here is that the generator function is automatically
called on.
'''

S = Squares2(1, 5)
print S                   #<__main__.Squares2 instance at 0xb73012ec>

I = iter(S) 
print(I)                  #<generator object __iter__ at 0xb72724dc>

print next(I)             #1
print next(I)             #4
print next(I)
print next(I)
print next(I)
try:
    next(I)
except StopIteration:
    print "StopIteration"


'''
It may also help to notice that we could name the generator method something other
than __iter__ and call manually to iterate-Squares(1,5).gen(), for example.
'''

class Squares3():
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
            
S = Squares3(1, 5)
I = iter(S.gen())
print next(I)             #1
print next(I)             #4
print next(I)             #9

print "-"*20 + "#8 Multiple iterators with yield" + "-"*20

'''
Besides its code conciseness, the user-defined class iterable of the prior section based
upon the __iter__/yield combination has an important added bonus-it also supports
multiple active iterators automatically. This naturally follows from the fact that each
call to __iter__ is a call to a generator function, which returns a new generator with its
own copy of the local scope for state retention:
'''

class Squares4:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

S = Squares4(1, 5)
I = iter(S)
print next(I), next(I)   #1, 4
J = iter(S)
print next(J)            #1
print next(I)            #9

'''
Although generator functions are single-scan iterables, the implicit calls to __iter__ in
iteration contexts make new generators supporting new independent scans:
'''

S = Squares4(1, 4)
for i in S:                       #each for call __iter__
    for j in S:
        print('%s:%s' % (i, j)),  #1:1 1:4 1:9 1:16 4:1 4:4 4:9 4:16 9:1 9:4 9:9 9:16 16:1 16:4 16:9 16:16
print

class Squares5:
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
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
    print('%s' % i), #2 4 6 8 10
print

print "-"*20 + "#9 Attribute Access: __getattr__ and __setattr__" + "-"*20

'''
In effect, age becomes a dynamically computed attribute-its value is
formed by running code, not fetching an object.
'''

class Empty:
    
    a = 555
    
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
        
X = Empty()
print X.age   #40
print X.a     #555, __getattr__ isn't invoked

try:
    print X.name
except AttributeError, e:
    print('Error:', e)
print 'finish'

print "-"*20 + "#10 Attribute Assignment and Deletion" + "-"*20

'''
In the same department, the __setattr__ intercepts all attribute assignments. If this
method is defined or inherited, self.attr = value becomes self.__setattr__('attr',
value). Like __getattr__, this allows your class to catch attribute changes, and validate
or transform as desired.
'''

'''
This method is a bit trickier to use, though, because assigning to any self attributes
within __setattr__ calls __setattr__ again, potentially causing an infinite recursion
loop (and a fairly quick stack overflow exception!).
Remember, this catches all attribute assignments.
'''

class AccessControl:
    
    def __setattr__(self, attr, value):
        print "__setattr__ is invoked"
        if attr == 'age':
            self.__dict__[attr] = value + 10
            #self.age = value + 10 #error: recursion
        else:
            raise AttributeError(attr + ' not allowed')

X = AccessControl()
X.age = 40
print X.age                 #50
try:
    X.name = "Bob"
except AttributeError, e:
    print('Error:', e)      #('Error:', AttributeError('name not allowed',))

'''
If you change the __dict__ assignment in this to either of the following, it triggers the
infinite recursion loop and exception-both dot notation and its setattr built-in func-
tion equivalent (the assignment analog of getattr) fail when age is assigned outside the
class:
self.age = value + 10               # Loops
setattr(self, attr, value + 10)     # Loops (attr is 'age')
'''

'''
The __getattribute__ method intercepts all attribute fetches, not just those that
are undefined, but when using it you must be more cautious than with __get
attr__ to avoid loops.

The property built-in function allows us to associate methods with fetch and set
operations on a specific class attribute.
'''
'''
Python programmers are able to write large OOP frameworks and applications without private
declarations-an interesting finding about access controls in general that is beyond the
scope of our purposes here.
'''


print "-"*20 + "#10 String Representation: __repr__ and __str__" + "-"*20

class adder:
    
    def __init__(self, value = 0):
        self.data = value
    
    def __add__(self, other):
        print "__add__"
        self.data += other
        return adder(self.data + other)

    def __repr__(self):
        return "addrepr(%s)" % self.data

x = adder()
print x.data
x = x + 5
print x.data
print(x)
print str(x), repr(x)


class addstr(adder):
    
    def __str__(self):
        return '[Value: %s]' % self.data
        
x = addstr(3)
x + 1
print(x)         #[Value: 4]
print str(x)     #[Value: 4]
print repr(x)    #addrerp(4)

class addboth(adder):

    def __str__(self):
        return '[Value: %s]' % self.data
    
    def __repr__(self):
        return 'addboth(%s)' % self.data

x = addboth(4)
x + 1
print(x)         
print str(x)      
print repr(x)     

class Printer:
    
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
objs = [Printer(2), Printer(3)]

'''
Second, depending on a container's string-conversion logic, the user-friendly display
of __str__ might only apply when objects appear at the top level of a print operation;
objects nested in larger objects might still print with their __repr__ or its default.
'''

for x in objs:
    print(x)    #2 3
        
print(objs)     #[<__main__.Printer instance at 0x887f60c>, <__main__.Printer instance at 0x887f62c>]        

'''
To ensure that a custom display is run in all contexts regardless of the container, code
__repr__ , not __str__ ; the former is run in all cases if the latter doesn't apply, including
nested appearances:
'''

class PrinterRepr:
    
    def __init__(self, val):
        self.val = val
    
    def __repr__(self):
        return str(self.val)
    
objs = [PrinterRepr(2), PrinterRepr(3)]
for x in objs:
    print(x)    #2 3

print(objs)     #[2, 3]


print "-"*20 + "#11 Right-Side and In-Place Uses: __radd__ and __iadd__" + "-"*20

class Commuter1:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

x = Commuter1(88)
y = Commuter1(99)

print(x + 1) #('add', 88, 1) 89
print(1 + y) #('radd', 99, 1) 100
print(x + y)
#('add', 88, <__main__.Commuter1 instance at 0x86c31ac>)
#('radd', 99, 88)
#187

class Commuter2:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        return self.__add__(other)
    
class Commuter3:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        return self + other
        
        
class Commuter4:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    __radd__ = __add__   


x = Commuter2(88)
y = Commuter2(99)

print(x + 1) #89
print(1 + y) #100
print(x + y) #187

x = Commuter3(88)
y = Commuter3(99)

print(x + 1) #89
print(1 + y) #100
print(x + y) #187

x = Commuter4(88)
y = Commuter4(99)

print(x + 1) #89
print(1 + y) #100
print(x + y) #187


print "-"*20 + "#12 Propagating class type" + "-"*20

class Commuter5:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        return Commuter5(other + self.val)
    
    def __str__(self):
        return '<Commuter5: %s>' % self.val
    
x = Commuter5(88)
y = Commuter5(99)
print(x + 10)  #<Commuter5: 98>
print(10 + y)  #<Commuter5: 109>

z = x + y
print(z)         #<Commuter5: 187>
print(z + 10)    #<Commuter5: 197>
print(z + z)     #<Commuter5: 374>
print(z + z + 1) #<Commuter5: 375>

'''
The __iadd__ method, though, allows for more efficient in-place changes to
be coded where applicable:
'''

class Number:
    
    def __init__(self, val):
        self.val = val
    
    def __iadd__(self, other):
        self.val += other
        return self

x = Number(5)
x += 1
x += 1
print x.val   #7

y = Number([1])
y += [2]
y += [3]
print y.val   #[1, 2, 3]

print "-"*20 + "#13 Call Expressions: __call__" + "-"*20

class Prod:
    
    def __init__(self, value):
        self.value = value
    
    def __call__(self, other):
        return self.value * other
    
x = Prod(2)
print x(3) #6
print x(4) #8

print "-"*20 + "#13 Function Interfaces and Callback-Based Code" + "-"*20

class Callback:
    
    def __init__(self, color):
        self.color = color
        
    def __call__(self):
        print('turn', self.color)
   
cb1 = Callback('blue')
cb2 = Callback('green')

cb1()  #('turn', 'blue')
cb2()  #('turn', 'green')

#Another alternative to make a callback

def callback(color):
    def oncall():
        print('turn')
    return oncall

cb3 = callback('yellow')
cb3()   #turn

'''
Before we move on, there are two other ways that Python programmers sometimes tie
information to a callback function like this. One option is to use default arguments in
lambda functions:
'''

cb4 = (lambda color = 'red' : 'turn ' + color)
print(cb4())  #turn red

'''
The other is to use bound methods of a class- a bit of a preview, but simple enough to
introduce here. A bound method object is a kind of object that remembers both the
self instance and the referenced function. This object may therefore be called later as
a simple function without an instance:
'''

class Callback:
    
    def __init__(self, color):
        self.color = color
        
    def changeColor(self):
        print('turn', self.color)
        
cb1 = Callback('blue')
cb2 = Callback('yellow')

cb1actual = cb1.changeColor
cb2actual = cb2.changeColor

cb1actual()   #('turn', 'blue')
cb2actual()   #('turn', 'yellow')

print "-"*20 + "#14 Comparisons: __lt__, __gt__, and Others" + "-"*20

class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other
    
X = C()
print(X > 'ham')  # True (runs __gt__)
print(X < 'ham')  # False (runs __lt__)

print "-"*20 + "#15 Boolean Tests: __bool__ and __len__" + "-"*20

'''
As mentioned briefly earlier, in Boolean contexts, Python first tries __bool__ to obtain
a direct Boolean value; if that method is missing, Python tries __len__ to infer a truth
value from the object's length.
'''

#Python 3

class Truth1:
    def __bool__(self): return True
    
X = Truth1()
if X: 
    print('yes!')  #'yes!'

class Truth2:
    def __bool__(self): 
        print 'Here'
        return False
    
Y = Truth2()
print bool(Y) #False

'''
The short story here: in 2.X, use __nonzero__ for Boolean values, or return 0 from the
__len__ fallback method to designate false:
'''
        
class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)
        
r1 = Life('r1')  #Hello r1
r1.live()        #r1
r1 = 'r2'        #Goodbye r1




