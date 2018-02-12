

#[Lutz]

import os

print('-' * 10 + "A.1. Formal syntax" + '-' * 10)

# [ expression for target1 in iterable1 if condition1
#              for target2 in iterable2 if condition2 ...
#              for targetN in iterableN if conditionN ]

# Nested for loop in list comprehensions work like nested for loop
# statements.

# [0, 1, 2] - external loop, [100, 200, 300] - nested loop
rv = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(rv)  # [100, 200, 300, 101, 201, 301, 102, 202, 302]

rv = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        rv.append(x + y)
print(rv)  # [100, 200, 300, 101, 201, 301, 102, 202, 302]

# Iterate over letters
rv = [x + y for x in 'spam' for y in 'SPAM']
print(rv)  # ['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM', 'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']

# List comprehension with if statements
rv = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(rv)  # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

rv = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                rv.append((x, y))
print(rv)  # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

print('-' * 10 + "A.2. List comprehensions and matrices" + '-' * 10)

M = [[1, 2, 3],
     [4, 5 ,6],
     [7, 8, 9]]

print(M[1])  # [4, 5, 6] - Row 2

# Get column 2
rv = [row[1] for row in M]
print(rv)  # [2, 5, 8]

# Get column 2 using offsets
rv = [M[row][1] for row in (0, 1, 2)]
print(rv)  # [2, 5, 8]

# Get main diagonal of the matrix
rv = [M[i][i] for i in range(len(M))]
print(rv)  # [1, 5, 9]

# Get another main diagonal
rv = [M[i][len(M)-1-i] for i in range(len(M))]
print(rv)  # [3, 5, 7]

# Change in place requires assignment to offsets 
L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] += 10
print(L)  # [[11, 12, 13], [14, 15, 16]]

# Impossible to do such in-place assignments with list comprehensions
# So we may create a new list and assign it to the original name

# [col + 10 for row in M for col in row]

# Equivalent for loops will be different
# Here as usual
# for row in M:
#    for col in row:
N = [col + 10 for row in M for col in row]
print(N)  # [11, 12, 13, 14, 15, 16, 17, 18, 19]

# Here a bit different
# for row in M:
#     tmp = []
#     for col in row:
#         tmp.append(col + 10) 
N = [[col + 10 for col in row] for row in M]
print(N)  # [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

# We can create tuples from the top level iteration over M and N
# More than 2 arguments in zip() are allowed 
# [([1, 2, 3], [11, 12, 13]), ([4, 5, 6], [14, 15, 16]), ([7, 8, 9], [17, 18, 19])]
print(zip(M, N))

# Multiply corresponding elements of the matrices
rv = [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]
print(rv)  # [[11, 24, 39], [56, 75, 96], [119, 144, 171]]

# The equivalent for loop looks different from previously considered
# Pay attention to the order of loops
rv = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    rv.append(tmp)
print(rv)  # [[11, 24, 39], [56, 75, 96], [119, 144, 171]]

# Based on tests run under Python today, map calls can be twice as fast
# as equivalent for loops, and list comprehensions are often faster than map calls

# Because map and list comprehensions are both expressions, they also
# can show up syntactically in places that for loop statements cannot, such as in the
# bodies of lambda functions, within list and dictionary literals, and more.

print('-' * 10 + "A.3. Compare list comprehensions and map()" + '-' * 10)

f = open("myfile.txt", 'w')
f.write("abc\n")
f.write("def\n")
f.close()

# We use file iterators here
rv = [line.rstrip() for line in open("myfile.txt")]
print(rv)  # ['abc', 'def']
rv = list(map((lambda line: line.rstrip()), open("myfile.txt")))
print(rv)  # ['abc', 'def']

os.remove("myfile.txt")

# Pick values from the tuples (like SQL request)
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
rv = [age for (name, age, job) in listoftuple]
print(rv)  # [35, 40]
rv = list(map((lambda row: row[1]), listoftuple))
print(rv)  # [35, 40]



