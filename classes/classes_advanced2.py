


# Lutz Chepter 32

print("-" * 20 + "#1 Extending Built-in Types by Embedding" + "-" * 20)

# The following example implements a new set object type by moving some 
# of the set functions to methods and adding some basic operator overloading.

class Set:
    
    def __init__(self, value = []):                            # Constructor
        self.data = []
        self.concat(value)
        
    def intersect(self, other):                                # other is any sequence
        res = []                                               # self is the subject
        for x in self.data:
            if x in other:                                     # Pick common items
                res.append(x)
        return Set(res)                                        # Return a new Set
    
    def union(self, other):                                    # other is any sequence
        res = self.data[:]                                     # Copy my data
        for x in other:                                        # Add items from other 
            if x not in res:                                   # "not in res" - important because we don't want to have the same item
                res.append(x)
        return Set(res)
    
    def concat(self, value):                                   # value: list, Set ...
        for x in value:                                        # Remove duplicates
            if x not in self.data:
                self.data.append(x)        
    
    def __len__(self):                                         # len(self), is self
        return len(self.data)
    
    def __getitem__(self, key):                                # self[i], self[i:j]
        return self.data[key]                         
    
    def __and__(self, other):                                  # self & other
        return self.intersect(other)
    
    def __or__(self, other):                                   # self | other
        return self.union(other)
    
    def __repr__(self):                                        # print(self) 
        return 'Set: ' + repr(self.data)
    
    def __iter__(self):                                        # for x in self 
        return iter(self.data)
        
x = Set([1, 3, 5, 7])
print(x)                                                       # Set: [1, 3, 5, 7]
print(x.union(Set([1, 4, 7])))                                 # Set: [1, 3, 5, 7, 4] 
print(x | Set([1, 4, 6]))                                      # Set: [1, 3, 5, 7, 4, 6]

# Works with other iterables too
print(x & [1, 4, 7])                                           # Set: [1, 7]
    
print("-" * 20 + "#2 Extending Built-in Types by Subclassing" + "-" * 20)

# Instances of your type subclasses can generally be used anywhere that the
# original built-in type can appear. Beginning with Python 2.2, all the built-in 
# types in the language can now be subclassed directly (list, str, dict, and tuple).

# Subclassing of list that starts indexing with 1 instead of 0

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

print(list('abc'))
x = MyList('abc')                                              # __init__ inherited from list
print(x)                                                       # __repr__ inherited from list

for element in x:
    print(element),                                            # a b c
print('')

# MyList.__getitem__ customizes list superclass method
print(x[1])                                                    # (indexing ['a', 'b', 'c'] at 1) a
print(x[3])                                                    # (indexing ['a', 'b', 'c'] at 3) c

# Attributes from list superclass
x.append('spam'); print(x)                                     # ['a', 'b', 'c', 'spam']
x.reverse();      print(x)                                     # ['spam', 'c', 'b', 'a']

print("-" * 20 + "#3 The 'New Style' Class Model" + "-" * 20)

# In Python 3.X, all classes are automatically what were formerly called 'new style,'
# whether they explicitly inherit from object or not. Coding the object superclass is
# optional and implied.

# In Python 2.X, classes must explicitly inherit from object (or another built-in type)
# to be considered 'new style' and enable and obtain all new-style behavior. Classes
# without this are 'classic.'

print("-" * 20 + "#3.1 Attribute Fetch for Built-ins Skips Instances" + "-" * 20)

# A key difference between __getattr__ and __getattribute__ is that __getattr__ is 
# only invoked if the attribute wasn't found the usual ways. It's good for implementing
# a fallback for missing attributes, and is probably the one of two you want.
# __getattribute__ is invoked before looking at the actual attributes on the object, 
# and so can be tricky to implement correctly. You can end up in infinite recursions
# very easily.

# In new style classes:
# - implicit built-in operators (print(), X[]) aren't routed to __getattr__
# - explicit built-in operators (X.__str__(), X.__getitem()) are routed to __getattr__
# - normally named methods are routed to __getattr__
# In old style classes:
# - all the above are routed to __getattr__

class C(object):
    data = 'spam'
    def __getattr__(self, name):                               # Built-ins not routed to getattr 
        print(name)
        return getattr(self.data, name)
    
X = C()
# X[0]                                                         # TypeError: 'C' object does not support indexing
print(X)                                                       # <__main__.C object at 0xb7377f4c> - inherited from 'object'


class C:
    data = 'spam'
    def __getattr__(self, name):                               # Classic classes in 2.X: catches built-ins 
        print(name)
        return getattr(self.data, name)

X = C()
X[0]                                                           # __getattr__ => __getitem__ => s
print(X)                                                       # __getattr__ => __str__ => spam - Classic classes don't inherit default

# In new style classes:
# - Implicit calls to built-in operations aren't looked up into instance, only in class 
# In old style classes:
# - Implicit calls to built-in operations are looked up into instance

class C(object):                                               # 2.X/3.X new-style class    
    def __sub__(self, other):
        return 88 - other

X = C()
X.normal = lambda: 99
X.normal()                                                     # Normals still from instance

X.__add__ = lambda(y): 88 + y
X.__add__(1)                                                   # Ditto for explicit built-in names
 
# print(X + 1)                                                 # TypeError: unsupported operand type(s) for +: 'C' and 'int'
print(X - 1)                                                   # 87 - fine, __sub__ is PART OF CLASS, NOT INSTANCE of the class


class C: pass                                                  # 2.X classic class  

X = C()
X.normal = lambda: 99
print(X.normal())                                              # 99 - normally named method

X.__add__ = lambda(y): 88 + y
print(X.__add__(1))                                            # 89 - __add__ is called explicitly
print(X + 1)                                                   # 89 - __add__ is called implicitly

# Proxy coding requirements
# In a more realistic delegation scenario, this means that built-in operations like 
# expressions no longer work the same as their traditional direct-call equivalent. 
# Asymmetrically, direct calls to built-in method names still work, but equivalent 
# expressions do not because through-type calls fail for names not at the class 
# level and above.

class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)

X = C()
print(X.__getitem__(1))                                        # getattr: __getitem__ => p - direct calls to built-in method
# print(X[1])                                                  # TypeError: 'C' object does not support indexing - built-in operations like expressions no longer work the same 
# type(X).__getitem__(X, 1)                                    # AttributeError: type object 'C' has no attribute '__getitem__' 

print(X.__add__('eggs'))                                       # getattr: __add__ => spameggs - direct calls to built-in method
# print(X + 'eggs')                                            # TypeError: unsupported operand type(s) for +: 'C' and 'str'
# type(X).__add__(X, 'eggs')                                   # AttributeError: type object 'C' has no attribute '__add__'

# The net effect: to code a proxy of an object whose interface may in part be invoked by
# built-in operations, new-style classes require both __getattr__ for normal names, as
# well as method redefinitions for all names accessed by built-in operations-whether
# coded manually, obtained from superclasses, or generated by tools. 

print("-" * 20 + "#3.2 Type Model Changes" + "-" * 20)

# The type object, returned by the type built-in function, is an object that
# gives the type of another object; its result differs slightly in 3.X, because 
# types have merged with classes completely.

L = [1, 2, 3]
print(type(L))                                                 # 2.X <type 'list'>; 3.X <class 'list'>

# Classes are types
# The type object generates classes as its instances, and classes generate instances of
# themselves. Both are considered types, because they generate instances. In fact,
# there is no real difference between built-in types like lists and strings and user-
# defined types coded as classes. This is why we can subclass built-in types, as shown
# earlier in this chapter-a subclass of a built-in type such as list qualifies as a new-
# style class and becomes a new user-defined type.

# Types are classes
# New class-generating types may be coded in Python as the metaclasses we'll meet
# later in this chapter-user-defined type subclasses that are coded with normal
# class statements, and control creation of the classes that are their instances. As
# we'll see, metaclasses are both class and type, though they are distinct enough to
# support a reasonable argument that the prior type/class dichotomy has become
# one of metaclass/class, perhaps at the cost of added complexity in normal classes.

# With Python 2.X's classic classes, the type of a class instance is a
# generic "instance", but the types of built-in objects are more specific

class C: pass                                                  # Classic classes in 2.X
I = C()
print(type(I), I.__class__)                                    # (<type 'instance'>, <class __main__.C at 0xb72dc35c>)
print(type(C))                                                 # <type 'classobj'> - But classes are not the same as types
# print(C.__class__)                                           # AttributeError: class C has no attribute '__class__'

print(type([1, 2, 3]), [1, 2, 3].__class__)                    # (<type 'list'>, <type 'list'>)
print(type(list), list.__class__)                              # (<type 'type'>, <type 'type'>)

# But with new-style classes in 2.X, the type of a class instance is the class it's created
# from, since classes are simply user-defined types-the type of an instance is its class,
# and the type of a user-defined class is the same as the type of a built-in object type.
# Classes have a __class__ attribute now, too, because they are instances of type

class C(object): pass                                          # New-style classes in 2.X
I = C()

# Type of instance is class it's made from
print(type(I), I.__class__)                                    # (<class '__main__.C'>, <class '__main__.C'>)

print(type(C), C.__class__)                                    # (<type 'type'>, <type 'type'>)

# The same is true for all classes in Python 3.X, since all classes are automatically new-
# style, even if they have no explicit superclasses.

# Type checking is usually the wrong thing to do in Python programs
# (we code to object interfaces, not object types), and the more general
# isinstance built-in is more likely what you'll want to use
# in the rare cases where instance class types must be queried.

# IMPORTANT EXAMPLE

class C: pass
class D: pass

c, d = C(), D()
print(type(c) == type(d))                                      # Python 2.X True, Python 3.X False

# Python 2.X (<type 'instance'>, <type 'instance'>)
# Python 3.X ((<class '__main__.C'>, <class '__main__.D'>))
print(type(c), type(d))                                        

print("-" * 20 + "#3.3 All Classes Derive from 'object'" + "-" * 20)

class C(object): pass

X = C()
print(type(X), type(C))                                        # (<class '__main__.C'>, <class 'type'>)

# As before (in new style classes), the type of a class instance is the 
# class it was made from, and the type of class is the type class because
# classes and types have merged in the new style classes

# It is also true, though, that the instance and class are both derived
# from the built-in object class and type, an implicit or explicit 
# superclass of every class

print(isinstance(X, object))                                   # True (2.X, 3.X)
print(isinstance(C, object))                                   # True (2.X, 3.X)
print(isinstance('spam', object))                              # True (2.X, 3.X)

# In fact, type itself derives from object, and object derives from type,
# even though the two are different objects-a circular relationship that 
# caps the object model and stems from the fact that types are classes 
# that generate classes

print(type(type))                                              # <type 'type'>
print(type(object))                                            # <type 'type'>
print(isinstance(type, object))                                # True
print(isinstance(object, type))                                # True 
print(type is object)                                          # False

# This model has a number of practical implications. For one thing, it
# means that we sometimes must be aware of the method defaults that come 
# with the explicit or implicit object root class in new-style classes only.

class C: pass
print(C.__bases__)                                             # () Classic classes do not inherit from object
X = C()
# print(X.__repr__)                                            # AttributeError: C instance has no attribute '__repr__'

class C(object): pass
print(C.__bases__)                                             # (<type 'object'>,) New-style classes inherit object defaults
X = C()
print(X.__repr__)                                              # <method-wrapper '__repr__' of C object at 0xb72d482c>

print("-" * 20 + "#3.4 Diamond Inheritance Change" + "-" * 20)

# For classic classes (the default in 2.X): DFLR
# The inheritance search path is strictly depth first, and then left to 
# right-Python climbs all the way to the top, hugging the left side of
# the tree, before it backs up and begins to look further to the right. 

# For new-style classes (optional in 2.X and automatic in 3.X): MRO
# The inheritance search path is more breadth-first in diamond cases-Python 
# first looks in any superclasses to the right of the one just searched 
# before ascending to the common superclass at the top. In other words, 
# this search proceeds across by levels before moving up. 

# The new-style MRO allows lower superclasses to overload attributes of
# higher superclasses, regardless of the sort of multiple inheritance 
# trees they are mixed into. Moreover, the new-style search rule avoids
# visiting the same superclass more than once when it is accessible from
# multiple subclasses.

# Classic classes

# The attribute x.attr here is found in superclass A, because with classic 
# classes, the inheritance search climbs as high as it can before backing
# up and moving right. For this attribute, the search stops as soon as attr 
# is found in A, above B.

class A:         attr = 1
class B(A):      pass
class C(A):      attr = 2
class D(B, C):   pass                                          # Tries A before C (depth first)

x = D()
print(x.attr)                                                  # 1 - Searches x, D, B, A

# However, with new-style classes derived from a built-in like object (and 
# all classes in 3.X), the search order is different: Python looks in C to
# the right of B, before trying A above B. For this attribute, the search 
# stops as soon as attr is found in C.

class A(object):  attr = 1
class B(A):       pass
class C(A):       attr = 2
class D(B, C):    pass                                          # Tries C before A

x = D()
print(x.attr)                                                   # 2 - Searches x, D, B, C

# This change in the inheritance search procedure is based upon the assumption
# that if you mix in C lower in the tree, you probably intend to grab its 
# attributes in preference to A's.

# If you want more control over the search process, you can always force the 
# selection of an attribute from anywhere in the tree by assigning or otherwise
# naming the one you want at the place where the classes are mixed together.

# Chooses new-style order in a classic class by resolving the choice explicitly

class A:          attr = 1
class B(A):       pass
class C(A):       attr = 2
class D(B, C):    attr = C.attr                                 # Choose C, to the right  

x = D()
print(x.attr)                                                   # 2 - Works like new-style

# New-style classes can similarly emulate classic classes by choosing the 
# higher version of the target attribute at the place where the classes
# are mixed together

class A(object):  attr = 1
class B(A):       pass
class C(A):       attr = 2
class D(B, C):    attr = B.attr                                 # Choose A.attr above

x = D()
print(x.attr)                                                   # 1 - Works like classic classes

# Naturally, attributes picked this way can also be method functions-methods are 
# normal, assignable attributes that happen to reference callable function objects.

# Every case of multiple inheritance exhibits the diamond pattern today. 
# That is, in new-style classes, object automatically plays the role that 
# the class A does in the example we just considered. Hence the new-style MRO
# search rule not only modifies logical semantics, but is also an important 
# performance optimization-it avoids visiting and searching the same class
# more than once, even the automatic object.

# Without the new-style MRO search order, in multiple inheritance cases
# the defaults in object would always override redefinitions in user-coded 
# classes, unless they were always made in the leftmost superclass. In other
# words, the new-style class model itself makes using the new-style search
# order more critical!

# IMPORTANT:
# In short, though, the MRO essentially works like this:
# 1. List all the classes that an instance inherits from using the classic 
# class's DFLR lookup rule, and include a class multiple times if it's visited
# more than once.
# 2. Scan the resulting list for duplicate classes, removing all but the last 
# occurrence of duplicates in the list.

# The class.__mro__ attribute is available only on new-style classes; 
# it's not present in 2.X unless classes derive from object.

# For diamond inheritance patterns only, the search is the new order 
# we've been studying-across before up

class A(object):    pass
class B(A):         pass                                        # Diamonds: order differs for newstyle
class C(A):         pass                                        # Breadth-first across lower levels
class D(B, C):      pass
print(D.__mro__)                                                # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)

# For nondiamonds, though, the search is still as it has always been 
# (albeit with an extra object root) - to the top, and then to the right

class A(object):    pass
class B(A):         pass                                        # Nondiamonds: order same as classic 
class C(object):    pass                                        # Depth first, then left to right
class D(B, C):      pass

# Why so? Pay attention to the MRO algorithm above
print(D.__mro__)                                                # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <type 'object'>)

print("-" * 20 + "#4 New-Style Class Extensions" + "-" * 20)














