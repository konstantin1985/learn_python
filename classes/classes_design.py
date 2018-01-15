

print("-" * 20 + "#0 Overview" + "-" * 20)

# - Inheritance
#   Inheritance is based on attribute lookup in Python (in X.name expressions).
# - Polymorphism
#   In X.method, the meaning of method depends on the type (class) of subject object X.
# - Encapsulation
#   Methods and operators implement behavior, though data hiding is a convention by default.
#   Encapsulation is available and useful in Python nonetheless: it allows the implementation 
#   of an object's interface to be changed without impacting the users of that object.

print("-" * 20 + "#1 Polymorphism Means Interfaces, Not Call Signatures" + "-" * 20)

# Some OOP languages also define polymorphism to mean overloading functions based
# on the type signatures of their arguments-the number passed and/or their types. 
# Because there are no type declarations in Python, this concept doesn't really apply; as
# we've seen, polymorphism in Python is based on object interfaces, not types.

# CASE #1

# If you're pining for your C++ days, you can try to overload methods by their argument
# lists, like this:
# class C:
#     def meth(self, x):
#         ...
#     def meth(self, x, y, z):
#     ...
# This code will run, but because the def simply assigns an object to a name in the class's
# scope, the last definition of the method function is the only one that will be retained

# CASE #2

# If they are truly required, you can always code type-based selections using the type-
# testing ideas we met in Chapter 4 and Chapter 9, or the argument list tools introduced
# in Chapter 18:
# class C:
#     def meth(self, *args):
#         if len(args) == 1:                                       # Branch on number arguments
#             ...
#         elif type(arg[0]) == int:                                # Branch on argument types (or isinstance())
#             ...

# CASE #3

# You normally shouldn't do this, though-it's not the Python way. As described in
# Chapter 16, you should write your code to expect only an object interface, not a specific
# data type. That way, it will be useful for a broader category of types and applications,
# both now and in the future:
# class C:
#     def meth(self, x):
#         x.operation()                                            # Assume x does the right thing
# It's also generally considered better to use distinct method names for distinct 
# operations, rather than relying on call signatures (no matter what language you code in).

print("-" * 20 + "#2 OOP and Inheritance: 'Is-a' Relationships" + "-" * 20)

# From a programmer's point of view, inheritance is kicked off by attribute qualifications, which
# trigger searches for names in instances, their classes, and then any superclasses. From
# a designer's point of view, inheritance is a way to specify set membership: a class defines
# a set of properties that may be inherited and customized by more specific sets (i.e.,
# subclasses).

# In OOP terms, we call these relationships 'is-a' links: a robot is a chef, which is an employee.

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def GiveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def Work(self):
        print(self.name, " does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
    
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def Work(self):
        print(self.name, " makes food")
        
class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def Work(self):
        print(self.name, " interfaces with customer")
        
class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def Work(self):
        print(self.name, " makes pizza")

bob = PizzaRobot('bob')                                            # Make a robot named bob
print(bob)                                                         # <Employee: name=bob, salary=50000>    Run inherited __repr__
bob.Work()                                                         # ('bob', ' makes pizza')               Run type-specific action
bob.GiveRaise(0.20)                                                # Give bob a 20% raise
print(bob)                                                         # <Employee: name=bob, salary=60000.0>

# Creates instances of all four classes; each responds differently when asked
# to work because the work method is different in each

for klass in Employee, Chef, Server, PizzaRobot:
    obj = klass(klass.__name__)
    obj.Work()

# ('Employee', ' does stuff')
# ('Chef', ' makes food')
# ('Server', ' interfaces with customer')
# ('PizzaRobot', ' makes pizza')

print("-" * 20 + "#3 OOP and Composition: 'Has-a' Relationships" + "-" * 20)

# From programmer's point of view, composition involves embedding other objects in a 
# container object, and activating them to implement container methods.

# In this text, a 'composition' simply refers to a collection of embedded
# objects. The composite class generally provides an interface all its own and implements
# it by directing the embedded objects.

# Our pizza shop is a composite object: it has an oven, and it has employees
# like servers and chefs. When a customer enters and places an order, the components
# of the shop spring into action-the server takes the order, the chef makes the pizza,
# and so on.

class Customer:
    def __init__(self, name):
        self.name = name
    def Order(self, server):
        print(self.name, "orders from", server)
    def Pay(self, server):
        print(self.name, "pays for item to")

class Oven:
    def Bake(self):
        print("oven bakes")

class PizzaShop:
    
    def __init__(self):
        self.server = Server('Pat')                                # Embed other objects
        self.chef   = PizzaRobot('Bob')                            # A robot named bob
        self.oven   = Oven()
    
    def Order(self, name):
        customer = Customer(name)
        customer.Order(self.server)
        self.chef.Work()
        self.oven.Bake()
        customer.Pay(self.server)
        
scene = PizzaShop()                                                # Make the composite
scene.Order('Homer')                                               # Simulate Homer's order 
print('-' * 10)
scene.Order('Shaggy')                                              # Simulate Shaggy's order

# ('Homer', 'orders from', <Employee: name=Pat, salary=40000>)
# ('Bob', ' makes pizza')
# oven bakes
# ('Homer', 'pays for item to')
# ----------
# ('Shaggy', 'orders from', <Employee: name=Pat, salary=40000>)
# ('Bob', ' makes pizza')
# oven bakes
# ('Shaggy', 'pays for item to') 

# The PizzaShop class is a container and controller; its constructor makes and embeds
# instances of the employee classes we wrote in the prior section, as well as an Oven class
# defined here. When this module's self-test code calls the PizzaShop order method, the
# embedded objects are asked to carry out their actions in turn. 

# Notice that we make a new Customer object for each order, and we pass on the embedded
# Server object to Customer methods; customers come and go, but the server is part of 
# the pizza shop composite.

# Also notice that employees are still involved in an inheritance relationship;
# composition and inheritance are complementary tools.

# IMPORTANT
# As a rule of thumb, classes can represent just about any objects and relationships
# you can express in a sentence; just replace nouns with classes (e.g., Oven), and verbs
#  with methods (e.g., bake), and you'll have a first cut at a design.

print("-" * 20 + "#4 Stream Processors Revisited" + "-" * 20)

# This class defines a converter method that it expects subclasses to fill in; its an
# example of the abstract superclass model. Coded this way, reader and writer objects
# are embedded within the class instance (composition), and we supply the conversion
# logic in a subclass rather than passing in a converter function (inheritance).

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        
    def Process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.Converter(data)
            self.writer.write(data)
            
    def Converter(self, data):
        assert False, "Converter must be defined"                  # Or raise exception   

class Uppercase(Processor):
    def Converter(self, data):
        return data.upper()
    
import sys
obj = Uppercase(open('classes_files/file1.txt'), sys.stdout)
obj.Process()                                                      # ABC DEF 123
print('\n')

# To process different sorts of streams, pass in different sorts of objects to the 
# class construction call. Here, we use an output file instead of a stream:

prog = Uppercase(open('classes_files/file1.txt'), open('classes_files/file2.txt', 'w'))
prog.Process()

# But, as suggested earlier, we could also pass in arbitrary objects coded as 
# classes that define the required input and output method interfaces.

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())
prog = Uppercase(open('classes_files/file1.txt'), HTMLize())
prog.Process()

# <PRE>ABC</PRE>
# <PRE>DEF</PRE>
# <PRE>123</PRE>

print("-" * 20 + "#5 OOP and Delegation: 'Wrapper' Proxy Objects" + "-" * 20)

# Delegation involves wrapping an object in a proxy class, which adds extra behavior
# and passes other operations to the wrapped object. The proxy retains the interface
# of the wrapped object.

# Composition is a technique whereby a controller class embeds and directs a number
# of objects, and provides an interface all its own; it's a way to build up larger
# structures with classes.

# Beside inheritance and composition, object-oriented programmers often speak of 
# delegation, which usually implies controller objects that embed other objects to which
# they pass off operation requests. The controllers can take care of administrative 
# activities, such as logging or validating accesses, adding extra steps to interface 
# components, or monitoring active instances.

# In a sense, delegation is a special form of composition, with a single embedded object
# managed by a wrapper (sometimes called a proxy) class that retains most or all of the
# embedded object's interface. The notion of proxies sometimes applies to other 
# mechanisms too, such as function calls; in delegation, we're concerned with proxies for
# all of an object's behavior, including method calls and other operations.

# A wrapper class can use __getattr__ to route arbitrary accesses to a wrapped object.

# This code makes use of the getattr built-in function to fetch an attribute from the 
# wrapped object by name string-getattr(X,N) is like X.N, except that N is an expression
# that evaluates to a string at runtime, not a variable. In fact, getattr(X,N) is similar
# to X.__dict__[N], but the former also performs an inheritance search, like X.N, while 
# the latter does not.

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj                                         # Save object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)                                # Trace fetch
        return getattr(self.wrapped, attrname)                     # Delegate fetch

x = Wrapper([1, 2, 3])                                             # Wrap a list
x.append(4)                                                        # Trace: append
print(x.wrapped)                                                   # [1, 2, 3, 4]

x = Wrapper({'a': 1,'b': 2})                                       # Wrap a dictionary
print(x.keys())                                                    # ['a', 'b'] - Delegate to dictionary method

# The net effect is to augment the entire interface of the wrapped object, with additional
# code in the Wrapper class. We can use this to log our method calls, route method calls
# to extra or custom logic, adapt a class to a new interface, and so on.

# Python 2.X vs 3.X you may need to redefine operator overloading methods (__repr__ etc) 
# in wrapper classes (either by hand, by tools, or by superclasses) if they are used by
# embedded objects and you want them to be intercepted in new-style classes.

print("-" * 20 + "#6 Pseudoprivate Class Attributes (name mangling)" + "-" * 20)

# Attributes are all 'public' and 'virtual', in C++ terms; they're all accessible
# everywhere and are looked up dynamically at runtime.

# Python today does support the notion of name 'mangling' (i.e., expansion)
# to localize some names in classes. Mangled names are sometimes misleadingly called
# 'private attributes,' but really this is just a way to localize a name to the class 
# that created it-name mangling does not prevent access by code outside the class. This
# feature is mostly intended to avoid namespace collisions in instances, not to restrict
# access to names in general; mangled names are therefore better called 'pseudoprivate'
# than 'private'.

# Python programmers code internal names with a single underscore (e.g., _X), which 
# is just an informal convention to let you know that a name shouldn't generally be
# changed (it means nothing to Python itself).

# Here's how name mangling works: within a class statement only, any names that
# start with two underscores but don't end with two underscores are automatically
# expanded to include the name of the enclosing class at their front. For instance,
# a name like __X within a class named Spam is changed to _Spam__X automatically:
# the original name is prefixed with a single underscore and the enclosing class's name.
# Because the modified name contains the name of the enclosing class, it's generally 
# unique; it won't clash with similar names created by other classes in a hierarchy.

# For example, in a class named Spam, a method named __meth is mangled to _Spam__meth,
# and an instance attribute reference self.__X is transformed to self._Spam__X.

# In Python, all instance attributes wind up in the single instance object at the bottom
# of the class tree, and are shared by all class-level method functions the instance is
# passed into. This is different from the C++ model, where each class gets its own space
# for data members it defines.

# Within a class's method in Python, whenever a method assigns to a self attribute (e.g.,
# self.attr = value), it changes or creates an attribute in the instance (recall that 
# inheritance searches happen only on reference, not on assignment). Because this is true 
# even if multiple classes in a hierarchy assign to the same attribute, collisions 
# are possible.

class C1:
    def meth1(self): self.X = 88                                   # I assume X is mine  
    def meth2(self): print(self.X)
    
class C2:
    def metha(self): self.X = 99                                   # Me too
    def methb(self): print(self.X)

class C3(C1, C2):
    pass

I = C3()

# I.meth2()                                                        # AttributeError: C3 instance has no attribute 'X'

I.meth1()                                                          # create self.X = 88
I.meth2()                                                          # 88
I.methb()                                                          # 88

I.metha()                                                          # self.X = 99
I.meth2()                                                          # 99
I.methb()                                                          # 99

# To guarantee that an attribute belongs to the class that uses it, though, prefix 
# the name with double underscores everywhere it is used in the class.

class C1:
    def meth1(self): self.__X = 33                                 # Now X is mine
    def meth2(self): print(self.__X)                               # Becomes _C1__X in I

class C2:
    def metha(self): self.__X = 44                                 # Me too
    def methb(self): print(self.__X)                               # Becomes _C2__X in I
    
class C3(C1, C2): 
    pass

I = C3()

I.meth1()
I.meth2()                                                          # 33

I.metha()
I.meth2()                                                          # 33
I.methb()                                                          # 34

print(I.__dict__)                                                  # {'_C2__X': 44, '_C1__X': 33}

# This trick can avoid potential name collisions in the instance, but note that it does not
# amount to true privacy. If you know the name of the enclosing class, you can still access
# either of these attributes anywhere you have a reference to the instance by using the
# fully expanded name (e.g., I._C1__X = 77).

# If a method is intended for use only within a class that may be mixed into
# other classes, the double underscore prefix virtually ensures that method 
# won't interfere with other names in the tree, especially in multiple-inheritance
# scenarios

# Superclasses are searched according to their left-to-right order in class header lines. 
# Here, this means Sub1 prefers Tool attributes to thoseSuper. Pseudoprivate names also 
# prevent subclasses from accidentally redefining the internal method's names, as in Sub2.

class Super:
    def method(self):                                              # A real application method
        pass

class Tool:
    def __method(self): pass                                       # Becomes _Tool__method
    def other(self): self.__method()                               # Use my internal method

class Sub1(Tool, Super):
    def actions(self): self.method()                               # Runs Super.method as expected
    
class Sub2(Tool):
    def __init__(self):
        self.method = 99                                           # Doesn't break Tool.__method
        
print("-" * 20 + "#7 Methods Are Objects: Bound or Unbound" + "-" * 20)

# Bound methods combine an instance and a method function; you can call them
# without passing in an instance object explicitly because the original instance is still
# available.

# We learned how functions can be processed as normal objects. Methods
# are a kind of object too, and can be used generically in much the same way as other
# objects-they can be assigned to names, passed to functions, stored in data structures,
# and so on-and like simple functions, qualify as "first class" objects. Because 
# a class's methods can be accessed from an instance or a class, though, they actually
# come in two flavors in Python:

# Unbound (class) method objects: no self
# Accessing a function attribute of a class by qualifying the class returns an unbound
# method object. To call the method, you must provide an instance object explicitly
# as the first argument. In Python 3.X, an unbound method is the same as a simple
# function and can be called through the class's name; in 2.X it's a distinct type and
# cannot be called without providing an instance.

# Bound (instance) method objects: self + function pairs
# Accessing a function attribute of a class by qualifying an instance returns a bound
# method object. Python automatically packages the instance with the function in
# the bound method object, so you don't need to pass an instance to call the method.

# When calling a bound method object, Python provides an instance for you automatically-
# the instance used to create the bound method object. This means that bound
# method objects are usually interchangeable with simple function objects, and makes
# them especially useful for interfaces originally written for functions.

class Spam:
    def doit(self, message):
        print(message)
    
object1 = Spam()
object1.doit('hello world')

# Really, though, a bound method object is generated along the way, just before the
# method call's parentheses. In fact, we can fetch a bound method without actually 
# calling it. An object.name expression evaluates to an object as all expressions do. 
# In the following, it returns a bound method object that packages the instance 
# (object1) with the method function (Spam.doit). We can assign this bound method
# pair to another name and then call it as though it were a simple function.

object1 = Spam()
x = object1.doit
x('hello world')                                                   # Same effect as object1.doit('...')              

# On the other hand, if we qualify the class to get to doit, we get back an unbound method
# object, which is simply a reference to the function object. To call this type of method,
# we must pass in an instance as the leftmost argument-there isn't one in the expression
# otherwise, and the method expects it

object1 = Spam()
t = Spam.doit                                                      # Unbound method object (a function in 3.X)
t(object1, 'howdy')                                                # Pass in instance (if the method expects one in 3.X)

# By extension, the same rules apply within a class's method if we reference self attributes
# that refer to functions in the class. A self.method expression is a bound method object
# because self is an instance object.

class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1                                                # Another bound method object 
        x(42)                                                      # Looks like a simple function

Eggs().m2()                                                        # 42

# Most of the time, you call methods immediately after fetching them with attribute
# qualification, so you don't always notice the method objects generated along the way.
# But if you start writing code that calls objects generically, you need to be careful to treat
# unbound methods specially-they normally require an explicit instance object to be
# passed in.

print("-" * 20 + "#8 Unbound Methods Are Functions in 3.X" + "-" * 20)

# In Python 3.X, the language has dropped the notion of unbound methods. What we
# describe as an unbound method here is treated as a simple function in 3.X. For most
# purposes, this makes no difference to your code; either way, an instance will be passed
# to a method's first argument when it's called through an instance.

# Programs that do explicit type testing might be impacted, though-if you print the type
# of an instance-less class-level method, it displays "unbound method" in 2.X, and
# "function" in 3.X.

# Moreover, in 3.X it is OK to call a method without an instance, as long as the method
# does not expect one and you call it only through the class and never through an instance.

class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(arg1, arg2):                                      # A simple function in 3.X
        print(arg1 + arg2)
    def normal(self, arg1, arg2):                                  # Instance expected when called
        print(self.data + arg1 + arg2)

X = Selfless(2)
X.normal(3, 4)                                                     # 9 - Instance passed to self automatically 2 + 3 + 4
Selfless.normal(X, 3, 4)                                           # 9 - self expected by method: pass manually
# Selfless.selfless(3, 4)                                          # 7 - No instance: works in 3.X, fails in 2.X

# The last test in this fails in 2.X, because unbound methods require an instance to be
# passed by default; it works in 3.X because such methods are treated as simple functions
# not requiring an instance. 

# The following two calls still fail in both 3.X and 2.X.

# X.selfless(3, 4)                                                 # TypeError: selfless() takes 2 positional arguments but 3 were given
# Selfless.normal(3, 4)                                            # TypeError: normal() missing 1 required positional argument: 'arg2'

# Because of this change, the staticmethod built-in function and decorator described in
# the next chapter is not needed in 3.X for methods without a self argument that are
# called only through the class name, and never through an instance-such methods are
# run as simple functions, without receiving an instance argument.

print("-" * 20 + "#9 Bound Methods and Other Callable Objects" + "-" * 20)

# As mentioned earlier, bound methods can be processed as generic objects, just like
# simple functions-they can be passed around a program arbitrarily. Moreover, because
# bound methods combine both a function and an instance in a single package, they can
# be treated like any other callable object and require no special syntax when invoked.

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3
    
x = Number(2)
y = Number(3)
z = Number(4)

print(x.double())                                                  # 4 Normal immediate call    

acts = [x.double, y.double, y.triple, z.double]                    # List of bound methods
for act in acts:                                                   # Calls are deferred
    print(act()),                                                  # 4 6 9 8 - Call as functions
print()

# Like simple functions, bound method objects have introspection information of their
# own, including attributes that give access to the instance object and method function
# they pair. Calling the bound method simply dispatches the pair

bound = x.double
print(bound.__self__, bound.__func__)                              # (<__main__.Number instance at 0xb72bbfcc>, <function double at 0xb73594fc>)
print(bound.__self__.base)                                         # 2
print(bound())                                                     # 4
print(bound.__call__())                                            # 4

# __call__ vs __init__
# https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call-in-python

# In fact, bound methods are just one of a handful of callable object types in Python. As
# the following demonstrates, simple functions coded with a def or lambda, instances that
# inherit a __call__, and bound instance methods can all be treated and called the same way

def square(arg):                                                   # Simple functions (def or lambda)
    return arg ** 2 
    
class Sum:                                                         # Callable instances
    def __init__(self, val):                                       
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:                                                     # Bound methods 
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]                        # function, instance, method

for act in actions:                                                # All three called same way
    print(act(5)),                                                 # 25 7 15 - Call any one-arg callable
print('')

print(actions[-1](5))                                              # 15
print([act(5) for act in actions])                                 # [25, 7, 15]
print(list(map(lambda x: x(5), actions)))                          # [25, 7, 15]

# Technically speaking, classes belong in the callable objects category too, but we 
# normally call them to generate instances rather than to do actual work-a single action is
# better coded as a simple function than a class with a constructor, but the class here
# serves to illustrate its callable nature:

class Negate:
    def __init__(self, val):                                       # Classes are callable too
        self.val = -val                                            # But called for object, not work
    def __repr__(self):                                            # Instance print format
        return str(self.val)

actions = [square, sobject, pobject.method, Negate]                # Call a class too

print([act(5) for act in actions])                                 # [25, 7, 15, -5] - Runs __repr__ not __str__


# Complete explanation of format
# https://pyformat.info/

table = {act(5): act for act in actions}                           # 3.X/2.7 dict comprehension
for (key, value) in table.items():
    print('{0:>2} => {1}'.format(key, value))

# 25 => <function square at 0xb7426764>
# 15 => <bound method Product.method of <__main__.Product instance at 0xb731d62c>>
# -5 => __main__.Negate
#  7 => <__main__.Sum instance at 0xb731d5ec>


# class MyGui:
#     def handler(self):
#         ...use self.attr for state...
#     def makewidgets(self):
#         b = Button(text='spam', command=self.handler)

# Here, the event handler is self.handler-a bound method object that remembers both
# self and MyGui.handler. Because self will refer to the original instance when handler
# is later invoked on events, the method will have access to instance attributes that can
# retain state between events, as well as class-level methods. With simple functions, state
# normally must be retained in global variables or enclosing function scopes instead.


print("-" * 20 + "#10 Classes Are Objects: Generic Object Factories" + "-" * 20)

# Sometimes, class-based designs require objects to be created in response to conditions
# that can't be predicted when a program is written. The factory design pattern allows
# such a deferred approach.

# Because classes are also "first class" objects, it's easy to pass them around a program,
# store them in data structures, and so on. You can also pass classes to functions that
# generate arbitrary kinds of objects; such functions are sometimes called factories in
# OOP design circles.

def factory(aClass, *pargs, **kargs):                              # Varargs tuple, dict
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print("Message:", message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

object1 = factory(Spam)                                            # Make a Spam object 
object2 = factory(Person, "Arthur", "King")                        # Make a Person object
object3 = factory(Spam)                                            # Ditto, with keywords and default

# And that's the only factory function you'll ever need to write in Python; it works 
# for any class and any constructor arguments. 

object1.doit(99)                                                   # ('Message:', 99)
print(object2.name, object2.job)                                   # ('Arthur', 'King')

# By now, you should know that everything is a "first class" object in Python-including
# classes, which are usually just compiler input in languages like C++. It's natural to 
# pass them around this way.

print("-" * 20 + "#11 Multiple Inheritance: 'Mix-in' Classes" + "-" * 20)

# When searching for an attribute, Python's inheritance search traverses all superclasses
# in the class header from left to right until a match is found. Technically, because any
# of the superclasses may have superclasses of its own, this search can be a bit more
# complex for larger class trees:

# In classic classes (the default until Python 3.0)  the attribute search in all cases
# proceeds depth-first all the way to the top of the inheritance tree, and then from
# left to right

# In new-style classes (optional in 2.X and standard in 3.X), the attribute search is
# usually as before, but in diamond patterns proceeds across by tree levels before
# moving up, in a more breadth-first fashion.

# Diamond patterns appear when multiple classes intree share a common superclass; 
# the new-style search order is designed to visit suchshared superclass just once,
# and after all its subclasses

# Though a useful pattern, multiple inheritance's chief downside is that it can 
# poseconflict when the same method (or other attribute) name is defined in more 
# than one superclass. When this occurs, the conflict is resolved either automatically
# by theheritance search order, or manually in your code:

# Default: By default, inheritance chooses the first occurrence of an attribute it finds
# when an attribute is referenced normally-by self.method(), for example. In this
# mode, Python chooses the lowest and leftmost in classic classes, and in nondiamond 
# patterns in all classes; new-style classes may choose an option to the right
# before one above in diamonds.

# Explicit: In some class models, you may sometimes need to select an attribute explicitly 
# by referencing it through its class name-with superclass.method(self),
# for instance. Your code breaks the conflict and overrides the search's default-to
# select an option to the right of or above the inheritance search's default.

# Perhaps the most common way multiple inheritance is used is to "mix in" general-
# purpose methods from superclasses. Such superclasses are usually called mix-in classes
# -they provide methods you add to application classes by inheritance. In a sense, mix-
# in classes are similar to modules: they provide packages of methods for use in their
# client subclasses. Unlike simple functions in modules, though, methods in mix-in
# classes also can participate in inheritance hierarchies, and have access to the self 
# instance for using state information and other methods in their trees.

# Defining a display method in a mix-in superclass once enables us to reuse it anywhere
# we want to see a custom display format-even in classes that may already have another 
# superclass.

# Listing attributes attached to an instance

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instance attrs only; self is
    instance of lowest class; __X names avoid clashing with client's attrs
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                            self.__class__.__name__,               # My class's name 
                            id(self),                              # id built-function, which returns any object's address
                            self.__attrnames())                    # name = value list
            
# Each instance has a built-in __class__ attribute that references the class from which
# it was created, and each class has a __name__ attribute that references the name in
# the header, so the expression self.__class__.__name__ fetches the name of an 
# instance's class.

class Spam(ListInstance):                                          # Inherit a __str__ method 
    def __init__(self):
        self.data1 = 'food'

x = Spam()
print(x)                                                           # print() and str() run __str__

# <Instance of Spam, address 3073628268:
#     data1=food
# >

class Super:
    def __init__(self):
        self.data1 = 'spam'                                        # Create instance attrs
    def ham(self):
        pass
    
class Sub(Super, ListInstance):                                    # Mix in ham and a __str__
    def __init__(self):                                            # Listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'                                        # More instance attrs
        self.data3 = 42
    def spam(self):                                                # Define another method here
        pass
    
X = Sub()
print(X)                                                           # Run mixed-in __str__

# <Instance of Sub, address 3072961260:
#     data1=spam
#     data2=eggs
#     data3=42
# >

# The ListInstance class we've coded so far works in any class it's mixed into because
# self refers to an instance of the subclass that pulls this class in, whatever that may be.

# ListerInstance mix-in displays instance attributes only (i.e., names 
# attached to the instance object itself). It's trivial to extend the class to display all the
# attributes accessible from an instance, though-both its own and those it inherits from
# its classes. The trick is to use the dir built-in function instead of scanning the instance's
# __dict__ dictionary; the latter holds instance attributes only, but the former also 
# collects all inherited attributes in Python 2.2 and later.

# With __repr__, this code will fall into recursive loops-displaying the value of a method 
# triggers the __repr__ of the method's class, in order to display the class. That is, if
# the lister's __repr__ tries to display a method, displaying the method's class will 
# trigger the lister's __repr__ again. Subtle, but true! Change __str__ to __repr__ here 
# to see this for yourself. If you must use __repr__ in such a context, you can avoid the 
# loops by using isinstance to compare the type of attribute values against types.MethodType
# in the standard library, to know which items to skip

class ListInherited:
    
    def __attrnames(self):
        result = ''
        for attr in dir(self):                                     # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':             # skips __X__ names' values
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s' % (
                          self.__class__.__name__,                 # My class's name
                          id(self),                                # My address
                          self.__attrnames())                      # name = value list


# !IMPORTANT
# There is also an example for class traversing, but I didn't implement it



 



