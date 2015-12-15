

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





