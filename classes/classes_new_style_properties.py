
# MAIN SOURCE:
# Lutz

# USEFUL LINKS
# http://jfine-python-class.readthedocs.org/en/latest/property_from_class.html#about-properties
# http://stackoverflow.com/questions/15458613/python-why-is-read-only-property-writable
# https://www.python-course.eu/python3_properties.php

# GENERAL DESCRIPTION

# Properties - a mechanism that provides another way for new-style classes 
# to define methods called automatically for access or assignment to instance 
# attributes. 

# This feature is similar to properties (a.k.a. "getters" and "setters")
# in languages like Java and C#, but in Python is generally best used sparingly,
# as a way to add accessors to attributes after the fact as needs evolve and warrant. 
# Where needed, though, properties allow attribute values to be computed dynamically
# without requiring method calls at the point of access.

# Though properties cannot support generic attribute routing goals, at least
# for specific attributes they are an alternative to some traditional uses
# of the __getattr__ and __setattr__ overloading methods.

# setattr(x, 'foobar', 123) is equivalent to x.foobar = 123
# getattr(x, 'foobar') is equivalent to x.foobar - The string may name an
# existing attribute or a new attribute.

# Properties and slots are related too, but serve different goals. Both
# implement instance attributes that are not physically stored in instance 
# namespace dictionaries - a sort of "virtual" attribute-and both are 
# based on the notion of class-level attribute descriptors. In contrast, 
# slots manage instance storage, while properties intercept access and
# compute values arbitrarily.

print("-" * 20 + "# 1 Property basics" + "-" * 20)

# You generate a property by calling the property built-in function,
# passing in up to three accessor methods-handlers for get, set, and
# delete operations - as well as an optional docstring for the property.

# The resulting property object is typically assigned to a name at the 
# top level of a class statement (e.g., name=property()).

# Later accesses to the class property name itself as an object attribute
# (e.g., obj.name) are automatically routed to one of the accessor methods
# passed into the property call.

# Example with __getattr__

class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = operators()
print(x.age)                                                       # 40 - runs __getattr__, because age attribute doesn't exist
# print(x.name)                                                    # AttributeError: name

# Same example with a property (new-style objects)

class properties(object):
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)                     # (get, set, del, docs) or use @

x = properties()
print(x.age)                                                       # Runs getage
x.age = 42                                                         # Runs setage
print(x._age)
# print(x.name)                                                    # AttributeError: 'properties' object has no attribute 'name' - normal fetch

x.job = 'trainer'                                                  # Normal assign: no setage call
print(x.job)                                                       # Normal fetch: no getage call

# A generic __getattr__ or a __setattr__ attribute handler with a passed-
# in attribute name is usually preferable when the set of attributes to be
# supported cannot be determined when the class is coded.

print("-" * 20 + "# 2 Property as a decorator" + "-" * 20)

class First(object):

    def __init__(self):
        self.width = 10;
        self.length = 5;

    @property
    def attrib(self):
        return self.width * self.length
    
f = First()
print(f.attrib)
# f.attrib = 5                                                     # There is no setter   
 
class Second(object):

    def __init__(self):
        self.value = 10

    @property
    def attrib(self):
        print('getter')
        return self.value

    @attrib.setter
    def attrib(self, value):
        print('setter')
        self.value = value

s = Second()
print(s.attrib)                                                    # getter 10         
s.attrib = 20                                                      # setter
print(s.attrib)                                                    # getter 20


print("-" * 20 + "# 3 __getattribute__ and Descriptors: Attribute Tools" + "-" * 20)

# The __getattribute__ operator (may create loops) overloading method, 
# available for new-style classes only, allows a class to intercept all 
# attribute references, not just undefined references.






