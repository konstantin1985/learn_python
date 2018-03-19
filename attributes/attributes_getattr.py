


# MAIN SOURCE:
# Lutz, "Learning Python" 5e Chapter 38

# USEFUL LINKS: 
#


# GENERAL INFORMATION:

# __getattr__ is run for undefined attributes-because it is run only
# for attributes not stored on an instance or inherited from one of
# its classes, its use is straightforward.

# __getattribute__ is run for every attribute-because it is all-inclusive,
# you must be cautious when using this method to avoid recursive loops
# by passing attribute accesses to a superclass.

# The __getattr__ and __getattribute__ methods are also more generic than
# properties and descriptors-they can be used to intercept access to any
# (or even all) instance attribute fetches, not just a single specific name.

# These two methods are more narrowly focused than the alternatives we
# considered earlier: they intercept attribute fetches only, not assignments.
# To also catch attribute changes by assignment, we must code a __setattr__
# method, which must take care to avoid recursive loops by routing attribute
# assignments through the instance namespace dictionary or a superclass method.



print("-" * 20 + "# 1 The Basics" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 2 Avoiding loops in attribute interception methods" + "-" * 20)

# NEED TO LEARN

# The potential for looping (a.k.a. recursing). Because __getattr__ is
# called for undefined attributes only, it can freely fetch other attributes
# within its own code. However, because __getattribute__ and __setattr__ are
# run for all attributes, their code needs to be careful when accessing other
# attributes to avoid calling themselves again and triggering a recursive loop.

print("-" * 20 + "# 3 A First Example" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 4 Computed Attributes" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 5 __getattr__ and __getattribute__ Compared" + "-" * 20)

# To summarize the coding differences between __getattr__ and __getattribute__,
# the following example uses both to implement three attributes-attr1 is a
# class attribute, attr2 is an instance attribute, and attr3 is a virtual
# managed attribute computed when fetched.

print("-" * 20 + "# 6 Intercepting Built-in Operation Attributes" + "-" * 20)

class GetAttr:
    
    attr1 = 1
    
    def __init__(self):
        self.attr2 = 2 
    
    def __getattr__(self, attr):                                # On undefined attrs only 
        print('get: ' + attr)                                   # Not on attr1: inherited from class
        if attr == 'attr3':                                     # Not on attr2: stored on instance
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
# 1
print(X.attr2)
# 2
print(X.attr3)
# get: attr3
#3
print('-'*20)      

class GetAttribute(object):
    
    attr1 = 1
    
    def __init__(self):
        self.attr2 = 2
    
    def __getattribute__(self, attr):                           # On all attr fetches
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)          # Use superclass to avoid looping here

X = GetAttribute()
print(X.attr1)
# get: attr1
# 1
print(X.attr2)
# get: attr2
# 2
print(X.attr3)
# get: attr2
# 3











