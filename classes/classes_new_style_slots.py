
# USEFUL LINKS

# https://stackoverflow.com/questions/472000/usage-of-slots
# https://www.python-course.eu/python3_slots.php
# http://tech.oyster.com/save-ram-with-python-slots/

# GENERAL DESCRIPTION

# The attributes of objects are stored in a dictionary "__dict__". Like any other dictionary, 
# a dictionary used for attribute storage doesn't have a fixed number of elements. In other
# words, you can add elements to dictionaries after they have been defined, as we have seen
# in our chapter on dictionaries. This is the reason, why you can dynamically add attributes
# to objects of classes.

# Using a dictionary for attribute storage is very convenient, but it can mean a waste of space
# for objects, which have only a small amount of instance variables. The space consumption can
# become critical when creating large numbers of instances. Slots are a nice way to work around
# this space consumption problem. Instead of having a dynamic dict that allows adding attributes
# to objects dynamically, slots provide a static structure which prohibits additions after the
# creation of an instance. 

# When we design a class, we can use slots to prevent the dynamic creation of attributes. 
# To define slots, you have to define a list with the name __slots__. The list has to contain
# all the attributes, you want to use.

print("-" * 20 + "#1 Slots: Attribute Declarations" + "-" * 20)

# To use slots, assign a sequence of string names to the special __slots__
# variable and attribute at the top level of a class statement: only those
# names in the __slots__ list can be assigned as instance attributes. 
# However, like all names in Python, instance attribute names must still 
# be assigned before they can be referenced, even if they're listed in __slots__.

class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
# print(x.age)                                                  # AttributeError: age
x.age = 40
print(x.age)                                                    # 40

# x.ape = 1000                                                  # AttributeError: 'limiter' object has no attribute 'ape'

# First off, when slots are used, instances do not normally have an attribute dictionary

# print(x.__dict__)                                             # AttributeError: 'limiter' object has no attribute '__dict__'  

# However, we can still fetch and set slot-based attributes by name string
# using storage-neutral tools such as getattr and setattr (which look beyond
# the instance __dict__ and thus include class-level names like slots) and 
# dir (which collects all inherited names throughout a class tree):

print(getattr(x, 'age'))                                        # 40
# print(getattr(x, 'job'))                                      # AttributeError: job

setattr(x, 'name', 'Bob')
print(getattr(x, 'name'))                                       # Bob

print('age' in dir(x))                                          # True
print('job' in dir(x))                                          # True

# Slots are also something of a major break with Python's core dynamic 
# nature, which dictates that any name may be created by assignment. 
# In fact, they imitate C++ for efficiency at the expense of flexibility,
# and even have the potential to break some programs. 

# Best reserved for rare cases where there are large numbers of instances
# in a memory-critical application.

# Also keep in mind that without an attribute namespace dictionary, 
# it's not possible to assign new names to instances that are not names 
# in the slots list

class D(object):
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4                                              # Cannot add new names if no __dict__
        
# X = D()                                                       # AttributeError: 'D' object has no attribute 'd'

# We can still accommodate extra attributes, though, by including 
# __dict__ explicitly in __slots__

class D(object):
    __slots__ = ['a', 'b', '__dict__']                          # Name __dict__ to include one too
    c = 3                                                       # class attrs work normally
    def __init__(self):
        self.d = 4                                              # d stored in __dict__
    
X = D()
print(X.d)                                                      # 4
print(X.c)                                                      # 3
# print(X.a)                                                    # AttributeError: a - All instance attrs undefined until assigned

X.a = 5
print(X.a)                                                      # 5

# Because slot names become class-level attributes, instances acquire
# the union of all slot names anywhere in the tree, by the normal inheritance rule

class E:
    __slots__ = ['c', 'd']                                      # Superclass has slots

class D(E):
    __slots__ = ['a', '__dict__']                               # But so does its subclass

X = D()
X.a = 1; X.b = 2; X.c = 3                                       # The instance is the union (slots: a, c)
print(X.a, X.c)                                                 # (1, 3)


print("-" * 20 + "#2 Slot usage rules" + "-" * 20)


# SLOT USAGE RULES

# 1. Slots in subs are pointless when absent in supers: If a subclass inherits from
#    a superclass without a __slots__, the instance __dict__ attribute created for the 
#    superclass will always be accessible, making a __slots__ in the subclass largely 
#    pointless.

# 2. Slots in supers are pointless when absent in subs: Similarly, because the meaning
#    of a __slots__ declaration is limited to the class in which it appears, subclasses 
#    will produce an instance __dict__ if they do not define a __slots__, rendering a
#    __slots__ in a superclass largely pointless.

# 3. Redefinition renders super slots pointless: If a class defines the same slot name
#    as a superclass, its redefinition hides the slot in the superclass per normal 
#    inheritance.

# 4. Slots prevent class-level defaults: Because slots are implemented as class-level 
#    descriptors (along with per-instance space), you cannot use class attributes of the
#    same name to provide defaults as you can for normal instance attributes: assigning
#    the same name in the class overwrites the slot descriptor.

# 5. Slots and __dict__: As shown earlier, __slots__ preclude both an instance
#    __dict__ and assigning names not listed, unless __dict__ is listed explicitly too.

class C(object): pass                                           # Bullet 1: slots in sub but not super
class D(C): __slots__ = ['a']                                   # Makes instance dict for nonslots
                                                                # But slot name still managed in class
X = D()
X.a = 1; X.b = 2
print(X.__dict__)                                               # {'b': 2}
print(D.__dict__.keys())                                        # ['a', '__module__', '__slots__', '__doc__']


class C(object): __slots__ = ['a']                              # Bullet 2: slots in super but not sub
class D(C): pass                                                # Names instance dict for nonslots
                                                                # But slot name still managed in class
X = D()
X.a = 1; X.b = 2
print(X.__dict__)                                               # {'b': 2}
print(C.__dict__.keys())                                        # ['a', '__module__', '__slots__', '__doc__']

# PROBLEM:
# In a book (Lutz p.1017) it's said that __slots__ prevent class-leve defaults
# (Bullet 4), but the code works. Need to understand the difference.

class C(object): 
    __slots__ = ['a'] 
    a = 99
    
X = C()

# Slots are not generally recommended, except in pathological cases where
# their space reduction is significant.

print("-" * 20 + "#3 Slot speed" + "-" * 20)

import timeit

base = """

Is = []
for i in range(1000):
    X = C()
    X.a = 1; X.b = 2; X.c = 3; X.d = 4
    t = X.a + X.b + X.c + X.d
    Is.append(C)

"""

with_slots = """

class C(object):
    __slots__ = ['a', 'b', 'c', 'd']
    
""" + base

without_slots = """

class C(object):
    pass

""" + base


print("With slots: ", min(timeit.repeat(with_slots, number=1000, repeat=2)))
# ('With slots: ', 0.8236749172210693)

print("Without slots: ", min(timeit.repeat(without_slots, number=1000, repeat=2)))
# ('Without slots: ', 0.9437649250030518)

