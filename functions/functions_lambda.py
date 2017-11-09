

# Like def, this expression creates a function to be called later, 
# but it returns function instead of assigning it to a name. 
# This is why lambdas are sometimes known as anonymous (i.e., unnamed)
# functions. In practice, they are often used as a way to inline
# a function definition, or to defer execution of a piece of code.


print('-' * 10 + "A.1. lambda Basics" + '-' * 10)

# lambda argument1, argument2,... argumentN : expression using arguments

# Differences from def:
# - lambda is an expression, not a statement. Because of this, a lambda can appear in
#places a def is not allowed by Python's syntax-inside a list literal or a function
# call's arguments, for example.  lambda returns a value (a new function) 
# that can optionally be assigned a name.

# - lambda's body is a single expression, not a block of statements.
# Because it is limited to an expression, a lambda is less general 
# than a def-you can only squeeze so much logic into a lambda body
# without using statements such as if. 

# Apart from those distinctions, defs and lambdas do the same sort of work.

def func(x, y): return x + y
print(func(2, 3))       # 5

f = lambda x, y: x + y  # can't have print() here 
print(f(2, 3))          # 5

# Defaults work on lambda arguments, just like in a def
x = (lambda a = "pi", b = "fi", c = 'fo' : a + b + c)
print(x('li'))  # lififo

# The code in a lambda body also follows the same scope lookup rules as code inside a
# def. lambda expressions introduce a local scope much like a nested def, which 
# automatically sees names in enclosing functions, the module, and the built-in scope

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)  # title in enclosing def scope
    return action                         # return a function object

act = knights()
msg = act('robin')                        # robin passed to x
print(msg)                                # Sir robin
print(act)                                # <function <lambda> at 0xb730bbc4>

print('-' * 10 + "A.2. Why use lambda?" + '-' * 10)

# lambda is also commonly used to code jump tables, which are
# lists or dictionaries of actions to be performed on demand.

# The equivalent def coding would require temporary function names 
# (which might clash with others) and function definition

# A list of three callable functions. Inline function definition.
L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))  # 4, 8, 16

print(L[0](3))   # 9

# The lambda expression is most useful as a shorthand for def, when you need to stuff
# small pieces of executable code into places where statements are illegal syntactically

# Example that illustrates the interactive prompt
# Here, when Python makes the temporary dictionary, each of the nested lambdas 
# generates and leaves behind a function to be called later. Indexing by key fetches
# one of those functions, and parentheses force the fetched function to be called.

key = 'got'
rv = {'already': (lambda: 2 + 2),
      'got':     (lambda: 2 * 4),
      'one':     (lambda: 2 * 6)}[key]()
print(rv)  # 8

# The code proximity that lambdas provide is especially useful for
# functions that will only be used in a single context - if the three 
# functions here are not useful anywhere else, it makes sense to 
# embed their definitions within the dictionary as lambdas.

print('-' * 10 + "A.3. How not to obfuscate your Python code" + '-' * 10)

# For example, if you want to print from the body of a lambda function, 
# simply print(X) in Python 3.X where this becomes a call expression instead 
# of a statement,say sys.stdout.write(str(X)+'\n') in either Python 2.X or 3.X

# We can use ternary expressions
lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))  # aa
print(lower('aa', 'bb'))  # aa

# Furthermore, if you need to perform loops within a lambda, you can 
# also embed things like map calls and list comprehension expressions

import sys
showall = lambda x: [sys.stdout.write(line) for line in x]
showall(('bright\n', 'side\n', 'of\n', 'life\n'))

print('-' * 10 + "A.4. Nested lambda" + '-' * 10)

# For readability, nested lambda are better avoided

def func5(y):
    return (lambda x: x + y)

f = func5(5)  # 
print(f)      # <function <lambda> at 0xb739dd14>
print(f(3))   # 8

func6 = lambda x: (lambda y: x + y) # return lambda y: x + y with certain x
g = func6(5)  # x = 5
print(g)      # <function <lambda> at 0xb7380d84>
print(g(3))   # 8

print('-' * 10 + "A.5. Lambda callbacks" + '-' * 10)

# Here, we register the callback handler by passing a function generated with a lambda to
# the command keyword argument. The advantage of lambda over def here is that the code
# that handles a button press is right here, embedded in the button-creation call.
# In effect, the lambda defers execution of the handler until the event occurs

#class MyGui:
#    def makewidgets(self): 
#        Button(command=(lamda: self.onPress("spam")))
#    def onPress(self, message):
#        ...use message...

