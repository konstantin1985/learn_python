



print("-" * 20 + "#1 The class Statement" + "-" * 20)

# unlike in C++, Python's class is not a declaration. Like a def, a class statement is
# an object builder, and an implicit assignment-when run, it generates a class object
# and stores a reference to it in the name used in the header. Also like a def, a class
# statement is true executable code-your class doesn't exist until Python reaches and
# runs the class statement that defines it. This typically occurs while importing the
# module it is coded in, but not before.

# A class statement effectively defines a namespace.

# When Python executes a class statement (not a call to a class), 
# it runs all the statements in its body, from top to bottom. Assignments that
# happen during this process create names in the class's local scope, which become 
# attributes in the associated class object.

# Because class is a compound statement, any sort of statement can be nested inside its
# body-print, assignments, if, def, and so on. All the statements inside the class 
# statement run when the class statement itself runs (not when the class is later called to make
# an instance). Typically, assignment statements inside the class statement make data
# attributes, and nested defs make method attributes.

# When attached to classes, names are shared; in instances, names
# record per-instance data, not shared behavior or data. Although inheritance searches
# look up names for us, we can always get to an attribute anywhere in a tree by accessing
# the desired object directly.

class CL:
    spam = "111"
    def __init__(self):
        self.data = "888"

c1 = CL()
c2 = CL()
print(c1.spam, c2.spam)                                              # ('111', '111')

# Assignments to instance attributes create or change the names in the instance, rather
# than in the shared class. More generally, inheritance searches occur only on attribute
# references, not on assignment: assigning to an object's attribute always changes that
# object, and no other.

c1.spam = "333"
print(c1.spam, c2.spam)                                              # ('333', '111') - new attribute of c1 is created

CL.spam = "444"
c3 = CL()
print(c1.spam, c2.spam, c3.spam)                                     # ('333', '444', '444')


# Another example

class MixedNames:                                                    # Define class
    data = 'spam'                                                    # Assign class attr

    def __init__(self, value):                                       # Assign method name
        self.data = value                                            # Assign instance attr

    def display(self):
        print(self.data, MixedNames.data)                            # Instance attr, class attr

m1 = MixedNames(100)
m2 = MixedNames(200)

m1.display()                                                         # (100, 'spam')
m2.display()                                                         # (200, 'spam')
print(m1.data)                                                       # 100
print(m2.data)                                                       # 200
print(MixedNames.data)                                               # 'spam'


print("-" * 20 + "#2 Methods" + "-" * 20)

# Method calls made through an instance, like this:
# instance.method(args...)
# are automatically translated to class method function calls of this form:
# class.method(instance, args...)

# In a class's method, the first argument is
# usually called self by convention (technically, only its position is significant, not its
# name). This argument provides methods with a hook back to the instance that is the
# subject of the call-because classes generate many instance objects, they need to use
# this argument to manage data that varies per instance.

class NextClass:
    def printer(self, text):
        self.message = text                                          # Change instance
        print(self.message)                                          # Access instance

x = NextClass()
x.printer('Instance call')                                           # Instance call
print(x.message)                                                     # Instance call

NextClass.printer(x, 'class call')                                   # class call - Direct class call
print(x.message)                                                     # class call - Instance changed again

# NextClass.printer('bad call')                                      # TypeError: unbound method printer() must be called with NextClass instance as first argument (got str instance instead)

# Doing class call is common when you invoke superclass constructor

# class Super:
#     def __init__(self, x):
#         ...default code...

# class Sub(Super):
#     def __init__(self, x, y):
#         Super.__init__(self, x)                                    # Run superclass __init__
#         ...custom code...                                          # Do my init actions

print("-" * 20 + "#3 Inheritance" + "-" * 20)

# Every time you use an expression of the form object.attr where object is an instance or class object,
# Python searches the namespace tree from bottom to top, beginning with object, looking
# for the first attr it can find. This includes references to self attributes in your methods.
# Because lower definitions in the tree override higher ones, inheritance forms the basis
# of specialization.

# Because inheritance finds names in subclasses before it checks superclasses, subclasses
# can replace default behavior by redefining their superclasses' attributes

# Subclasses may replace inherited attributes completely, provide attributes
# that a superclass expects to find, and extend superclass methods by calling
# back to superclass from an overridden method. 

# Example of the extension pattern

class Super:
    def Method(self):
        print("In super method")

class Sub(Super):
    def Method(self):
        print("Start sub method")
        Super.Method(self)
        print("Finish sub method")

sup = Super()
sup.Method()                                                         # In super method

sub = Sub()
sub.Method()

# Start sub method
# In super method
# Finish sub method

print("-" * 20 + "#4 Class Interface Techniques" + "-" * 20)

# Super: Defines a method function and a delegate that expects an action in a subclass.

# Inside the Super.delegate method, self.action invokes a new, independent 
# inheritance search of self and above. Because self references a Provider instance,
# the action method is located in the Provider subclass.

class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()                                                # Expected to be defined

# Inheritor: Doesn't provide any new names, so it gets everything defined in Super.

class Inheritor(Super):
    pass

# Replacer: Overrides Super's method with a version of its own.

class Replacer(Super):
    def method(self):                                                # Replace method completely 
        print('in Replacer.method')

# Extender: Customizes Super's method by overriding and calling back to run the default.

class Extender(Super):
    def method(self):                                                # Extend method behavior
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

# Provider: Implements the action method expected by Super's delegate method.

class Provider(Super):
    def action(self):                                                # Fill in a required method
        print('in Provider.action')

# Example

for klass in (Inheritor, Replacer, Extender):
    
    print('\n' + klass.__name__ + '...')
    klass().method()
    
    # Inheritor...
    # in Super.method
    # 
    # Replacer...
    # in Replacer.method
    # 
    # Extender...
    # starting Extender.method
    # in Super.method
    # ending Extender.method

print("\nProvider...")
x = Provider()
x.delegate()

# Provider...
# in Provider.action

print("-" * 20 + "#5 Abstract Superclasses" + "-" * 20)

# At least in terms of the delegate method, the superclass in this example is what is
# sometimes called an abstract superclass-a class that expects parts of its behavior to be
# provided by its subclasses. If an expected method is not defined in a subclass, Python
# raises an undefined name exception when the inheritance search fails.

# One of the possible implementations of abstract class

class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

X = Super()
# X.delegate()                                                       # NotImplementedError: action must be defined!

# In Python 2.6 and 3.0 we can use abc package

# Although this requires more code and extra knowledge, the potential advantage of 
# this approach is that errors for missing methods are issued when
# we attempt to make an instance of the class, not later when we try to call a missing
# method. This feature may also be used to define an expected interface, automatically
# verified in client classes.

from abc import ABCMeta, abstractmethod

# class Super(metaclass = ABCMeta):                                  # In Python 3.X  

class Super:
    __metaclass__ = ABCMeta
    
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

# X = Super()                                                        # TypeError: Can't instantiate abstract class Super with abstract methods action

class Sub(Super): pass

# X = Sub()                                                          # TypeError: Can't instantiate abstract class Sub with abstract methods action

class Sub(Super):
    def action(self): print('spam')
    
X = Sub()
X.delegate()                                                         # spam

print("-" * 20 + "#6 Namespaces: the conclusion" + "-" * 20)

# Qualified and unqualified names are treated differently, and that
# some scopes serve to initialize object namespaces:
# - Unqualified names (e.g., X) deal with scopes.
# - Qualified attribute names (e.g., object.X) use object namespaces.
# - Some scopes initialize object namespaces (for modules and classes).

# SIMPLE NAMES: GLOBAL UNLESS UNSIGNED
# Assignment (X = value)
# Makes names local by default: creates or changes the name X in the current local
# scope, unless declared global (or nonlocal in 3.X).
# Reference (X)
# Looks for the name X in the current local scope, then any and all enclosing 
# functions, then the current global scope, then the built-in scope, per the LEGB rule.
# Enclosing classes are not searched: class names are fetched as object attributes
# instead.

# ATTRIBUTE NAMES: OBJECT NAMESPACES

# Assignment (object.X = value)
# Creates or alters the attribute name X in the namespace of the object being
# qualified, and none other. Inheritance-tree climbing happens only on attribute
# reference, not on attribute assignment.

# Reference (object.X)
# For class-based objects, searches for the attribute name X in object, then in all
# accessible classes above it, using the inheritance search procedure. For nonclass
# objects such as modules, fetches X from object directly.

# In Python, the place where you assign a name is crucial-it fully determines the
# scope or object in which a name will reside.

X = 11                                                               # Global (module) name/attribute (X, of classes_advanced.X)

def f():
    print(X)                                                         # 11 Access global X

def g():
    X = 22                                                           # Local function variable (X, hides module X)
    print(X)                                                         # 22

class C:
    X = 33                                                           # Class attribute (C.X)
    def m(self):
        X = 44                                                       # Local variable in method (X)
        self.X = 55                                                  # Instance attribute (instance.X)

print(X)                                                             # 11: module (aka classes_advanced.X outside file)
f()                                                                  # 11: global
g()                                                                  # 22: local
print(X)                                                             # 11: module name unchanged

obj = C()
print(obj.X)                                                         # 33: class name inherited by instance

obj.m()                                                              # Attach attribute name X to instance now
print(obj.X)                                                         # 55: instance
print(C.X)                                                           # 33: class (aka obj.X if no X in instance)

# print(C.m.X)                                                       # FAILS: only visible in method
# print(g.X)                                                         # FAILS: only visible in function

# It's also possible for a function to change names
# outside itself, with global and (in Python 3.X) nonlocal statements

X = 11

def g2():
    global X
    X = 22
    
print(X)                                                             # 11 
g2()
print(X)                                                             # 22

print("-" * 20 + "#7 Nested classes" + "-" * 20)



