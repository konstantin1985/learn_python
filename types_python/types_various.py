

# In Python, we can also index backward, from the end-positive indexes count from
# the left, and negative indexes count back from the right:

s = "Spam"
print s[-1] # m
print s[-2] # a
# print s[-5] # string index out of range

# Formally, a negative index is simply added to the string''s length, so the following two
# operations are equivalent (though the first is easier to code and less easy to get wrong):
print s[-1]         # m
print s [len(s)-1]  # m

# Slicing
print s[1:]         # pam
print s[0:3]        # Spa
print s[:2]         # Sp
print s[:-1]        # Spa
print s[:]          # Spam

# Immutable objects can't be changed
#s[0] = "t"         # TypeError: 'str' object does not support item assignment

# Every object in Python is classified as either IMMUTABLE (unchangeable) or not. In terms
# of the core types, numbers, strings, and tuples are immutable; lists, dictionaries, and
# sets are not-they can be changed in place freely, as can most new objects you'll code
# with classes.

s = "Step"
l = list(s)
l[2] = "a"
print "".join(l)    # Stap

# Every string operation we've studied so far is really a sequence operation-that is, these
# operations will work on other sequences in Python as well, including lists and tuples.
# In addition to generic sequence operations, though, strings also have operations all
# their own, available as methods-functions that are attached to and act upon a specific
# object, which are triggered with a call expression.

p = "Star"
print p.find("a")         # 2
print p.replace("ta","2") # S2r
print p.replace("rr","3") # Star
print p                   # Star

p = "aaa,bbb,ccc , ddd\n"
print repr(p)                        # 'aaa,bbb,ccc , ddd\n'
print repr(p.rstrip())               # 'aaa,bbb,ccc , ddd' right strip
print repr(p.rstrip().split(','))    # ['aaa', 'bbb', 'ccc ', ' ddd']

a = "asd123"
print a.isalnum()                    # True
print a.isdigit()                    # False

# As a rule of thumb, Python's toolset is layered: generic
# operations that span multiple types show up as built-in functions or expressions (e.g.,
# len(X), X[0]), but type-specific operations are method calls (e.g., aString.upper())

# Show all the methods "+" = "__add__", 'replace' and other methods are also here
print dir(a)
print a + "NI"            # asd123NI
print a.__add__("NI")     # asd123NI

# Formally, in both 2.X and 3.X, non-Unicode strings are sequences of 8-bit bytes that
# print with ASCII characters when possible, and Unicode strings are sequences of Uni-
# code code points-identifying numbers for characters, which do not necessarily map to
# single bytes when encoded to files or stored in memory.
# https://en.wikipedia.org/wiki/UTF-8 = Unicode 8 bit

print repr("spam".encode('utf8'))    # 'spam'
print repr("spam".encode('utf16'))   #'\xff\xfes\x00p\x00a\x00m\x00'

# As a notable difference, Python 2.X allows its normal and Unicode strings to be mixed
# in expressions as long as the normal string is all ASCII; in contrast, Python 3.X has
# tighter model that never allows its normal and byte strings to mix without explicit
# conversion

# Apart from these string types, Unicode processing mostly reduces to transferring text
# data to and from files-text is encoded to bytes when stored in a file, and decoded into
# characters (a.k.a. code points) when read back into memory. Once it is loaded, usually 
# process text as strings in decoded form only.

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello    Python 444 world') # match in (.*) position, [ \t] - space or tab
print match.group(0)    # Hello    Python 444 world match.group(0) = match.group() - the whole match is returned
print match.group(1)    # Python 444
print match.groups()    # ('Python 444 ',)

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')  # [/:] = / or :
print match.groups()                                                  # ('usr', 'home', 'lumberjack')
print re.split('[/:]', '/usr/home/lumberjack')                        # ['', 'usr', 'home', 'lumberjack']

# Because they are sequences, lists support all the sequence operations we discussed for
# strings; the only difference is that the results are usually lists instead of strings.

L = [123, 'spam', 1.23]
print len(L) # 3

L = L + [4, 5, 6]
print L      # [123, 'spam', 1.23, 4, 5, 6]

# Type-Specific Operations
L.append("NI")
print L      # [123, 'spam', 1.23, 4, 5, 6, 'NI']
L.pop(1)
print L      # [123, 1.23, 4, 5, 6, 'NI']

M = ["bb", "aa", "cc"]
M.sort()
print M      # ["aa", "bb", "cc"]
M.reverse()
print M      # ["cc", "bb", "aa"]

# LIST COMPREHENSIONS
# List comprehensions derive from set notation; they are a way to build a new list by
# running an expression on each item in a sequence, one at a time, from left to right. 

# 3x3 matrix as nested lists
M = [[1, 2, 3], 
     [4, 5, 6], # Code can span lines if bracketed
     [7, 8, 9]]

col2 = [row[1] for row in M]
print col2      # [2, 5, 8]

diag = [M[i][i] for i in [0,1,2]]
print diag      # [1, 5, 9]

# Create a SET of row sums
sumRow = {sum(row) for row in M}
print sumRow    # set([24, 6, 15])

# Create a dictionary of row sums
sumRow = {i : sum(M[i]) for i in range(3)}
print sumRow    # {0: 6, 1: 15, 2: 24}

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print D['food'] # Spam
D['quantity'] += 1
print D         # {'food': 'Spam', 'color': 'pink', 'quantity': 5}

bob1 = dict(name='Bob', job='dev', age=40)
print bob1      # {'age': 40, 'job': 'dev', 'name': 'Bob'}

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print bob2      # {'age': 40, 'job': 'dev', 'name': 'Bob'}
 
print zip(['name', 'job', 'age'], ['Bob', 'dev', 40]) # [('name', 'Bob'), ('job', 'dev'), ('age', 40)]

# The list comprehension, though, and related functional programming tools like map and
# filter, will often run faster than a for loop today on some types of code (perhaps even
# twice as fast)-a property that could matter in your programs for large data sets. 

# The TUPLE object (pronounced "toople" or "tuhple," depending on whom you ask) is
# roughly like a list that cannot be changed-tuples are sequences, like lists, but they are
# immutable, like strings. Syntactically, they are
# normally coded in parentheses instead of square brackets, and they support arbitrary
# types, arbitrary nesting, and the usual sequence operations
T = (1, 2, 3, 4)
print len(T)        # 4
print T + (5, 6)    # (1, 2, 3, 4, 5, 6)
print T[0]          # 1
print T.index(4)    # 3
print T.count(4)    # 1
#T[0] = 3           # TypeError: 'tuple' object does not support item assignment

# Sets
x = set('spam')
y = {'h', 'a', 'm'}
print x,y           # set(['a', 'p', 's', 'm']) set(['a', 'h', 'm'])
print x & y         # set(['a', 'm'])
print x | y         # set(['a', 'p', 's', 'h', 'm'])





