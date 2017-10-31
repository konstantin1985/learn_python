

print('-' * 10 + "A.1. Basic if" + '-' * 10)

if not 1:           # If not expression is True = if expression is false
    print('true')
else:
    print('false')  # false
    

print('-' * 10 + "A.2. Multiway branching" + '-' * 10)

# There is no if statement, we can do long if, elif... or

choice = 'ham'
print({'spam': 1.25,
       'ham':  1.99,
       'eggs': 0.99,
       'bacon':1.10}[choice])  # 1.99

# Handling switch defaults with get()

D = {'spam': 1.25,
     'ham':  1.99,
     'eggs': 0.99,
     'bacon':1.10}

print(D.get('ham', 'Bad choice'))    # 1.99
print(D.get('super', 'Bad choice'))  # Bad choice

# Also you can use [if 'ham' in D:] or [try: + except KeyError:]

# Also, it could be D = {'ham': function} - later on about it

print('-' * 10 + "A.3. Boolean test" + '-' * 10)

# X and Y
# Is true if both X and Y are true
# X or Y
# Is true if either X or Y is true
# not X
# Is true if X is false (the expression returns True or False)

# With these operators we get True or False (1 or 0)
print(2 < 3, 3 < 2)  # (True, False)

# On the other hand, the and and or operators always return an object-either the object
# on the left side of the operator or the object on the right. 
# We don't get simple True or False, but if we test in if they will be as expected 
# (every object is inherently True or False)

# For or tests, Python evaluates the operand objects from left to right and returns the first
# one that is true.  Moreover, Python stops at the FIRST true operand it finds. 
print(2 or 3, 3 or 2)  # (2, 3)

# In the other two tests, the left operand
# is false (an empty object), so Python simply evaluates and returns the object on the
# right-which may happen to have either a true or a false value when tested.
print([] or 3, [] or {})  # (3, {})

# Python and operations also stop as soon as the result is known; however, in this case
# Python evaluates the operands from left to right and stops if the left operand is a false
# object because it determines the result
print(2 and 3, 3 and 2)  # (3, 2)
print([] and {})         # []
print(3 and [])          # []

# So in Python Booleans return either the left or the right object, not a simple integer flag.

print('-' * 10 + "A.4. Ternary expression" + '-' * 10)

# For a string, nonempty means True
A = 't' if 'spam' else 'f'
print(A)  # t
A = 't' if '' else 'f'
print(A)  # f

# A = ((X and Y) or Z) -> A = Y if X else Z (need to assume that Y will be Boolean true)

# The bool function will translate X into the equivalent of integer 1 or 0, 
# which can then be used as offsets to pick true and false values from a list.
# This isn't exactly the same, because Python WILL NOT SHORT-CIRTUIT
# it will always run both Z and Y, regardless of the value of X.

A = ['f', 't'][bool('')]
print(A)  # f
A = ['f', 't'][bool('spam')]
print(A)  # t

# Short-circuit is important to know
def f1():
    print "f1"
    return "f1"

def f2():
    print "f2"
    return "f2"
    
if f1() or f2(): # Only f(1) is invoked because what it returns (return "f1" is true)
    pass

# Correct way to run both
tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2:
    pass

# Pay attention to __bool__ and __len__method (latter is tried if the former is absent)

print('-' * 10 + "A.5. Collection tools" + '-' * 10)

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))  # [1, 2, 'spam', 'ham']
print([x for x in L if x])    # [1, 2, 'spam', 'ham']
print(any(L), all(L))         # (True, False)



