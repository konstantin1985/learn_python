# A reference (X) looks for the name X first in the current local scope (function); then
# in the local scopes of any lexically enclosing functions in your source code, from
# inner to outer; then in the current global scope (the module file); and finally in the
# built-in scope (the module builtins). global declarations make the search begin
# in the global (module file) scope instead.

# An assignment (X = value) creates or changes the name X in the current local
# scope, by default. If X is declared global within the function, the assignment creates
# or changes the name X in the enclosing module's scope instead. If, on the other
# hand, X is declared nonlocal within the function in 3.X (only), the assignment
# changes the name X in the closest enclosing function's local scope.

# When nested functions are present, variables in enclosing functions may be referenced,
# but they require 3.X nonlocal declarations to be changed.

print('-' * 10 + "A.1. Basic nested functions" + '-' * 10)

A = 99     # Global scope name: not used 
def func1():
    A = 88
    def func2():
        print(A)
    func2()
func1()    # print 88, from enclosing def
# func2()  # NameError: name 'func2' is not defined

# This enclosing scope lookup works even if the enclosing function has already returned.
# func4 remembers the enclosing scope's X in func3, even though f1 is no longer active
def func3():
    A = 77
    def func4():
        print(A)
    return func4  # We return a function here
somef = func3()   # Assign function pointer (func4)
somef()           # Invoke function some f that really runs func4, 77 is printed

print('-' * 10 + "A.2. Factory functions or closure" + '-' * 10)

# The function object in question remembers values in enclosing scopes 
# regardless of whether those scopes are still present in memory. 
# In effect, they have attached packets of memory, 
# which are local to each copy of the nested function created.

# N from the enclosing local scope is retained as state
# information attached to the generated action, which is why we get back its argument
# squared when it is later called.

# maker makes action, but simply returns action without running it
def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)      # What we get back is a reference to the generated nested function
print(f)          # <function action at 0xb7307bfc>
print(f(3))       # 9

# Each call to a factory function like this gets its own set of state information.
g = maker(3)
print(g(4))       # 64
print(f(4))       # 16

# Lambda functions retain state too
def makerl(N):
    return lambda X: X ** N
h = makerl(3)
print(h(4))       # 64

# Factory functions provide per-call localized storage for data required
# by a single nested function. They are a lightweight alternative to classes.

# The criteria that must be met to create closure in Python are summarized in the following points.
# - We must have a nested function (function inside a function).
# - The nested function must refer to a value defined in the enclosing function.
# - The enclosing function must return the nested function.
# Decorators in Python make an extensive use of closures as well.

# We can find out values that get enclosed in the closure function
print(h.__closure__[0].cell_contents)  # 3

print('-' * 10 + "A.3. Retaining enclosing scope with defaults" + '-' * 10)

# In early Python enclosed functions didn't automatically remember values from the enclosing scope, 
# so the default arguments were used
def func5():
    x = 99
    def func6(x=x):
        print(x)
    func6()
func5()           # 88


print('-' * 10 + "A.4. Nested scopes and lambdas" + '-' * 10)

# Lambda is an expression that generates a new function to be called later, 
# much like a def statement.
# Because it's an expression, it can be used in places that def cannot, such as
# within list and dictionary literals.

def func7():
    x = 4
    action = (lambda n: x ** n)
    return action
x = func7()
print(x(3))  # 4 ** 3 = 64

# The following works even in old Python
def func8():
    x = 4
    action = (lambda n, x=x: x ** n)
    return action
x = func8()
print(x(3))  # 64

print('-' * 10 + "A.5. Loop variables may require defaults" + '-' * 10)

# We attempt to build up a list of functions that each remember the current 
# variable i from the enclosing scope

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts
acts = makeActions()
print(acts[0])  # <function <lambda> at 0xb7363e64>

# It doesn't work because the enclosing scope variable is looked up
# when the nested functions are later called, they all effectively remember the same value:
# the value the loop variable had on the last loop iteration
print(acts[0](2))  # 2 ** 4 = 16
print(acts[1](2))  # 2 ** 4 = 16
print(acts[2](2))  # 2 ** 4 = 16

# This is the one case where we still have to explicitly retain enclosing scope values with
# default arguments, rather than enclosing scope references. 
# Because defaults are evaluated when the nested function is created (not when
# it's later called), each remembers its own value for i

def makeActions2():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts
acts = makeActions2()
print(acts[0](2))  # 0 ** 2 = 0
print(acts[1](2))  # 1 ** 2 = 1
print(acts[2](2))  # 2 ** 2 = 4

# Some more information on Python closure
# https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures

print('-' * 10 + "A.6. Arbitrary scope nexting" + '-' * 10)

def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()  # 99


print('-' * 10 + "A.7. Python 3.x nonlocal" + '-' * 10)

# In Python 3.X (not in 2.X), we can also change such enclosing scope variables, 
# as long as we declare them in nonlocal statements. With this statement, nested
# defs can have both read and write access to names in enclosing functions. This makes
# nested scope closures more useful, by providing changeable state information.

# Unlike global, nonlocal names MUST (!) already
# exist in the enclosing function's scope when declared-they can exist only in enclosing
# functions and cannot be created by a first assignment in a nested def.

# In Python 2.X, when one function def is nested
# in another, the nested function can reference any of the names defined by assignment
# in the enclosing def's scope, but it cannot change them. In 3.X, declaring the enclosing
# scopes' names in a nonlocal statement enables nested functions to assign and thus
# change such names as well.

# nonlocal names can appear only in enclosing defs, not in
# the module's global scope or built-in scopes outside the defs.

# This works even though tester has returned and exited by the time 
# we call the returned nested function through the name F
# Each call makes a new, distinct state object, such that updating one function's state won't
# impact the other
'''
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('spam')  # spam 0
F('ham')   # ham 1
F('eggs')  # eggs 2

# In a closure function, nonlocals are per-call, multiple copy data
G = tester(42)
G('spam')   # spam 42
G('eggs')   # eggs 43
F('bacon')  # bacon 3

# nonlocal restricts the scope lookup to just enclosing defs; nonlocals are not
# looked up in the enclosing module's global scope or the built-in scope outside all defs

# These restrictions make sense once you realize that Python would not otherwise 
# generally know which enclosing scope to create a brand-new name in.

spam = 99
def tester():
    def nested():
        # nonlocal spam  # SyntaxError: no binding for nonlocal 'spam' found
        print('Current = ', spam)
        spam += 1
    return nested

'''

print('-' * 10 + "A.8. State retention options: state with nonlocal (only Python 3.x)" + '-' * 10)

# Each call to tester creates a self-contained package of
# changeable information, whose names do not clash with any other part of the program

'''
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')  # spam 0
# F.state  # AttributeError: 'function' object has no attribute 'state'
'''

print('-' * 10 + "A.8. State retention options: state with globals, a single copy only" + '-' * 10)

def tester(start):
    global state  # Move it out to the module to change it
    state = start
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')  # spam 0
F('eggs')  # eggs 1

# It only allows for a single shared copy of the state information in the module scope
G = tester(42)
G('toast')  # toast 42
G('bacon')  # beacon 43
F('ham')    # ham 44

# As shown earlier, when you are using nonlocal and nested function closures instead of
# global, each call to tester remembers its own unique copy of the state object.


# How global works with nested function scopes

print("-" * 10)

def tester():
    testVar = 11
    def nested():
        testVar = 55
        print(testVar)    # 55
    nested()
    print(testVar)        # 11
tester()

print("-" * 10)

def tester():
    testVar = 11
    def nested():
        global testVar  
        # print(testVar)  # NameError: global name 'testVar' is not defined
        testVar = 55
        print(testVar)    # 55 
    nested()
    print(testVar)        # 11
tester()

print("-" * 10)

testVar = 7
def tester():
    testVar = 11
    def nested():
        global testVar
        print(testVar)    # 7
        testVar = 55
        print(testVar)    # 55 
    nested()
    print(testVar)        # 11
tester()
print(testVar)            # 55

print('-' * 10 + "A.9. State retention options: classes, explicit attributes" + '-' * 10)

class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1
F = tester(0)
F('eggs')  # (eggs, 0)
F('ham')   # (eggs, 1)

print('-' * 10 + "A.10. State retention options: function attributes" + '-' * 10)

# When you attach user-defined attributes to nested functions 
# generated by enclosing factory functions, they can also serve as per-call, multiple copy, and
# writable state, just like nonlocal scope closures and class attributes.

# Moreover, function attributes allow state variables to be accessed outside the nested
# function, like class attributes; with nonlocal, state variables can be seen directly only
# within the nested def.

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(10)
F('eggs')   # (eggs, 10)
F('ham')    # (ham, 11)

G = tester(20)
G('bacon')  # (bacon, 20)
G('spam')   # (bacon, 21)
F('tam')    # (tam, 12)

print(F.state) # 13
print(G.state) # 22
print(F is G)  # False

print('-' * 10 + "A.11. State retention options: leverage mutability of lists" + '-' * 10)

def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1 
    state = [start]
    return nested
    
F = tester(0)
F("eggs")  # ('eggs', 0)
F("ham")   # ('ham', 1)
