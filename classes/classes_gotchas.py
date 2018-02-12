

# USEFUL LINKS:


# GENERAL INFORMATION:


print("-" * 20 + "#1 Changing Class Attributes Can Have Side Effects" + "-" * 20)

# Theoretically speaking, classes (and class instances) are mutable objects. 
# As with built-in lists and dictionaries, you can change them in place by 
# assigning to their attributes - and as with lists and dictionaries, this
# means that changing a class or instance object may impact multiple
# references to it.

# Because all instances generated from a class share the class's namespace,
# any changes at the class level are reflected in all instances, unless they
# have their own versions of the changed class attributes.

# Because classes, modules, and instances are all just objects with attribute
# namespaces, you can normally change their attributes at runtime by assignments.

class X:
    a = 1                                                          # Class attribute
    
I = X()
print(I.a)                                                         # Inherited by instance
# 1
print(X.a)
# 1

# When we change the class attribute dynamically outside the class statement:
# it also changes the attribute in every object that inherits from the class. 
# Moreover, new instances created from the class during this session or program
# run also get the dynamically set value, regardless of what the class's source
# code says.

X.a = 2                                                            # May change more than X
print(I.a)                                                         # I changes too
# 2
J = X()                                                            # J inherits from X's runtime values
print(J.a)                                                         # (but assigning to J.a changes a in J, not X or I)
# 2
print('-----')

# Here, the classes X and Y work like "fileless" modules - namespaces for
# storing variables we don't want to clash. This is a perfectly legal Python
# programming trick, but it's less appropriate when applied to classes
# written by others; you can't always be sure that class attributes you
# change aren't critical to the class's internal behavior.

class X: pass                                                      # Make a few attribute namespaces
class Y: pass

X.a = 1                                                            # Use class attributes as variables
X.b = 2                                                            # No instances anywhere to be found
X.c = 3
Y.a = X.a + X.b + X.c

for i in range(Y.a): print(i)
# 0, 1, 2, 3, 4, 5

# If you're out to simulate a C struct, you may be better off changing
# instances than classes, as that way only one object is affected.

class Record: pass
X = Record()
X.name = 'Bob'
X.job = 'Pizza maker'


print("-" * 20 + "#2 Changing Mutable Class Attributes Can Have Side Effects, Too" + "-" * 20)

# This gotcha is really an extension of the prior. Because class attributes
# are shared by all instances, if a class attribute references a mutable object,
# changing that object in place from any instance impacts all instances at once.

class C:
    shared = []                                                    # Class attribute
    def __init__(self):
        self.perobj = []                                           # Instance attribute
        
x = C()                                                            # Two instances                  
y = C()                                                            # Implicitly share class attributes
print(y.shared, y.perobj)
# ([], [])

x.shared.append('spam')                                            # Impacts y's view too!
x.perobj.append('spam')                                            # Impacts x's data only

print(y.shared, y.perobj)                                          # y sees change made through x
# (['spam'], [])
print(C.shared)                                                    # Stored on class and shared
# ['spam']

# This effect is no different than many we've seen in this book already:
# mutable objects are shared by simple variables, globals are shared by
# functions, module-level objects are shared by multiple importers, and
# mutable function arguments are shared by the caller and the callee. All
# of these are cases of general behavior-multiple references to a mutable
# object-and all are impacted if the shared object is changed in place from
# any reference.

# It may be made more subtle by the different behavior of assignments to
# instance attributes themselves.

# IMPORTANT DISTINCTION:

x.shared.append('spam')                                            # Changes shared object attached to class in place                                                 
x.shared = 'spam'                                                  # Changes or creates INSTANCE attribute attached to x


print("-" * 20 + "#3 Multiple Inheritance: Order Matters" + "-" * 20)

# If you use multiple inheritance, the order in which superclasses are
# listed in the class statement header can be critical. Python always 
# searches superclasses from left to right, according to their order
# in the header line.

class ListTree:
    def __str__(self):
        return "ListTree"
    
class SuperClass:
    def __str__(self):
        return "SuperClass"

class Sub(ListTree, SuperClass): pass                                   # Get ListTree's __str__ by listing it first

x = Sub()
print(x)
# ListTree


# But now suppose Super and ListTree have their own versions of other 
# same-named attributes, too. If we want one name from Super and another
# from ListTree, the order in which we list them in the class header
# won't help.

class ListTree:
    def __str__(self): return "ListTree"
    def other(self): print("ListTree.other()")
    
class SuperClass:
    def __str__(self): return "SuperClass"
    def other(self): print("SuperClass.other()")

class Sub(ListTree, SuperClass):                                             # Get ListTree's __str__ by listing it first
    other = SuperClass.other                                                 # But explicitly pick Super's version of other
    
x = Sub()
print(x)                                                                     # __str__
# ListTree
x.other()
# SuperClass.other()

# As a rule of thumb, multiple inheritance works best when your mix-in
# classes are as self-contained as possible-because they may be used in
# a variety of contexts, they should not make assumptions about names
# related to other classes in a tree.

# The pseudoprivate __X attributes feature can help by localizing names
# that a class relies on owning and limiting the names that your mix-in
# classes add to the mix. 

# If ListTree only means to export its custom __str__, it can name its other
# method __other to avoid clashing with like-named classes in the tree.

print("-" * 20 + "#4 Scopes in Methods and Classes" + "-" * 20)

# The 'generate' function returns an instance of the nested Spam class.
# Within its code, the class name Spam is assigned in the generate
# function's local scope, and hence is visible to any further nested 
# functions, including code inside method; it's the E in the "LEGB" rule

def generate():
    class Spam:                                                              # Spam is a name in generate's local scope
        count = 1
        def method(self):
            print(Spam.count)                                                # Visible in generate's scope, per LEGB rule (E)
    return Spam()

generate().method()
# 1

# IMPORTANT:

# The local scopes OF all enclosING function defs are automatically visible
# to nestED defs (including nested method defs, as in the example above).

# Even so, keep in mind that method defs cannot see the local scope OF the
# enclosING CLASS; they can see only the local scopes of enclosing defs.
# That's why methods must go through the self instance or the class name
# to reference methods and other attributes defined in the enclosing class
# statement. For example, code in the method must use self.count or 
# Spam.count, not just count.

# To avoid nesting, we could restructure this code such that the class Spam
# is defined at the top level of the module: the nested method function and
# the top-level generate will then both find Spam in their global scopes;
# it's not localized to a function's scope, but is still local to a single
# module.

def generate():                                                              # Spam need to be defined only when we invoke generate()
    return Spam()                                                            # we don't go inside generate() BEFORE it's called

class Spam:
    count = 1
    def method(self):
        print(Spam.count)

generate().method()
# 1

# In fact, this approach is recommended for all Python releases-code tends
# to be simpler in general if you avoid nesting classes and functions. On
# the other hand, class nesting is useful in CLOSURE contexts, where the
# enclosing function's scope retains state usED by the class or
# its methods. In the following, the nested method has access to its own scope,
# the enclosing function's scope (for label), the enclosing module's global 
# scope, anything saved in the self instance by the class, and the class 
# itself via its nonlocal name.

def generate(label):                                                         # Returns a class instead of an instance
    class Spam:
        count = 1
        def method(self):
            print("%s = %s" % (label, Spam.count))
    return Spam                                                              # Return class

aclass = generate('Gotchas')
I = aclass()                                                                 # Instance of the class
I.method()
# Gotchas = 1

print("-" * 20 + "#5 You usually want to call superclass constructors" + "-" * 20)

# Remember that Python runs only one __init__ constructor method when
# an instance is made - the lowest in the class inheritance tree. It 
# does not automatically run the constructors of all superclasses higher
# up. Because constructors normally perform required startup work, you'll
# usually need to run a superclass constructor from a subclass constructor
# -using a manual call through the superclass's name (or super), passing
# along whatever arguments are required-unless you mean to replace the 
# super's constructor altogether, or the superclass doesn't have or inherit
# a constructor at all.


print("-" * 20 + "#6 Delegation-based classes in 3.X: __getattr__ and built-ins" + "-" * 20)

# Classes that use the __getattr__ operator overloading method to delegate
# attribute fetches to wrapped objects may fail in Python 3.X (and 2.X
# when new-style classes are used) unless operator overloading methods
# are redefined in the wrapper class. The names of operator overloading
# methods implicitly fetched by built-in operations are not routed through
# generic attribute-interception methods. To work around this, you must
# redefine such methods in wrapper classes, either manually, with tools,
# or by definition in super-classes.

print("-" * 20 + "#7 KISS Revisited: 'Overwrapping-itis'" + "-" * 20)

# However, you'll simplify debugging and aid maintainability if you make
# your class interfaces intuitive, avoid making your code overly abstract,
# and keep your class hierarchies short and flat unless there is a good
# reason to do otherwise.






