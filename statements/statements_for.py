
import os

#for target in object:  # Assign object items to target
    #statements         # Repeated loop body: use target
#else:                  # Optional else part
    #statements         # If we didn't hit a 'break'

print('-' * 10 + "A.1. Basic for loops" + '-' * 10)

# The name used as the assignment target in a for header line is usually a (possibly new)
# variable in the scope where the for statement is coded. 
# It can even be changed inside the loop's body, but it will automatically be
# set to the next item in the sequence when control returns to the top of the loop again.
# After the loop this variable normally still refers to the last item visited, which is the last
# item in the sequence unless the loop exits with a break statement.
for x in [1, 2, 3]:
    pass
print(x)  # 3

# Any sequence works in a for, as it's a generic tool. 
# For example, for loops work on strings and tuples:
S = 'lumberjack'
for x in S: print(x + ','),  # l, u, m, b, e, r, j, a, c, k, - space is added

T = ('and', "I'm", 'ok')
for x in T: print(x),  # and I'm ok
print

T = [(1, 2), (3, 4)]
for (a, b) in T:
    print(a, b),  # (1, 2) (3, 4)
print

# We can iterate thfough key/values in dictionaries
D = {'a': 1, 'b': 2, 'c': 3}
print(D.items())  # [('a', 1), ('c', 3), ('b', 2)]
for (key, value) in D.items():
    print(key, "=>", value),  #
print

# Even nested structures may be automatically unpacked in a for loop
for ((a, b), c) in [([1, 2], 3), ('AB', 4)]:
    print(a, b, c),  # (1, 2, 3) ('A', 'B', 4)
print 

# Slicing returns a type-specific result, 
# whereas starred names always are assigned lists
for all in [[1, 2, 3, 4], (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c),  # (1, [2, 3], 4) (5, (6, 7), 8)
print

print('-' * 10 + "A.2. Nested for loops" + '-' * 10)

# Check whether 'search' are in 'items'  
items = ["aaa", 11, (4, 5)]
search = [(4, 5), 3.14]

# Pay attention that 'else' is a part of 'for' statement here
for key in search:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "wasn't found")
# ((4, 5), 'was found')
# (3.14, "wasn't found")
      
# We can use 'in' operator to achieve the same result easier
for key in search:
    if key in items:
        print(key, "was found")
    else:
        print(key, "wasn't found")        
# ((4, 5), 'was found')
# (3.14, "wasn't found")

print('-' * 10 + "A.3. Work with files" + '-' * 10)

f = open("myfile.txt", 'w')
f.write("My File 123\n")
f.write("Some text")
f.close()

# Read by characters
f = open("myfile.txt", 'r')
while True:
    char = f.read(1)     # read 1 character
    if not char: break   # EOF is reached
    print(char),         # , adds spaces
print
# M y   F i l e   1 2 3 
# S o m e   t e x t

# Also read by characters, but load the file in memory all at one
# read() - if the size argument is negative or omitted, read until EOF is reached.
for char in open("myfile.txt", 'r').read():
    print(char),
print
# M y   F i l e   1 2 3 
# S o m e   t e x t

# To read text files line by line:
# readlines() method loads a file IN MEMORY all at once into a line-string list
for line in open("myfile.txt", 'r').readlines():
    print(line.rstrip())
# My File 123
# Some text

# To read files with ITERATORS:
# The best option for text files-besides its simplicity, it works for arbitrarily
# large files because it doesn't load the entire file into memory all at once.
for line in open("myfile.txt", 'r'):
    print(line.rstrip())
# My File 123
# Some text

os.remove("myfile.txt")

print('-' * 10 + "A.4. Exercises" + '-' * 10)

# Return a new list that contains the ASCII codes of each character in the string. 
# Does the expression map(ord, S) have similar effect? How about [ord(c) for c in S]? Why?
S = 'abc'
rv = []
for c in S:
    rv.append(ord(c))
print(rv)        # [97, 98, 99]

rv = map(ord, S)
print(rv)        # p2: [97, 98, 99], p2: <map object at 0xb709556c>
print(list(rv))  # [97, 98, 99]

rv = [ord(c) for c in S]
print(rv)        # [97, 98, 99]
 
 
# Program logic alternatives. Consider the following code, which uses a while loop
# and found flag to search a list of powers of 2 for the value of 2 raised to the fifth
# power (32).

X = 5
value = 2 ** X

L = map(lambda x: x ** 2, range(7))
# L = [x ** 2 for x in range(7)]

if value in L:
    print('at index ', L.index(value))
else:
    print(X, ' not found')

