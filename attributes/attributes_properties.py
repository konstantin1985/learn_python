


# MAIN SOURCE:
# Lutz, "Learning Python" 5e Chapter 38

# USEFUL LINKS: 
#
# 1) Inheritance and __init__
#    https://stackoverflow.com/questions/5166473/inheritance-and-init-method-in-python
#
# 2) Good example of property usage
#    https://www.programiz.com/python-programming/property

# GENERAL INFORMATION:

print("-" * 20 + "# 1 Why Manage Attributes?" + "-" * 20)

# Normally, attributes are simply names for objects; a person's name attribute, 
# for example, might be a simple string, fetched and set with basic attribute
# syntax:
# person.name           # Fetch attribute value
# person.name = value   # Change attribute value
# In most cases, the attribute lives in the object itself, or is inherited from
# a class from which it derives. That basic model suffices for most programs you
# will write in your Python career.

# Sometimes, though, more flexibility is required. Suppose you've written a
# program to use a name attribute directly, but then your requirements change
# - for example, you decide that names should be validated with logic when set
# or mutated in some way when fetched. It's straightforward to code methods to
# manage access to the attribute's value

# class Person:
#     def getName(self)
#     def setName(self, value)
#
# person = Person()
# person.getName()
# person.setName('value')

# However, this also requires changing all the places where names are used in
# the entire program - a possibly nontrivial task. Moreover, this approach 
# requires the program to be aware of how values are exported: as simple names
# or called methods.
  
# A better solution would allow you to run code automatically on attribute access,
# if needed. That's one of the main roles of managed attributes-they provide ways
# to add attribute accessor logic after the fact.


# Four accessor techniques
#
# - The __getattr__ and __setattr__ methods, for routing undefined attribute
#   fetches and all attribute assignments to generic handler methods.
#
# - The __getattribute__ method, for routing all attribute fetches to a generic
#   handler method.
#
# - The property built-in, for routing specific attribute access to get and set
#   handler functions.
#
# - The descriptor protocol, for routing specific attribute accesses to instances
#   of classes with arbitrary get and set handler methods, and the basis for other
#   tools such as properties and slots.

# The tools in the first of these bullets are available in all Pythons. The last
# three bullets' tools are available in Python 3.X and new-style classes in 2.X.

print("-" * 20 + "# 2 Properties: Basic" + "-" * 20)

# The property protocol allows us to route a specific attribute's get, set, and
# delete operations to functions or methods we provide, enabling us to insert
# code to be run automatically on attribute access, intercept attribute 
# deletions, and provide documentation for the attributes if desired.

# Properties are created with the property built-in and are assigned to class
# attributes, just like method functions. Accordingly, they are inherited by
# subclasses and instances, like any other class attributes. Their access-
# interception functions are provided with the self instance argument, which
# grants access to state information and class attributes available on the
# subject instance.

# A property is created by assigning the result of a built-in function to a class attribute:
#
# attribute = property(fget, fset, fdel, doc)

# None of this built-in's arguments are required, and all default to None if
# not passed. For the first three, this None means that the corresponding
# operation is not supported, and attempting it will raise an AttributeError
# exception automatically.

# When these arguments are used, we pass fget a function for intercepting
# attribute fetches, fset a function for assignments, and fdel a function
# for attribute deletions. Technically, all three of these arguments accept
# any callable, including a class's method, having a first argument to receive
# the instance being qualified. When later invoked,fget function returns the
# computed attribute value, fset and fdel return nothing (really, None), and
# all three may raise exceptions to reject access requests.

# The doc argument receives a documentation string for the attribute, if
# desired; otherwise, the property copies the docstring of the fget function,
# which as usual defaultsNone.

# This built-in property call returns a property object, which we assign to
# the name of the attribute to be managed in the class scope, where it will
# be inherited by every instance.

class Person(object):
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, 'name property docs')

bob = Person('Bob Smith')                                        # bob has a managed attribute
print(bob.name)                                                  # Runs getName()
bob.name = 'Robert Smith'                                        # Runs setName()
print(bob.name)
del bob.name                                                     # Runs delName()

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)                                       # Or help(Person.name)

# OUTPUT:
# fetch...
# Bob Smith
# change...
# fetch...
# Robert Smith
# remove...
# --------------------
# fetch...
# Sue Jones
# name property docs

# Like all class attributes, properties are inherited by both instances
# and lower subclasses.

class Child(Person):
    pass

print('-' * 20)
mary = Child("Mary Smith")
print(mary.name)
# OUTPUT:
# fetch...
# Mary Smith    

# Child is extending the class Person and since you are not redefining the special
# method named __init__() in Child, it gets inherited from Num (tree!).

print("-" * 20 + "# 3 Computed Attributes" + "-" * 20)

# The example in the prior section simply traces attribute accesses. Usually, 
# though, properties do much more-computing the value of an attribute dynamically
# when fetched, for example. 

class PropSquare(object):
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2                                   # On attr fetch
    def setX(self, value):
        self.value = value
    X = property(getX, setX)
    
P = PropSquare(3)                                                # Two instances of class with property  
Q = PropSquare(32)                                               # Each has different state information

print(P.X)                                                       # 3 ** 2
P.X = 4
print(P.X)                                                       # 4 ** 2
print(Q.X)                                                       # 32 ** 2 (1024)

# This class defines an attribute X that is accessed as though it were static data,
# but really runs code to compute its value when fetched.

# Notice that we've made two different instances-because property methods automat-
# ically receive a self argument, they have access to the state information stored 
# in instances. In our case, this means the fetch computes the square of the subject
# instance's own data.

print("-" * 20 + "# 4 Coding Properties with Decorators" + "-" * 20)

# Recall that the function decorator syntax:
#
# @decorator
# def func(args): ...

# is automatically translated to this equivalent by Python, to rebind the function
# name to the result of the decorator callable:
# 
# def func(args): ...
# func = decorator(func)

class Person2(object):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):                                              # name = property(name)                 
        "name property docs"
        print('fetch...')
        return self._name
    
    @name.setter
    def name(self, value):                                       # name = name.setter(name)
        print('change...')
        self._name = value
    
    @name.deleter
    def name(self):                                              # name = name.deleter(name)  
        print('remove...')
        del self._name

bob = Person2('Bob Smith')                                       # bob has a managed attribute
print(bob.name)                                                  # Runs name getter (name 1)
bob.name = 'Robert Smith'                                        # Runs name setter (name 2)
print(bob.name)
del bob.name                                                     # Runs name deleter (name 3)

print('-' * 20)
sue = Person2('Sue Jones')                                       # sue has property too
print(sue.name)
print(Person2.name.__doc__)

# OUTPUT:
# fetch...
# Bob Smith
# change...
# fetch...
# Robert Snith
# remove...
# --------------------
# fetch...
# Sue Jones
# name property docs

# In fact, this code is equivalent to the first example in this section-decoration
# is just an alternative way to code properties in this case. As is so often the 
# case with alternative tools, though, the choice between the two techniques is
# largely subjective.




