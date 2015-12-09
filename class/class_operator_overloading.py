from django.conf.locale import sk


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








