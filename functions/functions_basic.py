

print('-' * 10 + "A.1. def statements" + '-' * 10)

# The def statement creates a function object and assigns it to a name.
# If the value is omitted, return sends back a None.
# Technically, a function without a return statement also returns the None object automatically.

# The Python def is a true executable statement: when it runs, it creates a new function
# object and assigns it to a name.

test = True
if test:
    def func():
        print("f1")
        return
else:
    def func():
        print("f2")
        return

func()  # f1, call the version selected and built

# One way to understand this code is to realize that the def is much like an = statement:
# it simply assigns a name at runtime.

# IMPORTANT
# defs are not evaluated until they are reached and run, and the code inside defs is not
# evaluated until the functions are later called.

# Because function definition happens at runtime, there's nothing special about the
# function name. 
othername = func
othername()  # f1

# Besides calls, functions allow arbitrary attributes to be attached to record information for later use
func.attr = "some value"
print func.attr  # some value

# This sort of type-dependent behavior is known as polymorphism, 2 * 4 = 8, 2 * 'Ni' = 'NiNi'
# that essentially means that the meaning of an operation depends on the
# objects being operated upon. Because it's a dynamically typed language, polymorphism
# runs rampant in Python. In fact, every operation is a polymorphic operation in Python:
# printing, indexing, the * operator, and much more.

# Moreover, if the objects passed in do not support this expected interface, Python will
# detect the error when the * expression is run and raise an exception automatically. It's
# therefore usually pointless to code error checking ourselves.

# This turns out to be a crucial philosophical difference between Python and statically
# typed languages like C++ and Java: in Python, your code is not supposed to care about
# specific data types.

# By and large, we code to object interfaces in Python, not data types.

# Before you can call a function, you have to make it. To do this, run its def statement,
# either by typing it interactively or by coding it in a module file and importing the file.
#func2()  # NameError: name 'func2' is not defined
def func2():
    pass

# Example of polymorphic behavior with different input arguments
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

# For intersect, this means that the first argument has to support the for loop, and the
# second has to support the in membership test. Any two such objects will work, 
# regardless of their specific types

s1 = "SPAM"; s2 = "SCAM"
print(intersect(s1, s2))                # ['S', 'A', 'M']
print(intersect([1, 3, 5], (3, 4, 5)))  # [3, 4]

print('-' * 10 + "A.2. Scope" + '-' * 10)

# The place where you assign a name in your source code determines the namespace it will
# live in, and hence its scope of visibility

Y = 88      # Global (module) scope
def func3():
    Y = 99  # Local (function) scope, a different variable
print(Y)     # 88

# If you need to assign a name that
# lives at the top level of the module enclosing the function, 
# you can do so by declaring it in a global statement inside the function.

# Names not assigned a value in the function definition are assumed
# to be enclosing scope locals

# Also note that any type of assignment within a function classifies a name as local.

# Conversely, in-place changes to objects do not classify names as locals; only actual name
# assignments do. For instance, if the name L is assigned to a list at the top level of a
# module, a statement L = X within a function will classify L as a local, but L.append(X)
# will not. In the latter case, we are changing the list object that L references, not L itself

# LEGB RULE
# Name assignments create or change local names by default.
# Name references search at most four scopes: local, then enclosing functions (if any),
# then global, then built-in.
# Names declared in global and nonlocal statements map assigned names to en-
# closing module and function scopes, respectively.

# In other words, all names assigned inside a function def statement (or a lambda, an
# expression we'll meet later) are locals by default. Functions can freely use names as-
# signed in syntactically enclosing functions and the global scope, but they must declare
# such nonlocals and globals in order to change them.

# for loop statements never localize their variables to the statement block in any Python
# List comprehensions usually localize (p.490), but rules are a bit more
# complicated

# try except E as X, in 3.x X is local to except block, it 2.x they
# live on after try statement

x = 99 # global scope
p = 55 # global scope

def func4(y):
    global x
    z = x + y # local scope
    x = 999
    p = 777
    return z

rv = func4(1)
print(rv, x, p)  # (100, 999, 55)

# Because the names True and False in 2.X are just variables in the built-in scope and are not reserved,
# it's possible to reassign them with a statement like True = False.
# This statement merely redefines the word True for the single scope in which it appears to return False.
True = False
if True == False:
    print("Strange")  # Strange
    
del True
if True != False:
    print("Fine")     # Fine


print('-' * 10 + "A.3. Global" + '-' * 10)

xx = 88

def func5():
    global xx
    xx = 99
    # global statement maps 'yyy' to the module's scope explicitly. 
    # We didn't declared 'yyy' before
    global yy  
    yy = 100

func5()
print(xx, yy)  # (99, 100)

# Other ways to work with global variables

var = 99

def local():
    var = 0                 # Change local var

def glob1():
    global var              # Declare global (normal)
    var += 1                # Change global var

def glob2():
    var = 0                 # Change local var 
    import functions_basic          # Import myself
    functions_basic.var += 1        # Change global var

def glob3():
    var = 0                          # Change local var
    import sys                       # Import system table
    glob = sys.modules['functions_basic']    # Get module object (or use __name__)
    glob.var += 1                    # Change global var


def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)

test()  # 99 102, also print(100) comes from somewhere (when the module import itself)

# Interesting thoughts on the example below
# 
# https://stackoverflow.com/questions/25277807/when-a-module-imports-itself-what-happens-to-the-global-variables