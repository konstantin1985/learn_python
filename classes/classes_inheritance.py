

# Inheritance is best at coding extensions based on direct customization (like our
# Manager specialization of Person). Composition is well suited to scenarios where
# multiple objects are aggregated into a whole and directed by a controller layer class.
# Inheritance passes calls up to reuse, and composition passes down to delegate.

print("-" * 20 + "#1 Attributes of class and instance" + "-" * 20)

# The basic inheritance model that classes produce is very simple
# - all it really involves is searching for attributes in trees of linked objects.

class rec: pass

# Attach attributes to the class
rec.name = "Bob"
rec.age = 40

# Class is just an object with field names attached to it.
# Notice that this works even though there are no instances of the class yet; classes are
# objects in their own right, even without instances.
# In fact, they are just self-contained namespaces; as long as we have a reference 
# to a class, we can set or change its attributes anytime we wish. 
print(rec.name)                                           # Bob

# These instances begin their lives as completely empty namespace objects. Because they
# remember the class from which they were made, though, they will obtain the attributes
# we attached to the class by inheritance

x = rec()
y = rec()
print(x.name, y.name)                                     # ('Bob', 'Bob')

# Crucially, attribute references kick off inheritance searches, but attribute 
# assignments affect only the objects in which the assignments are made.

x.name = "Sue"
print(rec.name, x.name, y.name)                           # ('Bob', 'Sue', 'Bob')

# Here, the class's namespace dictionary shows the name and age attributes we assigned
# to it, x has its own name, and y is still empty.

print(list(rec.__dict__.keys()))                          # ['age', '__module__', '__doc__', 'name']
print(list(x.__dict__.keys()))                            # ['name']
print(list(y.__dict__.keys()))                            # []

# Attribute notation kicks off inheritance search, but indexing looks 
# in the single object only

print(x.name, x.__dict__['name'])                         # ('Sue', 'Sue')
print(x.age)                                              # 40
# print(x.__dict__["age"])                                # KeyError: 'age'

# To facilitate inheritance search on attribute fetches, each instance has a link 
# to its class

print(x.__class__)                                        # __main__.rec
# print(rec.__class__)                                    # AttributeError: class rec has no attribute '__class__'
print(rec.__bases__)                                      # () in 2.X, 'object' in 3.X

# Even methods, normally created by a def nested in a class, can be created completely
# independently of any class object.

def uppername(obj):
    return obj.name.upper()

# Pay attention that method() could be invoked on the instances created before
rec.method = uppername
print(x.method())                                         # SUE
print(y.method())                                         # BOB
print(rec.method(x))                                      # SUE

# Instance attributes are created by assigning attributes to an instance object. They
# are normally created within a class's method functions coded inside the class
# statement, by assigning attributes to the self argument (which is always the 
# implied instance). Again, though, they may be created by assignment anywhere a
# reference to the instance appears, even outside the class statement. Normally, all
# instance attributes are initialized in the __init__ constructor method; that way,
# later method calls can assume the attributes already exist.

# self is the name commonly given to the first (leftmost) argument in a class's
# method function; Python automatically fills it in with the instance object that is
# the implied subject of the method call. This argument need not be called self
# (though this is a very strong convention); its position is what is significant.

# Operator overloading is useful to implement objects that resemble built-in types.

print("-" * 20 + "#2 Augmenting methods" + "-" * 20)

class Person:
    
    def __init__(self, sal):
        self.sal = sal
    
    def GiveRaise(self, percent):
        self.sal *= (1 + percent)

class Manager(Person):
    
    def GiveRaise(self, percent, bonus = 0.10):
        Person.GiveRaise(self, percent + bonus)    # Better to invoke parent method than to copy/paste
    
m = Manager(10000)
m.GiveRaise(0.10)
print(m.sal)                                       # 12000.0

print("-" * 20 + "#3 Inherit, Customize, and Extend" + "-" * 20)

class Person:
    def lastName(self): pass
    def giveRaise(self): pass
    def __repr__(self): return 'p'

class Manager(Person):                             # Inherit
    def giveRaise(self, a): pass                   # Customize
    def someThingElse(self, b): pass               # Extend

tom = Manager()
tom.lastName()                                     # Inherited verbatim
tom.giveRaise(1)                                   # Customized version
tom.someThingElse(2)                               # Extension here
print(tom)                                         # Inherited overload method

print("-" * 20 + "#4 Inheritance and constructors" + "-" * 20)

# Calling superclass constructors from redefinitions this way turns out to be a very common 
# coding pattern in Python. By itself, Python uses inheritance to look for and call
# only one __init__ method at construction time-the lowest one in the class tree. If you
# need higher __init__ methods to be run at construction time (and you usually do), you
# must call them manually, and usually through the superclass's name. The upside to
# this is that you can be explicit about which argument to pass up to the superclass's
# constructor and can choose to not call it at all: not calling the superclass constructor
# allows you to replace its logic altogether, rather than augmenting it.

class Person:
    def __init__(self, a):
        self.a = a + 10
        
class Manager(Person):
    def __init__(self, a, b):
        self.b = b
        Person.__init__(self, a)
        
m = Manager(10, 100)
print(m.a, m.b)                                    # (20, 100)

print("-" * 20 + "#5 Composition getattr() instead of inheritance" + "-" * 20)

# getattr()
# If the string is the name of one of the object's attributes, the result is the value of that attribute. 
# For example, getattr(x, 'foobar') is equivalent to x.foobar.

class Person:
    
    def __init__(self, sal):
        self.sal = sal
    
    def GiveRaise(self, percent):
        self.sal *= (1 + percent)
    
    def DoSomething(self):
        print("Do something now!")

    def __repr__(self):
        return "Person %d" % self.sal              # IMPORTANT: __repr__ RETURN string, it doesn't print anything

class Manager:
    
    def __init__(self, sal):                       # Embed a Person object
        self.person = Person(sal)
    
    def GiveRaise(self, percent, bonus = 0.10):    # Intercept and delegate
        self.person.GiveRaise(percent + bonus)
        
    def __getattr__(self, attr):                   # Delegate all other attributes
        return getattr(self.person, attr)          

    def __repr__(self):                            # IMPORTANT: Must overload again (in 3.X)
        return str(self.person)


m = Manager(1000)
m.GiveRaise(0.10) 
print(m.sal)                                       # 1200.0
print(m.DoSomething)                               # <bound method Person.DoSomething of <__main__.Person instance at 0xb732f3ec>>
m.DoSomething()                                    # Do something now!
print(m)                                           # Person 1200

# IMPORTANT p.839 Built-in attributes in Python 2.x vs Python 3.x

# Python 3.x: will not be able to intercept and delegate operator
# overloading method attributes like __repr__ without redefining them itself


print("-" * 20 + "#6 Class and instance attributes" + "-" * 20)

# The built-in instance.__class__ attribute provides a link from an instance to the
# class from which it was created. Classes in turn have a __name__, just like modules,
# and a __bases__ sequence that provides access to superclasses. We can use these
# here to print the name of the class from which an instance is made

bob = Person(1000)
print(bob)                                         # Person 1000
print(bob.__class__)                               # __main__.Person
print(bob.__class__.__name__)                      # Person
print(bob.__dict__.keys())                         # ['sal'] - the only attribute of instance (self.sal)
print(Person.__dict__.keys())                      # ['__module__', 'GiveRaise', 'DoSomething', '__repr__', '__doc__', '__init__']
print(dir(bob))                                    # + inherited attributes ['DoSomething', 'GiveRaise', '__doc__', '__init__', '__module__', '__repr__', 'sal']
for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])            # ('sal', '=>', 1000)
for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))            # ('sal', '=>', 1000)

l = (n for n in dir(bob) if not n.startswith('__'))
print(list(l))                                     # ['DoSomething', 'GiveRaise', 'sal']
    
man = Manager(2000)
print(man)                                         # Person 2000
print(man.__class__)                               # __main__.Manager
print(man.__class__.__name__)                      # Manager
print(man.__dict__.keys())                         # ['person']
print(Manager.__dict__.keys())                     # ['__module__', 'GiveRaise', '__getattr__', '__repr__', '__doc__', '__init__']
print(dir(man))                                    # + inherited attributes ['GiveRaise', '__doc__', '__getattr__', '__init__', '__module__', '__repr__', 'person']
for key in man.__dict__:
    print(key, '=>', man.__dict__[key])            # ('person', '=>', Person 2000)
for key in man.__dict__:
    print(key, '=>', getattr(man, key))            # ('person', '=>', Person 2000)

l = (n for n in dir(man) if not n.startswith('__'))
print(list(l))                                     # ['GiveRaise', 'person']

# To minimize the chances of name collisions like this, Python programmers often prefix
# methods not meant for external use with a single underscore: _gatherAttrs in our case.
# This isn't foolproof (what if another class defines _gatherAttrs, too?), but it's usually
# sufficient, and it's a common Python naming convention for methods internal to a class.

# A better and less commonly used solution would be to use two underscores at the front
# of the method name only: __gatherAttrs for us. Python automatically expands such
# names to include the enclosing class's name, which makes them truly unique when
# looked up by the inheritance search. This is a feature usually called pseudoprivate class
# attributes


