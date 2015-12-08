

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
__iter__ too—it supports general iteration contexts better than __getitem__ can.
'''








