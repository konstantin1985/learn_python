

# What are "first class" objects?, it means there are no restrictions 
# on the object's use. It's the same as any other object.

# A first class object is an entity that can be dynamically created, 
# destroyed, passed to a function, returned as a value, and have all
# the rights as other variables in the programming language have.

# In C++ functions themselves are not first class objects, however:

# You can override the '()' operator making it possible
# to have an object function, which is first class.
# Function pointers are first class.

print('-' * 10 + "A.1. Indirect function calls, first class objects" + '-' * 10)

# There's really nothing special about the name used in a def statement: 
# it's just a variable assigned in the current scope,
# as if it had appeared on the left of an = sign. After a def runs,
# the function name is simply a reference to an object-you can reassign 
# that object to other names freely and call it through any reference

def echo(message):      # Name echo assigned to function object
    print(message)
    
echo('Direct call')     # Call object through original name

x = echo                # Now x references the function too
x('Indirect call')      # Call object through name by adding ()

# Because arguments are passed by assigning objects, it's just as easy
# to pass functions to other functions as arguments.

def indirect(func, arg):
    func(arg)                     # Call the passed-in object by adding ()

indirect(echo, 'Argument call')   # Pass the function to another function

# Because Python compound types like these can contain any sort
# of object, there's no special case here

schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg)                     # Spam! Ham!

# Functions can be returned
def make(label):
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam')
F('Ham!')          # Spam:Ham!
F('Eggs!')         # Spam:Eggs!

print('-' * 10 + "A.2. Function introspection" + '-' * 10)

# But the call expression is just one operation defined to work on function 
# objects. We can also inspect their attributes generically

def func(a):
    b = 'spam'
    return b * a

print(func(3))                    # spamspamspam

print(func.__name__)              # func
print(func.__code__.co_varnames)  # ('a', 'b')
print(func.__code__.co_argcount)  # 1

print('-' * 10 + "A.3. Function attributes" + '-' * 10)

# It's been possible to attach arbitrary user-defined 
# attributes to functions

print(func)               # <function func at 0xb735380c> 
func.count = 0
func.count += 1
print(func.count)         # 1
print(dir(func))          # There is 'count' attribute

# In 3.X, all function internals' names have leading and trailing
# double underscores ('__X__'); 2.X follows the same scheme, 
# but also assigns some names that begin with 'func_X'

# In a sense, this is also a way to emulate 'static locals' in other 
# languages-variables whose names are local to a function, but whose
# values are retained after a function exits.

'''

# In Python 3.X (but not 2.X), it's also possible to attach annotation 
# information arbitrary user-defined data about a function's arguments
# and result to a function OBJECT

# For arguments, they appear after a colon immediately following the 
# argument's name; for return values, they are written after a -> 
# following the arguments list.


def func2(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
func2(1, 2, 3)  # 6


# Calls to an annotated function work as usual, but when annotations are present Python
# collects them in a dictionary and attaches it to the function object itself. Argument
# names become keys, the return value annotation is stored under key 'return' if coded


print(func2.__annotations__)
# {'c': <class 'float'>, 'b': (1, 10), 'a': 'spam', 'return': <class 'int'>}


# Because they are just Python objects attached to a Python object, annotations are
# straightforward to process.

def func3(a: 'spam', b, c: 99):
    return a + b + c

print(func3(1, 2, 3))         # 6
print(func3.__annotations__)  # {'c': 99, 'a': 'spam'}

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])
# c => 99
# a => spam

# It's easy to imagine annotations being used to specify constraints for argu-
# ment types or values, though, and larger APIs might use this feature as a way 
# to register function interface information.

'''