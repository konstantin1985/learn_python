

#[Lutz]


print('-' * 10 + "A.1. Comprehension syntax summary" + '-' * 10)

# For sets, the new literal form {1, 3, 2} is equivalent to 
# set([1, 3, 2]), and the new set comprehension syntax 
# {f(x) for x in S if P(x)} is like the generator expression 
# set(f(x) for x in S if P(x)), where f(x) is an arbitrary 
# expression.

# For dictionaries, the new dictionary comprehension syntax 
# {key: val for (key, val) in zip(keys, vals)} works like the 
# form dict(zip(keys, vals)), and {x: f(x) for x in items} is 
# like the generator expression dict((x, f(x)) for x in items).

# List comprehension
rv = [x * x for x in range(4)]
print(rv)                                 # [0, 1, 4, 9]

# Generator expression
rv = (x * x for x in range(4))
print(rv)                                 # <generator object <genexpr> at 0xb738f144>

# Set comprehension (3.X and 2.7)
rv = {x * x for x in range(4)}        
print(rv)                                 # set([0, 1, 4, 9])

# Dictionary comprehension (3.X and 2.7)
rv = {x: x * x for x in range(4)}         
print(rv)                                 # {0: 0, 1: 1, 2: 4, 3: 9}

print('-' * 10 + "A.2. Scope and comprehension variables" + '-' * 10)

(X for X in range(5))
# print(X)                                # NameError: name 'X' is not defined


# Python 3.X - list localize variables
# Python 2.X - list doesn't localize variables

X = 99
rv = [X for X in range(5)] 
print(rv)                                 # [0, 1, 2, 3, 4]
print(X)                                  # P 2.X: 4, P 3.X: 99

# Python 3.X - generator, set and dictionary localize variables
# Python 2.X - generator, set and dictionary localize variables

X = 99
rv = (X for X in range(5))
print(list(rv))                           # [0, 1, 2, 3, 4]
print(X)                                  # P 2.X: 99, P 3.X: 99

# Loop statements do not localize variables

Y = 99
for Y in range(5): pass
print(Y)                                  # P 2.X: 4, P 3.X: 4

# More complicated example. Usual LEGB rule works

X = 'aaa'
def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))      # Z comprehension, Y local, X global

func()                                    # aaabbb
# print(Z)                                # NameError: name 'Z' is not defined

print('-' * 10 + "A.3. Comprehending set and dictionary comprehensions" + '-' * 10)

# In a sense, set and dictionary comprehensions are just syntactic sugar
# for passing generator expressions to the type names. Because both accept
# any iterable, a generator works well here

rv = {x * x for x in range(5)}            # set comprehension
print(rv)                                 # set([0, 1, 4, 16, 9])

rv = set(x * x for x in range(5))         # same as the set comprehension
print(rv)                                 # set([0, 1, 4, 16, 9])

rv = {x: x * x for x in range(5)}         # dictionary comprehension
print(rv)                                 # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

rv = dict((x, x * x) for x in range(5))   # same as dictionary comprehension
print(rv)                                 # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# We can always build the result objects with manual code

res = set()
for x in range(5):
    res.add(x * x)
print(res)                                # set([0, 1, 4, 16, 9])

res = {}
for x in range(5):
    res[x] = x * x
print(res)                                # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Notice that although both set and dictionary comprehensions accept 
# and scan iterables, they have no notion of generating results on 
# demand-both forms build complete objects all at once.

# Discussion: https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

G = ((x, x * x) for x in range(5))        # Every generator is an iterator
print(next(G))                            # (0, 0)
print(next(G))                            # (1, 1)
 
print('-' * 10 + "A.4. Extended syntaxis for set and dictionary comprehensions" + '-' * 10)

# Set and dictionary comprehensions support nested associated if
# clauses to filter items out of the result

rv = [x * x for x in range(10) if x % 2 == 0]       # Lists are ordered
print(rv)                                           # [0, 4, 16, 36, 64]

rv = {x * x for x in range(10) if x % 2 == 0}       # Sets aren't ordered
print(rv)                                           # set([0, 16, 4, 64, 36])

rv = {x: x * x for x in range(10) if x % 2 == 0}    # Dictionary keys aren't ordered
print(rv)                                           # {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}

# Nested for loops work as well, though the unordered and no-duplicates
# nature of both types of objects can make the results a bit less
# straightforward to decipher

rv = [x + y for x in [1, 2, 3] for y in [4, 5, 6]]  # Lists keep duplicates
print(rv)                                           # [5, 6, 7, 6, 7, 8, 7, 8, 9]

rv = {x + y for x in [1, 2, 3] for y in [4, 5, 6]}  # Sets don't keep duplicates
print(rv)                                           # set([8, 9, 5, 6, 7])

rv = {x: y for x in [1, 2, 3] for y in [4, 5, 6]}   # Dictionaries don't keep duplicated
print(rv)                                           # {1: 6, 2: 6, 3: 6}

# Like list comprehensions, the set and dictionary varieties can also
# iterate over any type of iterable-lists, strings, files, ranges, and
# anything else that supports the iteration protocol

rv = {x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
print(rv)                                           # {'bd': (98, 100), 'ac': (97, 99), 'ad': (97, 100), 'bc': (98, 99)}

rv = {k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
print(rv)                                           # set(['sausagesausage', 'spamspam'])