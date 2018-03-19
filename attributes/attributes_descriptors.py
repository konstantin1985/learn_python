


# MAIN SOURCE:
# Lutz, "Learning Python" 5e Chapter 38

# USEFUL LINKS: 
#


# GENERAL INFORMATION:

# Descriptors provide an alternative way to intercept attribute access;
# they are strongly related to the properties discussed in the prior
# section. Really, a property is a kind of descriptor-technically speaking,
# the property built-in is just a simplified way to create a specific type
# of descriptor that runs method functions on attribute accesses. In fact,
# descriptors are the underlying implementation mechanism for a variety of
# class tools, including both properties and slots.

# Functionally speaking, the descriptor protocol allows us to route a
# specific attribute's get, set, and delete operations to methods of a
# separate class's instance object that we provide. This allows us to
# insert code to be run automatically on attribute fetches and assignments,
# intercept attribute deletions, and provide documentation for the 
# attributes if desired.

# Descriptors are created as independent classes, and they are assigned
# to class attributes just like method functions. Like any other class
# attribute, they are inherited by subclasses and instances. Their
# access-interception methods are provided with both a self for the
# descriptor instance itself, as well as the instance of the client class
# whose attribute references the descriptor object. Because of this, they
# can retain and use state information of their own, as well as state
# information of the subject instance. For example, a descriptor may call
# methods available in the client class, as well as descriptor-specific
# methods it defines.

# Like a property, a descriptor manages a single, specific attribute;
# although it can't catch all attribute accesses generically, it provides
# control over both fetch and assignment accesses and allows us to change
# an attribute name freely from simple data to a computation without
# breaking existing code. Properties really are just a convenient way to
# create a specific kind of descriptor, and as we shall see, they can be
# coded as descriptors directly.

# Unlike properties, descriptors are broader in scope, and provide a more
# general tool. For instance, because they are coded as normal classes,
# descriptors have their own state, may participate in descriptor inheritance
# hierarchies, can use composition to aggregate objects, and provide a
# natural structure for coding internal methods and attribute documentation
# strings.

print("-" * 20 + "# 1 Descriptors: the basics" + "-" * 20)

# Descriptors are coded as separate classes and provide specially named
# accessor methods for the attribute access operations they wish to intercept
# -get, set, and deletion methods in the descriptor class are automatically
# run when the attribute assigned to the descriptor class instance is accessed
# in the corresponding way.

# class Descriptor:
#     "docstring goes here"
#     def __get__(self, instance, owner): ...                      # Return attr value
#     def __set__(self, instance, value): ...                      # Return nothing (None)
#     def __del__(self, instance): ...                             # Return nothing (None)

# Classes with any of these methods are considered descriptors, and their
# methods are special when one of their instances is assigned to another
# class's attribute-when the attribute is accessed, they are automatically
# invoked. If any of these methods are absent, it generally means that the
# corresponding type of access is not supported. Unlike properties, however,
# omitting a __set__ allows the descriptor attribute's name to be assigned
# and thus redefined in an instance, thereby hiding the descriptor-to make
# an attribute read-only, you must define __set__ to catch assignments and
# raise an exception.

# A descriptor with a __set__ is known formally as data descriptor, and is
# given precedence over other names located by normal inheritance rules.
# The inherited descriptor for name __class__, for example, overrides the
# same name in an instance's namespace dictionary. This also works to ensure
# that data descriptors you code in your own classes take precedence over
# others.

print("-" * 20 + "# 2 Descriptor method arguments" + "-" * 20)

# All three descriptor methods are passed both the descriptor class instance
# (self), and the instance of the client class to which the descriptor instance
# is attached (instance).

# The __get__ access method additionally receives an owner argument, specifying
# the class to which the descriptor instance is attached. Its instance argument
# is either the instance through which the attribute was accessed (for 
# instance.attr), or None when the attribute is accessed through the owner class
# directly (for class.attr). The former of these generally computes a value for
# instance access, and the latter usually returns self if descriptor object
# access is supported.

# When X.attr is fetched, Python automatically runs the __get__ method of the
# Descriptor class instance to which the Subject.attr class attribute is assigned.

class Descriptor(object):
    
    def __get__(self, instance, owner):
        print(self, instance, owner)
        
class Subject(object):
    attr = Descriptor()

X = Subject()
X.attr
# (<__main__.Descriptor object at 0xb739d7ec>, 
#  <__main__.Subject instance at 0xb739d80c>,
#  <class '__main__.Subject'>)

Subject.attr
# (<__main__.Descriptor object at 0xb72f67ec>, 
#  None, 
#  <class '__main__.Subject'>)

# When X.attr is fetched, it's as though the following translation occurs
# X.attr -> Descriptor.__get__(Subject.attr, X, Subject)

# The descriptor knows it is being accessed directly when its instance argument
# is None.

print("-" * 20 + "# 3 Read-only descriptors" + "-" * 20)

# Unlike properties, simply omitting the __set__ method in a descriptor
# isn't enough to make an attribute read-only, because the descriptor name
# can be assigned to an instance. In the following, the attribute assignment
# to X.a stores a in the instance object X, thereby hiding the descriptor
# stored in class C.

class D(object):
    def __get__(*args): print('get')

class C:
    a = D()                                                        # Attribute a is a descriptor instance    

X = C()
X.a                                                                # Runs inherited descriptor __get__
# get 
C.a
# get

X.a = 99                                                           # Stored on X, hiding C.a! 
print(X.a)
# 99

print(list(X.__dict__.keys()))
# ['a']

# This is the way all instance attribute assignments work in Python, and
# it allows classes to selectively override class-level defaults in their
# instances. To make a descriptor-based attribute read-only, catch the
# assignment in the descriptor class and raise an exception to prevent
# attribute assignment-when assigning an attribute that is a descriptor,
# Python effectively bypasses the normal instance-level assignment behavior
# and routes the operation to the descriptor object.

class D(object):
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')
    
class C(object):
    a = D()

X = C()
X.a
# get
# X.a = 99                                                         # AttributeError: cannot set

# Also be careful not to confuse the descriptor __delete__ method with
# the general __del__ method. 

print("-" * 20 + "# 4 First example" + "-" * 20)

# The following defines a descriptor that intercepts access to an attribute
# named name in its clients. Its methods use their instance argument to
# access state information in the subject instance, where the name string is
# actually stored. 

# IMPORTANT:
# Like properties, descriptors work properly only for 
# new-style classes, so be sure to derive both classes in the following from
# object if you're using 2.X-it's not enough to derive just the descriptor,
# or just its client.

class Name(object):
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person(object):
    def __init__(self, name):
        self._name = name
    name = Name()                                                  # Assign descriptor to attr

bob = Person('Bob Smith')
print(bob.name)
# fetch...
# Bob Smith
bob.name = 'Robert Smith'
# change...
print(bob.name)
# fetch...
# Robert Smith
del bob.name
# remove...

print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
# fetch...
# Sue Jones
print(Name.__doc__)

# Notice in this code how we assign an instance of our descriptor class to a
# class attribute in the client class; because of this, it is inherited by all
# instances of the class, just like a class's methods. When the descriptor's
# __get__ method is run, it is passed three objects to define its context:
# - self is the Name class instance.
# - instance is the Person class instance.
# - owner is the Person class.

# Our descriptor class instance is a class attribute and thus is inherited
# by all instances of the client class and any subclasses.

# Also note that when a descriptor class is not useful outside the client
# class, it's perfectly reasonable to embed the descriptor's definition
# inside its client syntactically. When coded this way, Name becomes a 
# local variable in the scope of the Person class statement, such that it
# won't clash with any names outside the class.

class Person2(object):
    def __init__(self, name):
        self._name = name
        
    class Name(object):
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name    
    
    name = Name() 

print("-" * 20 + "# 4 Computed attributes" + "-" * 20)

# In practice, descriptors can also be used to compute attribute values each
# time they are fetch.

class DescSquare(object):
    
    def __init__(self, start):                                     # Each desc has own state       
        self.value = start
    
    def __get__(self, instance, owner):                            # On attr fetch
        return self.value ** 2
    
    def __set__(self, instance, value):                            # On attr assign
        self.value = value                                         # No delete or docs
      
        
class Client1(object):
    X = DescSquare(3)                                              # Assign descriptor instance to class attr 
    
class Client2(object):
    X = DescSquare(32)                                             # Another instance in another client class. Could also code two instances in same class

c1 = Client1()
c2 = Client2()

print(c1.X)                                                        #  3 ** 2
c1.X = 4
print(c1.X)                                                        #  4 ** 2
print(c2.X)                                                        # 32 ** 2


print("-" * 20 + "# 5 Using State Information in Descriptors" + "-" * 20)

# In the previous examples: 
# - the first (the name attribute example) uses data stored on the client instance
# - the second (the attribute squaring example) uses data attached to the descriptor
#   object itself (a.k.a. self). 

# Descriptors can use both instance state and descriptor state, or any combination:
# - Descriptor state is used to manage either data internal to the workings of the
#   descriptor, or data that spans all instances. It can vary per attribute appearance
#   (often, per client class).
# - Instance state records information related to and possibly created by the client
#   class. It can vary per client class instance (that is, per application object).

# In other words, descriptor state is per-descriptor data and instance state is per-
# client-instance data. As usual in OOP, you must choose state carefully. For instance, 
# you would not normally use descriptor state to record employee names, since each client
# instance requires its own value-if stored in the descriptor, each client class instance
# will effectively share the same single copy. On the other hand, you would not usually
# use instance state to record data pertaining to descriptor implementation internals-if
# stored in each instance, there would be multiple varying copies.

# This code's internal value information lives only in the descriptor, so there won't
# be a collision if the same name is used in the client's instance. Notice that only
# the descriptor attribute is managed here-get and set accesses to X are intercepted,
# but accesses to Y and Z are not (Y is attached to the client class and Z to the
# instance). When this code is run,  is computed when fetched, but its value is also
# the same for all client instances.

class DescState(object):
    
    def __init__(self, value):
        self.value = value                                         # Descriptor state          

    def __get__(self, instance, owner):
        print("DescState get...")
        return self.value * 10
    
    def __set__(self, instance, value):
        print("DescState set...")
        self.value = value
     
# Client class   
class CalcAttrs(object):
    X = DescState(2)                                               # Descriptor class attribute
    Y = 3                                                          # Class attribute
    def __init__(self):
        self.Z = 4                                                 # Instance attribute

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                                         # X is computed, others are not
# DescState get...
# (20, 3, 4)

obj.X = 5                                                          # X assignment is intercepted  
CalcAttrs.Y = 6                                                    # Y reassigned in class
obj.Z = 7                                                          # Z assigned in instance
print(obj.X, obj.Y, obj.Z)
# DescState set...
# DescState get...
# (50, 6, 7)

obj2 = CalcAttrs()
print(obj2.X, obj2.Y, obj2.Z)                                      # IMPORTANT:
# (50, 6, 4)                                                       # But X uses shared data, like Y!


# It's also feasible for a descriptor to store or use an attribute attached to the
# client class's instance, instead of itself. Crucially, unlike data stored in the
# descriptor itself, this allows for data that can vary per client class instance.

class InstState(object):
    def __get__(self, instance, owner):
        print("InstState...")
        return instance._X * 10
    def __set__(self, instance, value):
        print("InstState...")
        instance._X = value
        
class CalcAttrs2(object):
    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z = 4
        
obj3 = CalcAttrs2()
print(obj3.X, obj3.Y, obj3.Z) 
# InstState...
# (20, 3, 4)
    
obj3.X = 5                                                         # X assignment is intercepted
CalcAttrs2.Y = 6                                                   # Y reassigned in class
obj3.Z = 7                                                         # Z assigned in instance
print(obj3.X, obj3.Y, obj3.Z)
# InstState...
# InstState...
# (50, 6, 7)

obj4 = CalcAttrs2()
print(obj4.X, obj4.Y, obj4.Z)                                      # But X differs now, like Z!
# InstState...
# (20, 6, 4)

# Here, X is assigned to a descriptor as before that manages accesses. The new
# descriptor here, though, has no information itself, but it uses an attribute
# assumed to exist in the instance-that attribute is named _X, to avoid collisions
# with the name of the descriptor itself.

# Both descriptor and instance state have roles. In fact, this is a general
# advantage that descriptors have over properties-because they have state of
# their own, they can easily retain data internally, without adding it to the
# namespace of the client instance object.

# "Virtual" attributes like properties and descriptors with tools like dir and
# getattr, even though they don't exist in the instance's namespace dictionary.

print(obj4.__dict__)
# {'Z': 4, '_X': 2}

print([x for x in dir(obj4) if not x.startswith('__')])
# ['X', 'Y', 'Z', '_X']

print(getattr(obj4, 'X'))
# InstState...
# 20

# The more generic __getattr__ and __getattribute__ tools we'll meet later are
# not designed to support this functionality-because they have no class-level
# attributes, their "virtual" attribute names do not appear in dir results.

print("-" * 20 + "# 6 How Properties and Descriptors Relate" + "-" * 20)

# As mentioned earlier, properties and descriptors are strongly related-the
# property built-in is just a convenient way to create a descriptor. Now that
# you know how both work, you should also be able to see that it's possible
# to simulate the property built-in with a descriptor class.

# This Property class catches attribute accesses with the descriptor protocol
# and routes requests to functions or methods passed in and saved in descriptor
# state when the class is created.

class Property:
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel                                           # Save unbounded methods       
        self.__doc__ = doc                                         # or other callables

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
        
    def __del__(self, instance):
        
    

# To use @ decorator syntax to also specify set and delete operations, we'd
# have to extend our Property class with setter and deleter methods, which
# would save the decorated accessor function and return the property object
# (self should suffice).



