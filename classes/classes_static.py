

# USEFUL LINKS
# https://stackoverflow.com/questions/6535832/python-inherit-the-superclass-init

# GENERAL DESCRIPTION

# Two kinds of methods within a class that can be called without
# an instance: static methods work roughly like simple instance-less
# functions inside a class, and class methods are passed a class 
# instead of an instance.

# Both are similar to tools in other languages (e.g., C++ static methods). 
# Static and class methods work for classic classes too.

# To enable these method modes, you must call special built-in functions 
# named staticmethod and classmethod within the class, or invoke them with
# the special @name decoration syntax we'll meet later in this chapter.

# Sometimes, programs need to process data associated with classes 
# instead of instances:
# - keeping track of the number of instances created from a class
# - maintaining a list of all of a class's instances that are currently 
#   in memory

# For such tasks, simple functions coded outside a class can often suffice.
# To better associate such code with a class, and to allow such processing
# to be customized with inheritance as usual, it would be better to code 
# these types of functions inside the class itself. 

# Need methods in a class that are not passed, and do not expect, a 
# self instance argument.

# Static methods - simple functions with no self argument that are nested 
# in a class and are designed to work on class attributes
# instead of instance attributes.
# - A static method belongs to the class rather than object of a class.
# - A static method can be invoked without the need for creating an instance of a class.
# - A static method can access static data member and can change the value of it.
# - A static method can not use non static data member or call non-static method directly.

# Class methods - methods of a class that are passed a class object in 
# their first argument instead of an instance, regardless of whether
# they are called through an instance or a class.  Such methods can
# access class data through their class argument.

# Normal methods - instance methods, receive a subject instance when called.

'''
class Test:
    #regular instance method:
    def MyMethod(self):
        print "MyMethod"
    #class method:
    @classmethod
    def MyClassMethod(cl):
        print "MyClassMethod"
    #static method:
    @staticmethod
    def MyStaticMethod():
        print "MyStaticMethod"
    
    
t = Test()
t.MyMethod()
t.MyClassMethod()
t.MyStaticMethod()

#Test.MyMethod()
Test.MyClassMethod() #MyClassMethod
Test.MyStaticMethod() #MyStaticMethod

MyStaticMethod()
'''

print("-" * 20 + "#1 Static Methods in 2.X and 3.X" + "-" * 20)

# - Both Python 2.X and 3.X produce a bound method when a method is fetched
#   through an instance.
# - In Python 2.X, fetching a method from a class produces an unbound method,
#   which cannot be called without manually passing an instance.
# - In Python 3.X, fetching a method from a class produces a SIMPLE FUNCTION, 
#   which can be called normally with no instance present.

# In other words, Python 2.X class methods always require an instance to be passed 
# in, whether they are called through an instance or a class. By contrast, in 
# Python 3.X we are required to pass an instance to a method only if the method 
# expects one.

# The net effect is that:
# - In Python 2.X, we must always declare a method as static in order to call it 
#   without an instance, whether it is called through a class or an instance.
# - In Python 3.X, we need not declare such methods as static if they will
#   be called through a class only, but we must do so in order to call them
#   through an instance.

# Suppose we want to use class attributes to count how many instances are
# generated from a class.

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

a = Spam()
b = Spam()
# Spam.printNumInstances()                                         
# Python 2.X TypeError: unbound method printNumInstances() must be called with Spam instance as first argument (got nothing instead)
# Python 3.X Number of instances created: 2

# a.printNumInstances()                                            
# Python 2.X TypeError: printNumInstances() takes no arguments (1 given)
# Python 3.X TypeError: printNumInstances() takes 0 positional arguments but 1 was given

# The problem here is that unbound instance methods aren't exactly the same as
# simple functions in 2.X. Even though there are no arguments in the def header,
# the method still expects an instance to be passed in when it's called, because
# the function is associated with a class.

# Calls to instance-less methods like printNumInstances made through the class
# fail in Python 2.X but work in Python 3.X. On the other hand, calls made through 
# an instance fail in both Pythons, because an instance is automatically passed 
# to a method that does not have an argument to receive it.

print("-" * 20 + "#2 Static Methods Alternatives" + "-" * 20)

# The simplest idea is to use normal functions outside the class, not class
# methods. This way, an instance isn't expected in the call.

# The following works the same in Python 3.X and 2.X. Because the class name
# is accessible to the simple function as a global variable, this works fine.
# However, the function is much less directly associated with the class by 
# structure.

# Also, simple functions like this cannot be customized by inheritance, since
# they live outside a class's namespace: subclasses cannot directly replace
# or extend such a function by redefining it.

def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1

a = Spam()
b = Spam()
c = Spam()
printNumInstances()                                              # Number of instances created: 3

# We might try to make this example work in a version-neutral way by using a
# normal method and always calling it through (or with) an instance, as usual.

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(self):
        print("Number of instances created: %s" % Spam.numInstances)

a, b, c = Spam(), Spam(), Spam()
a.printNumInstances()                                            # Number of instances created: 3
Spam.printNumInstances(a)                                        # Number of instances created: 3
# But fetching counter changes counter!
Spam().printNumInstances()                                       # Number of instances created: 4

# Unfortunately, as mentioned earlier, such an approach is completely unworkable if
# we don't have an instance available, and making an instance changes the class data.

print("-" * 20 + "#3 Using static and class methods" + "-" * 20)

class Methods:
    
    def imeth(self, x):                                          # Normal method: passed a self
        print([self, x])

    def smeth(x):                                                # Static: no instance passed
        print([x])

    def cmeth(cls, x):                                           # Class: gets class, not instance
        print([cls, x])

    # Overwrite the assignments made earlier by the defs
    smeth = staticmethod(smeth)                                  # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth)                                   # Make smeth a class method (or @: ahead)

obj = Methods()

# Instance (normal methods) are callable through instance or class

obj.imeth(1)                                                     # [<__main__.Methods instance at 0xb7309a8c>, 1] 
Methods.imeth(obj, 2)                                            # [<__main__.Methods instance at 0xb7309a8c>, 2]

# Static methods are called without an instance argument.

# Instance-less functions can be called through a class normally in Python 3.X, 
# but never by default in 2.X. Using the staticmethod built-in allows such 
# methods to also be called through an instance in 3.X and through both a class
# and an instance in Python 2.X

# Static methods can be called through class or through instance 
Methods.smeth(3)                                                 # [3]
obj.smeth(4)                                                     # [4]

# Class methods are similar, but Python automatically passes the class (not an
# instance) in to a class method's first (leftmost) argument, whether it is 
# called through a class or an instance.

Methods.cmeth(5)                                                 # [<class __main__.Methods at 0xb72ff11c>, 5]
obj.cmeth(6)                                                     # [<class __main__.Methods at 0xb72ff11c>, 6]

print("-" * 20 + "#4 Counting Instances with Static Methods" + "-" * 20)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():                                     # Static method for class data
        print("Number of instances %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)          # Create static method
    
a, b, c = Spam(), Spam(), Spam()
Spam.printNumInstances()                                         # Number of instances 3
a.printNumInstances()                                            # Number of instances 3

# Static methods allows subclasses to customize the static method with
# inheritance - a more convenient and powerful approach than importing
# functions from the files.

class Sub(Spam):
    def printNumInstances():                                     # Override a static method
        print("Extra stuff...")                                  # But call back to original
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

# Notice how this also bumps up the superclass's instance counter, 
# because its constructor is inherited and run.

a, b = Sub(), Sub()
a.printNumInstances()
# Extra stuff...
# Number of instances 5
Sub.printNumInstances()
# Extra stuff...
# Number of instances 5
Spam.printNumInstances()
# Number of instances 5

# Moreover, classes can inherit the static method without redefining
# it-it is run without an instance, regardless of where it is defined
# in a class tree.

class Other(Spam): pass

c = Other()
c.printNumInstances()
# Number of instances 6

print("-" * 20 + "#5 Counting Instances with Class Methods" + "-" * 20)

# Rather than hardcoding the class name, the class method uses the
# automatically passed class object generically.

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances: %s" % cls.numInstances)
    printNumInstances = classmethod(printNumInstances)
    
# printNumInstances() method receives the Spam class, not the instance,
# when called from both the class and an instance.

a, b = Spam(), Spam()
a.printNumInstances()                                            # Passes class to first argument
# Number of instances: 2
Spam.printNumInstances()                                         # Also passes class to first argument
# Number of instances: 2

# When using class methods, though, keep in mind that they receive 
# the most specific (i.e., lowest) class of the call's subject. 

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):                                  # Override a class method
        print("Extra stuff...", cls)
        Spam.printNumInstances()                                 # But call back to original
    printNumInstances = classmethod(printNumInstances)
    
class Other(Spam): pass

# he lowest class is passed in whenever a class method is run, even 
# for subclasses that have no class methods of their own.

x = Sub()
y = Spam()
x.printNumInstances()                                            # Call from subclass instance 
# ('Extra stuff...', <class __main__.Sub at 0xb73b750c>)
# Number of instances: 2 __main__.Spam

Sub.printNumInstances()                                          # Class from subclass itself
# ('Extra stuff...', <class __main__.Sub at 0xb732c50c>)
# Number of instances: 2 __main__.Spam

y.printNumInstances()                                            # Call from superclass instance
# Number of instances: 2 __main__.Spam

print("-" * 20 + "#6 Counting Instances with Class Methods" + "-" * 20)

# In fact, because class methods always receive the lowest class in
# an instance's tree:
# - Static methods and explicit class names may be a better solution
#   for processing data local to a class.
# - Class methods may be better suited to processing data that may 
#   differ for each class in a hierarchy.

# Code that needs to manage per-class instance counters, for example,
# might be best off leveraging class methods.

class Spam:
    numInstances = 0
    def count(cls):
        cls.numInstances += 1                                    # cls is lower class above instance
    def __init__(self):
        self.count()                                             # Passes self.__class__ to count (lowest class in the instance's tree)
    count = classmethod(count)
    
class Sub(Spam):
    numInstances = 0
    def __init__(self):                                          # Redefines __init__
        Spam.__init__(self)

class Other(Spam):                                               # Inherits __init__
    numInstances = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()

# Per class data!

print(x.numInstances, y1.numInstances, z1.numInstances)          # (1, 2, 3)
print(Spam.numInstances, Sub.numInstances, Other.numInstances)   # (1, 2, 3)

