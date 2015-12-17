
print "-"*20 + "#1 Headers: Collecting arguments" + "-"*20

'''
For instance, in the following, 1 is passed to a by
position, 2 and 3 are collected into the pargs positional tuple, and x and y wind up in
the kargs keyword dictionary
'''

def f(a, *pargs, **kargs): print(a, pargs, kargs)

f(1, 2, 3, 4, x=1, y=2)   #(1, (2, 3, 4), {'y': 2, 'x': 1})
#f(1, 2, 3, 4, x=1, y=2, 5)  #SyntaxError: non-keyword arg after keyword arg


print "-"*20 + "#2 Calls: Unpacking arguments" + "-"*20

'''
In all recent Python releases, we can use the * syntax when we call a function, too. In
this context, its meaning is the inverse of its meaning in the function definition-it
unpacks a collection of arguments, rather than building a collection of arguments.
'''

def func(a, b, c, d):
    print(a, b, c, d)

args = (1, 2)
args += (3, 4)
func(*args)                         #(1, 2, 3, 4)

args = {'a':1, 'b':2, 'c':3}
args['d'] = 4
func(**args)                        #(1, 2, 3, 4)
func(*args)                         #('a', 'c', 'b', 'd')

func(*(1, 2), **{'d': 4, 'c': 3})   #(1, 2, 3, 4)
func(1, c=3, *(2,), **{'d': 4})     #(1, 2, 3, 4)

'''
Again, don''t confuse the * / ** starred-argument syntax in the function header and the function call
-in the header it collects any number of arguments, while in the call it unpacks any
number of arguments. In both, one star means positionals, and two applies to key-words.
'''





