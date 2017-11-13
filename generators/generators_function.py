

print("-" * 20 + "#1 Generator Functions: yield Versus return" + "-" * 20)

# Generator functions are like normal functions in most respects, and in fact are coded
# with normal def statements. However, when created, they are compiled specially into
# an object that supports the iteration protocol. And when called, they don't return a
# result: they return a result generator that can appear in any iteration context.

# Python for loops, and all other iteration contexts, use this iteration protocol to step
# through a sequence or value generator, if the protocol is supported (if not, iteration
# falls back on repeatedly indexing sequences instead). Any object that supports this
# interface works in all iteration tools.

# To support this protocol, functions containing a yield statement are compiled specially
# as generators - they are not normal functions, but rather are built to return an object
# with the expected iteration protocol methods. When later called, they return a 
# generator object that supports the iteration interface with an automatically created 
# method named __next__ to start or resume execution.

# An iterable object's iterator is fetched initially with the iter built-in function,
# though this step is a no-op for objects that are their own iterator.

# The chief code difference between generator and normal functions is that a generator
# yields a value, rather than returning one-the yield statement suspends the function
# and sends a value back to the caller, but retains enough state to enable the function to
# resume from where it left off. When resumed, the function continues execution 
# immediately after the last yield run. From the function's perspective, this allows its code
# to produce a series of values over time, rather than computing them all at once and
# sending them back in something like a list.

# Generator functions may also have a return statement that, along with falling off the
# end of the def block, simply terminates the generation of values - technically, by raising
# a StopIteration exception after any normal function exit actions. From the caller's
# perspective, the generator's __next__ method resumes the function and runs until either
# the next yield result is returned or a StopIteration is raised.

# The net effect is that generator functions, coded as def statements containing yield
# statements, are automatically made to support the iteration object protocol and thus
# may be used in any iteration context to produce results over time and on demand.

def gensquares(N):
    for i in range(N):
        yield i ** 2

# To end the generation of values, functions either use a return statement with no value
# or simply allow control to fall off the end of the function body.

for i in gensquares(5):
    print(i, ":"),    # (0, ':') (1, ':') (4, ':') (9, ':') (16, ':')
print()   

# Notice that the top-level iter call of the iteration protocol isn't required here because
# generators are their own iterator, supporting just one active iteration scan. To put that
# another way generators return themselves for iter, because they support next directly.
# This also holds true in the generator expressions

y = gensquares(5)
print(iter(y) is y)   # True
print(next(y))        # 0
print(next(y))        # 1
print(next(y))        # 4
print(next(y))        # 9
print(next(y))        # 16
# print(next(y))      # StopIteration

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

# All iteration contexts would work
print tuple(ups('aaa,bbb,ccc'))                            # ('AAA', 'BBB', 'CCC')
print {i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}   # {0: 'AAA', 1: 'BBB', 2: 'CCC'}

print("-" * 20 + "#2 Generator Functions: send Versus next" + "-" * 20)

# When this extra protocol is used, values are sent into a generator G by calling
# G.send(value). The generator's code is then resumed, and the yield expression in the
# generator returns the value passed to send. If the regular G.__next__() method (or its
# next(G) equivalent) is called to advance, the yield simply returns None.

def gen():
    for i in range(10):
        X = yield i  # (*) 
        print(X)     # (**)
        
G = gen()
rv = next(G)       # Nothing is printed, because gen() did "yield 0" and (**) wasn't reached yet 
print rv           # 0  - result of yield 0
rv = G.send(77)    # 77 - X in (*) equals to 77 we print it (**) and go to the next iteration
print rv           # 1  - yield 1
rv = G.send(88)    # 88
print rv           # 2
rv = next(G)       # None - if we don't pass any value with send, then X is None 
print rv           # 3

# There are also throw and close methods!