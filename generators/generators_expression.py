import math


print("-" * 20 + "#1 Generator Expressions: Iterables Meet Comprehensions" + "-" * 20)


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


print("-" * 20 + "#2 Generator Expressions: versus map" + "-" * 20)

# In 2.X, map makes temporary lists and generator
# expressions do not, but the same coding comparisons apply.
# In 3.X, map generates results on request.

print(list(map(abs, (-1, -2, 3, 4))))        # [1, 2, 3, 4]
print(list(abs(x) for x in (-1, -2, 3, 4)))  # [1, 2, 3, 4]

# Nonfunction case. Generator looks simpler
print(list(map(lambda x: x * 2, (1, 2, 3, 4))))  # [2, 4, 6, 8]
print(list(x * 2 for x in (1, 2, 3, 4)))         # [2, 4, 6, 8]

line = 'aaa,bbb,ccc'

# Pointless temporary list is created
rv = ''.join([x.upper() for x in line.split(',')])
print(rv)  # AAABBBCCC

# Generates results
rv = ''.join(x.upper() for x in line.split(','))
print(rv)  # AAABBBCCC

# Nested comprehensions, nested maps and nested generator
rv = [x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]
print rv  # [2, 4, 6, 8]
rv = list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))))
print rv  # [2, 4, 6, 8]
rv = list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))
print rv  # [2, 4, 6, 8]

# Nested combination of map and generator
rv = list(map(math.sqrt, (x ** 2 for x in range(4))))
print rv  # [0.0, 1.0, 2.0, 3.0]

print("-" * 20 + "#3 Generator Expressions: versus filter" + "-" * 20)

# Because filter is an iterable in 3.X that generates its results on request, 
# a generator expression with an if clause is operationally equivalent

line = "aa bbb c"
rv = ''.join(x for x in line.split() if len(x) > 1)
print rv  # aabbb

rv = ''.join(filter(lambda x: len(x) > 1, line.split()))
print rv  # aabbb

# Adding processing steps to filter results requires a map too, which makes
# filter noticeably more complex than a generator expression

rv = ''.join(x.upper() for x in line.split() if len(x) > 1)
print rv  # AABBB

rv = ''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))
print rv  # AABBB
