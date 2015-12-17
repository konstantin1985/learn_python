from audioop import reverse


print "-"*20 + "#1 List Comprehensions Versus map" + "-"*20

res = []
for x in 'spam':
    res.append(ord(x))
print res                   #[115, 112, 97, 109]

res = map(ord, 'spam')
print res                   #[115, 112, 97, 109]

res = [ord(x) for x in 'spam']
print res                   #[115, 112, 97, 109]

print filter(lambda x: x % 2 == 0, range(5)) #[0, 2, 4]

print [x + y for x in [0, 1, 2] for y in [100, 200, 300]]   #[100, 200, 300, 101, 201, 301, 102, 202, 302]


M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print [col + 10 for row in M for col in row]   #[11, 12, 13, 14, 15, 16, 17, 18, 19]

print [[col + 10 for col in row] for row in M] #[[11, 12, 13], [14, 15, 16], [17, 18, 19]]

'''
However, in this case, there is currently a substantial performance advantage to the
extra complexity: based on tests run under Python today, map calls can be twice as fast
as equivalent for loops, and list comprehensions are often faster than map calls. This
speed difference can vary per usage pattern and Python, but is generally due to the fact
that map and list comprehensions run at C language speed inside the interpreter, which
is often much faster than stepping through Python for loop bytecode within the PVM.
'''

listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
print [age for (name, age, job) in listoftuple]
print list(map((lambda row: row[1]), listoftuple))


print "-"*20 + "#2 Generator Functions: yield Versus return" + "-"*20

'''
The chief code difference between generator and normal functions is that a generator
yields a value, rather than returning one-the yield statement suspends the function
and sends a value back to the caller, but retains enough state to enable the function to
resume from where it left off. When resumed, the function continues execution im-
mediately after the last yield run. From the function's perspective, this allows its code
to produce a series of values over time, rather than computing them all at once and
sending them back in something like a list.
'''

def gensquares(N):
    for i in range(N):
        yield i ** 2

'''
Notice that the top-level iter call of the iteration protocol isn't required here because
generators are their own iterator, supporting just one active iteration scan. To put that
another way generators return themselves for iter , because they support next directly.
This also holds true in the generator expressions
'''

y = gensquares(5)
print(iter(y) is y)   #True
print(next(y))        #0

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print {i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}   #{0: 'AAA', 1: 'BBB', 2: 'CCC'}

def gen():
    for i in range(10):
        X = yield i
        print(X)
        
G = gen()
print next(G)      #0
print G.send(77)   #77 1
print G.send(88)   #88 2
print next(G)      #None 3

print "-"*20 + "#3 Generator Expressions: Iterables Meet Comprehensions" + "-"*20

'''
In fact, at least on a functionality basis, coding a list comprehension is essentially the
same as wrapping a generator expression in a list built-in call to force it to produce
all its results in a list at once:
'''

print list(x ** 2 for x in range(4))   #[0, 1, 4, 9]

'''
Operationally, however, generator expressions are very different: instead of building
the result list in memory, they return a generator object-an automatically created
iterable. This iterable object in turn supports the iteration protocol to yield one piece
of the result list at a time in any iteration context. The iterable object also retains gen-
erator state while active-the variable x in the preceding expressions, along with the
generator's code location.
'''

G = (x ** 2 for x in range(4))
print iter(G) is G   #True
print next(G) #0
print next(G) #1
print next(G) #4
print next(G) #9
#print next(G) #StopIteration

for num in (x ** 2 for x in range(4)):
    print("%s, %s" % (num, num/2.0)) #important to divide by 2.0

'''
Syntactically, parentheses are not required around a generator expression
that is the sole item already enclosed in parentheses used for other purposes-like those
of a function call.
'''

print ''.join(x.upper() for x in "aaa,bbb,ccc".split(',')) #AAABBBCCC

print sorted((x ** 2 for x in range(4)), reverse = True)   #[9, 4, 1, 0]
             
    
print "-"*20 + "#4 Generators Are Single-Iteration Objects" + "-"*20

'''
A subtle but important point: both generator functions and generator expressions are
their own iterators and thus support just one active iteration-unlike some built-in
types, you can't have multiple iterators of either positioned at different locations in the
set of results.
'''

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







