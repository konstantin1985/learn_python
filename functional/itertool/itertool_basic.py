

# MAIN SOURSE:
# [Hattem][XXXX] Mastering Python p.95


# USEFUL LINKS:
# 1) https://www.blog.pythonlibrary.org/2016/04/20/python-201-an-intro-to-itertools/

# 2) https://docs.python.org/3/library/itertools.html#itertools.accumulate
#    How all itertools are implemented under the hood.

# GENERAL INFORMATION:

# Simply put, a functional program consists of many functions
# having a simple input and output, without using (or even having) 
# any outside scope or context to access. Python is not a purely
# functional language, so it is easy to cheat and work outside of
# the local scope, but that is not recommended.

# All of these are iterable and have been constructed in such a
# way that only a minimal amount of memory is required to process 
# even the largest of datasets. While you can easily write most
# of these functions yourself using a simple function, I would 
# still recommend using the ones available in the itertools library.
# These are all fast, memory efficient, and-perhaps more importantly
# -tested.

import operator
import itertools
import sys

print('-' * 10 + "# 1. Accumulate - reduce with intermediate results" + '-' * 10) 

# The accumulate function is very similar to the reduce function,
# which is why some languages actually have accumulate instead of
# reduce as the folding operator.

# The major difference between the two is that the accumulate
# function returns the immediate results. This can be useful when
# summing the results of a company's sales.

if sys.version_info >= (3, 0):

    # Sales per month
    months = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]
    
    # list to do all iterations
    rv  = list(itertools.accumulate(months, operator.add))
    print(rv)
    # [10, 18, 23, 30, 42, 52, 57, 65, 80, 83, 87, 89]

print('-' * 10 + "# 2. Chain - combining multiple results" + '-' * 10) 

# Roughly equivalent to:
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

# The chain function is a simple but useful function that combines
# the results of multiple iterators. Very simple but also very
# useful if you have multiple lists, iterators, and so on-just
# combine them with a simple chain.

a = range(3)
b = range(5)
rv = list(itertools.chain(a, b))
print(rv)
# [0, 1, 2, 0, 1, 2, 3, 4]

rv = list(itertools.chain('abc','de','fg'))
print(rv)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print('-' * 10 + "# 3. Combinations - combinatorics in Python" + '-' * 10) 

# In mathematics, a combination is a selection of items from a
# collection, such that (unlike permutations) the order of selection
# does not matter.

# The combinations iterator produces results exactly as you would
# expect from the mathematical definition. All combinations with
# a specific length from a given list of items.

# The combinations function gives all possible combinations
# of the given items of a given length. The number of possible
# combinations is given by the binomial coefficient.

# | n |       n!
# | - |  = --------
# | k |    k!(n-k)!

rv = list(itertools.combinations(range(3), 2))
print(rv)
# [(0, 1), (0, 2), (1, 2)]

# The combinations_with_repetitions function is very similar to
# the regular combinations function, except that the items can
# be combined with themselves as well. To calculate the number
# of results, the binomial coefficient described earlier can be
# used with the parameters as n = n + k - 1 and k = k.


rv = list(itertools.combinations_with_replacement(range(3), 2))
print(rv)
# [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

# Let's look at a little combination of combinations and chain
# for generating a powerset. In mathematics, the power set (or
# powerset) of any set S is the set of all subsets of S, including
# the empty set and S itself.

rv = []
NUM = 4
for x in range(NUM):
    c = itertools.combinations(range(NUM), x)
    rv = chain(rv, c)
rv = list(rv)
print(rv)

def powerset(iterable):
    return itertools.chain.from_iterable(
        itertools.combinations(iterable, i)
        
 for i in range(len(iterable) + 1))

list(powerset(range(3)))


print('-' * 10 + "# 4. permutations - combinations where the order matters" + '-' * 10) 

# The permutations function is quite similar to the combinations
# function. The only real difference is that (a, b) is considered
# distinct from (b, a). In other words, the order matters.

rv = itertools.permutations(range(3), 2)
print(list(rv))
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# | n |       n!
# | - |  = --------
# | k |     (n-k)!

print('-' * 10 + "# 5. compress - selecting items using a list of Booleans" + '-' * 10) 

# The compress function is one of those that you won't need too often,
# but it can be very useful when you do need it. It applies a Boolean
# filter to your iterable, making it return only the ones you actually
# need. The most important thing to note here is that it's all executed
# lazily and that compress will stop if either the data or the selectors
# collection is exhausted. So, even with infinite ranges, it works without
# a hitch.

rv = itertools.compress(range(1000), [0, 1, 1, 1, 0, 1])
print(list(rv))
# [1, 2, 3, 5]

print('-' * 10 + "# 6. dropwhile/takewhile - selecting items using a function" + '-' * 10)

# The dropwhile function will drop all results until a given predicate
# evaluates to true. This can be useful if you are waiting for a device
# to finally return an expected result.

rv = itertools.dropwhile(lambda x: x <= 3, [1, 3, 5, 4, 2])
print(list(rv))
# [5, 4, 2]

rv = itertools.takewhile(lambda x: x <= 3, [1, 3, 5, 4, 2])
print(list(rv))
# [1, 3]

# Simply adding the two will give you the original result again.

print('-' * 10 + "# 7. count - infinite range with decimal steps" + '-' * 10)

# The first is that this range is infinite, so don't even try to do 
# list(itertools.count()). You'll definitely run out of memory immediately.

# The second difference is that unlike the range function, you can actually
# use floating-point numbers here, so there is no need of whole/integer numbers.

# The count function takes two optional parameters: a start parameter, which
# defaults to 0, and a step parameter, which defaults to 1.

# Except for being infinite, the standard version of "count" returns the same
# results as the range function does.
for a, b in zip(range(3), itertools.count()):
    print(a, b)
# (0, 0)
# (1, 1)
# (2, 2)

# With a different starting point the results are still the same
for a, b in zip(range(5, 8), itertools.count(5)):
    print(a, b)
# (5, 5)
# (6, 6)
# (7, 7)

# And a different step works the same as well
for a, b in zip(range(5, 10, 2), itertools.count(5, 2)):
    print(a, b)
# (5, 5)
# (7, 7)
# (9, 9)

# Unless you try to use floating point numbers
# range(5, 10, 0.5)                           
# TypeError: range() integer step argument expected, got float.

# Which does work for count
for a, b in zip(range(5, 10), itertools.count(5, 0.5)):
    print(a, b)
# (5, 5)
# (6, 5.5)
# (7, 6.0)
# (8, 6.5)
# (9, 7.0)

print('-' * 10 + "# 8. groupby - grouping your sorted iterable" + '-' * 10)

# The groupby function is a really convenient function for grouping
# results. The usage and use cases are probably clear, but there are
# some important things to keep in mind when using this function:
# - The input needs to be sorted by the group parameter ('a', 'b', 'c'
#   in the example). Otherwise, it will be added as a separate group.
# - The results are available for use only once. So, after processing
#   a group, it will not be available anymore.

items = [('a', 1), ('a', 2), ('b', 2), ('b', 0), ('c', 3)]

# Part of a group by the first parameter in items
for group, items in itertools.groupby(items, lambda x: x[0]):
    print('%s: %s' % (group, [v for k, v in items]))
# a: [1, 2]
# b: [2, 0]
# c: [3]

# And then there are cases where you might get unexpected results
# (we didn't sort by group):

items = [('a', 1), ('b', 0), ('b', 2), ('a', 2), ('c', 3)]
groups = dict()
for group, items in itertools.groupby(items, lambda x: x[0]):
    groups[group] = items
    print('%s: %s' % (group, [v for k, v in items]))
# a: [1]
# b: [0, 2]
# a: [2]
# c: [3]

for group, items in sorted(groups.items()):
    print('%s: %s' % (group, [v for k, v in items]))
# a: []
# b: []
# c: []

# So, make sure you sort by the grouping parameter before trying
# to group. Additionally, walking through the same group a second
# time offers no results. This can be fixed easily using 
# groups[group] = list(items) instead, but it can give quite a few
# unexpected bugs if you are not aware of this.

print('-' * 10 + "# 9. islice - slicing any iterable" + '-' * 10)

# When working with the itertools functions, you might notice
# that you cannot slice these objects. That is because they are
# generators. Luckily, the itertools library has a function for
# slicing these objects as well - islice.

rv = itertools.islice(itertools.count(), 2, 7)
print(list(rv))
# [2, 3, 4, 5, 6]

# So, instead of the regular slice:
# itertools.count()[:10]

# We enter the slice parameters to the function:
rv = itertools.islice(itertools.count(), 10)
print(list(rv))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# What you should note from this is actually more than the inability
# to slice the objects. It is not just that slicing doesn't work, 
# but it is not possible to get the length either-at least not without
# counting all items separately-and with infinite iterators, even that
# is not possible. The only understanding you actually get from a 
# generator is that you can fetch items one at a time. You won't even
# know in advance whether you're at the end of the generator or not.














