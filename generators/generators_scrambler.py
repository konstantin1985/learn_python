

print("-" * 20 + "#1 Simple functions" + "-" * 20)

# must build an entire result list in memory all at once
# (not great on memory usage if it's massive), and requires the caller
# to wait until the entire list is complete (less than ideal if this
# takes a substantial amount of time)

def scramble1(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

print(scramble1("spam"))  # ['spam', 'pams', 'amsp', 'mspa']

# We can save some space by using a list comprehension

def scramble2(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble2("spam"))  # ['spam', 'pams', 'amsp', 'mspa']

print("-" * 20 + "#2 Generator functions" + "-" * 20)

# We can do better on both fronts by translating this to a generator
# function that yields one result at a time. Generator functions retain 
# their local scope state while active, minimize memory space
# requirements, and divide the work into shorter time slices.

def scramble3(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

print(list(scramble3('spam')))  # ['spam', 'pams', 'amsp', 'mspa']

def scramble4(seq):
    for i in range(len(seq)):
        yield seq
        seq = seq[1:] + seq[:1] # pay attention that it's no 'i' here

print(list(scramble4('spam')))  # ['spam', 'pams', 'amsp', 'mspa']


print("-" * 20 + "#3 Generator expressions" + "-" * 20)

# They're not as flexible as full functions, but because they yield
# their values automatically, expressions can often be more concise
# in specific use cases like this

s = "spam"
G = (s[i:] + s[:i] for i in range(len(s)))
print(list(G))  # ['spam', 'pams', 'amsp', 'mspa']

# We can't use the assignment statement of the first generator function version
# here, because generator expressions cannot contain statements. To generalize 
# a generator expression for an arbitrary subject, wrap it in a simple
# function that takes an argument and returns a generator that uses it

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

s = 'spam'
print F(s)                      # <generator object <genexpr> at 0xb73603c4>
print list(F(s))                # ['spam', 'pams', 'amsp', 'mspa']
print list(F([1, 2, 3]))        # [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

print("-" * 20 + "#4 Permutations" + "-" * 20)

# Since the number of combinations is a factorial that explodes exponentially, 
# the preceding permute1 recursive list-builder function will either introduce
# a noticeable and perhaps interminable pause or fail completely due to memory
# requirements, whereas the permute2 recursive generator will not-it returns 
# each individual result quickly, and can handle very large result sets

def permute1(seq):
    if not seq:
        return [seq]                         # Empty sequence
    else:
        res = []                             # 'res' is local for all recursion depths!
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]       # Delete current node
            for x in permute1(rest):         # Permute the others
                res.append(seq[i:i+1] + x)   # Add node seq[i:i+1] at front
        return res

print(permute1('abc'))                       # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]       # Delete current node
            for x in permute2(rest):         # Permute the others
                yield seq[i:i+1] + x         # Add node seq[i:i+1] at front

print(list(permute2('abc')))                 # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

