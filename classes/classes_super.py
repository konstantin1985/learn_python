

# USEFUL LINKS:


# GENERAL INFORMATION:

# In its defense, this call does have a valid use case too - cooperative
# same-named method dispatch in diamond multiple inheritance trees - but
# it seems to ask a lot of newcomers.

# It requires that super be used universally and consistently (if not
# neurotically), much like __slots__ discussed earlier; relies on the
# arguably obscure MRO algorithm to order calls; and addresses a use
# case that seems far more the exception than the norm in Python programs.

# Differs in form between 2.X and 3.X

# In 3.X, relies on arguably non-Pythonic magic, and does not fully apply
# to operator overloading or traditionally coded multiple-inheritance trees

# In 2.X, seems so verbose in this intended role that it may make code more
# complex instead of less

# Offers one solution to the difficult problem of same-named method dispatch
# in multiple inheritance trees, for programs that choose to use it universally
# and consistently. But therein lies one of its largest obstacles: it requires
# universal deployment to address a problem most programmers probably do not have.

# In single-inheritance mode can mask later problems and lead to unexpected
# behavior as trees grow

# In multiple-inheritance mode brings with it substantial complexity for an
# atypical Python use case

import sys

print("-" * 20 + "#1 Traditional Superclass Call Form: Portable, General" + "-" * 20)

# In general, this book's examples prefer to call back to superclass methods
# when needed by naming the superclass explicitly, because this technique is
# traditional in Python, because it works the same in both Python 2.X and 3.X,
# and because it sidesteps limitations and complexities related to this call
# in both 2.X and 3.X.

# This form works the same in 2.X and 3.X, follows Python's normal method call
# mapping model, applies to all inheritance tree forms, and does not lead to 
# confusing behavior when operator overloading is used. 

class C:                                                            # In Python 2.X and 3.X
    def act(self):
        print('spam')

class D(C):
    def act(self):
        C.act(self)                                                 # Name superclass explicitly, pass self
        print('eggs')
        
X = D()
X.act()
# spam
# eggs

print("-" * 20 + "#2 Basic super usage and its tradeoffs" + "-" * 20)

# The role we're interested in here is more commonly used, and more frequently
# requested by people with Java backgrounds-to allow superclasses to be named 
# generically in inheritance trees. This is intended to promote simpler code
# maintenance, and to avoid having to type long superclass reference paths in
# calls.

# This works, and minimizes code changes - you don't need to update the call 
# if D's superclass changes in the future. One of the biggest downsides of 
# this call in 3.X, though, is its reliance on deep magic: though prone to 
# change, it operates today by inspecting the call stack in order to automatically
# locate the self argument and find the superclass, and pairs the two in a special
# proxy object that routes the later call to the superclass version of the method.
# If that sounds complicated and strange, it's because it is.


if (sys.version_info >= (3, 0)):

    class C:                                                            # Only Python 3.X
        def act(self):
            print('spam')
    
    class D(C):
        def act(self):
            super().act()                                               # Reference superclass generically, omit self
            print('eggs')                                               # Pay attention to brackets in super()
    
    X = D()
    X.act()
    # spam
    # eggs

# In fact, this call form doesn't work at all outside the context of a class's
# method. Really, this call's semantics resembles nothing else in Python-it's
# neither a bound nor unbound method, and somehow finds a self even though you
# omit one in the call. 

    class E(C):
        def method(self):                                                   # self is implicit in super...only!
            proxy = super()                                                 # This form has no meaning outside a method
            print(proxy)                                                    # Show the normally hidden proxy object
            proxy.act()                                                     # No arguments: implicitly calls superclass method!
        
    E().method()
    # <super: <class 'E'>, <E object>>
    # spam   
    
# The heavily implicit nature of this call makes this difficult to see, and
# even flies in the face of Python's explicit self policy that holds true
# everywhere else. That is, this call violates a fundamental Python idiom 
# for a single use case.

print("-" * 20 + "#3 Pitfall: Adding multiple inheritance naively" + "-" * 20)

# Besides its unusual semantics, even in 3.X this super role applies most
# directly to single inheritance trees, and can become problematic as soon
# as classes employ multiple inheritance with traditionally coded classes. 
# This seems a major limitation of scope; due to the utility of mix-in
# classes in Python, multiple inheritance from disjoint and independent 
# superclasses is probably more the norm than the exception in realistic code.
# The super call seems a recipe for disaster in classes coded to naively use
# its basic mode, without allowing for its much more subtle implications in
# multiple inheritance trees.

if (sys.version_info >= (3, 0)):

    class A:                                                            # Only Python 3.X
        def act(self): print('A')
    class B:
        def act(self): print('B')
    class C(A):
        def act(self):
            super().act()                                               # super applied to a single-inheritance tree

    X = C()
    X.act()
    # A
    
# It does not raise an exception for multiple inheritance trees, but will
# naively pick just the leftmost superclass having the method being run
# (technically, the first per the MRO), which may or may not be the one 
# that you want.
    
    class C(A, B):                                                      # Add a B mix-in class with the same method
        def act(self):
            super().act()                                               # Doesn't fail on multi-inher, but picks just one!
    
    X = C()
    X.act()
    # A

    class C(B,A):
        def act(self):
            super().act()                                               # If B is listed first, A.act() is no longer run!
    
    X = C()
    X.act()
    # B

# Perhaps worse, this silently masks the fact that you should probably
# be selecting superclasses explicitly in this case, as we learned earlier
# in both this chapter and its predecessor.

    class C(A, B):                                                      # Traditional form
        def act(self):                                                  # You probably need to be more explicit here
            A.act(self)                                                 # This form handles both single and multiple inher
            B.act(self)                                                 # And works the same in both Python 3.X and 2.X
                                                                        # So why use the super() special case at all?
    X = C()
    X.act()

# Much more subtly, as we'll also see ahead, once you step up to multiple
# inheritance calls this way, the super calls in your code might not invoke
# the class you expect them to. They'll be routed per the MRO order, which,
# depending on where else super might be used, may invoke a method in a
# class that is not the caller's superclass at all!

print("-" * 20 + "#4 Limitation: Operator overloading" + "-" * 20)

# Super also doesn't fully work in the presence of __X__ operator overloading
# methods. Direct named calls to overload methods in the superclass operate
# normally, but using the super result in an expression fails to dispatch
# to the superclass's overload method.

if (sys.version_info >= (3, 0)):

    class C:                                                            # In Python 3.X
        def __getitem__(self, ix):                                      # Indexing overload method
            print('C index')
            
    
    class D(C):
        def __getitem__(self, ix):                                      # Redefine to extend here
            print('D index')
            C.__getitem__(self, ix)                                     # Traditional call form works
            super().__getitem__(ix)                                     # Direct name calls work too
            super()[ix]                                                 # But operators do not! (__getattribute__)                            

    X = C()
    X[99]
    # C index
    X = D()
    # X[99]                                                             # TypeError: 'super' object is not subscriptable

# This behavior is due to the very same new-style (and 3.X) class change
# described earlier because the proxy object returned by super uses 
# __getattribute__ to catch and dispatch later method calls, it fails to
# intercept the automatic __X__ method invocations run by built-in 
# operations including expressions, as these begin their search in the
# class instead of the instance. 

print("-" * 20 + "#5 Use differs in Python 2.X: Verbose calls" + "-" * 20)

# Its form differs between 2.X and 3.X - and not just between classic and 
# new-style classes. It's really a different tool in 2.X, which cannot run
# 3.X's simpler form.

# To make this call work in Python 2.X, you must first use new-style classes. 
# Even then, you must also explicitly pass in the immediate class name and 
# self to super, making this call so complex and verbose that in most cases
# it's probably easier to avoid it completely, and simply name the superclass
# explicitly per the previous traditional code pattern.

if (sys.version_info < (3, 0)):

    class C(object):                                                        # In Python 2.X: for new-style classes onl
        def act(self):
            print('spam')
        
    class D(C):
        def act(self):
            super(D, self).act()                                            # 2.X: different call format - seems too complex
            print('eggs')

    X = D()
    X.act()
    # spam
    # eggs
    
# Although you can use the 2.X call form in 3.X for backward compatibility,
# it's too cumbersome to deploy in 3.X-only code, and the more reasonable 3.X
# form is not usable in 2.X.

# On the other hand, the traditional call form with explicit class names works
# in 2.X in both classic and new-style classes, and exactly as it does in 3.X

    class D(C):
        def act(self):
            C.act(self)
            print('eggs')
    
    X = D()
    X.act()
    # spam
    # eggs

print("-" * 20 + "#6 The super Upsides: Tree Changes and Dispatch" + "-" * 20)

# Changing class trees at runtime: When a superclass may be changed at runtime,
# it's not possible to hardcode its name in a call expression, but it is 
# possible to dispatch calls via super.

# Cooperative multiple inheritance method dispatch: When multiple inheritance
# trees must dispatch to the same-named method in multiple classes, super can
# provide a protocol for orderly call routing.

print("-" * 20 + "#7 Runtime Class Changes and super" + "-" * 20)

# Superclass that might be changed at runtime dynamically preclude hardcoding
# their names in a subclass's methods, while super will happily look up the
# current superclass dynamically.

if (sys.version_info >= (3, 0)):

    class X:
        def m(self): print('X.m')
    
    class Y:
        def m(self): print('Y.m')
    
    class C(X):                                                                 # Start out inheriting from X
        def m(self): super().m()                                                # Can't hardcode class name here
    
    i = C()
    i.m()
    # X.m
    C.__bases__ = (Y,)                                                          # Change the base class
    i.m()
    # Y.m
    
# This works, but seems rare in the extreme. Moreover, there may be other ways
# to achieve the same effect - perhaps most simply, calling through the
# current superclass tuple's value indirectly.

    class C(X):
        def m(self): C.__bases__[0].m(self)                                     # Special code for a special case 

    i = C()
    i.m()
    # X.m
    C.__bases__ = (Y, )                                                         # Same effect without super
    i.m()
    # Y.m
    
print("-" * 20 + "#8 The basics: Cooperative Multiple Inheritance Method Dispatch" + "-" * 20)

# The main rationale commonly given for super. It generally applies to diamond
# pattern multiple inheritance trees, discussed earlier in this chapter, and 
# allows for cooperative and conformant classes to route calls to a same-named
# method coherently among multiple class implementations. Especially for constructors,
# which have multiple implementations normally, this can simplify call routing protocol
# when used consistently.

# In this mode, each super call selects the method from a next class following
# it in the MRO ordering of the class of the self subject of a method call. Because
# the MRO's linear ordering depends on which class self was made from, the order of
# method dispatch orchestrated by super can vary per class tree, and visits each
# class just once as long as all classes use super to dispatch.

# To do so, however, super must be used universally in the class tree to ensure
# that method call chains are passed on - a fairly major requirement that may be
# difficult to enforce in much existing and new code.

class B:
    def __init__(self): print('B.__init__')                                     # Disjopint class tree branches

class C:
    def __init__(self): print('C.__init__')

class D(B, C): pass

x = D()                                                                         # Runs leftmost only by default
# B.__init__

# In this case, superclass tree branches are disjoint (they don't share a common
# explicit ancestor), so subclasses that combine them must call through each
# superclass by name - a common situation in much existing Python code that super
# cannot address directly without code changes.

class D(B, C):
    def __init__(self):
        B.__init__(self)                                                        # Traditional form
        C.__init__(self)                                                        # Invoke supers by name

x = D()
# B.__init__
# C.__init__

# In diamond class tree patterns, though, explicit-name calls may by default
# trigger the top-level class's method more than once, though this might be
# subverted with additional protocols (e.g., status markers in the instance)

class A:
    def __init__(self): print('A.__init__')
    
class B(A):
    def __init__(self): print('B.__init__'); A.__init__(self)

class C(A):
    def __init__(self): print('C.__init__'); A.__init__(self)
    
x = B()
# B.__init__
# A.__init__

x = C()                                                                         # Each super works by itself
# C.__init__
# A.__init__

class D(B, C): pass                                                             # Still runs leftmost only

x = D()
# B.__init__
# A.__init__

print('-----')

class D(B, C):
    def __init__(self):
        B.__init__(self)                                                        # Traditional form
        C.__init__(self)                                                        # Invoke both supers by name

x = D()                                                                         # But this now invokes A twice!
# B.__init__
# A.__init__
# C.__init__
# A.__init__

print('*****')

# By contrast, if all classes use super, or are appropriately coerced by
# proxies to behave as if they do, the method calls are dispatched according
# to class order in the MRO, such that the top-level class's method is run
# just once.

if(sys.version_info >= (3, 0)):

    class A:
        def __init__(self): print('A.__init__')
        
    class B(A):
        def __init__(self): print('B.__init__'); super().__init__()
        
    class C(A):
        def __init__(self): print('C.__init__'); super().__init__()
     
    x = B()                                                                     # Runs B.__init__, A is next super in self's B MRO                         
    # B.__init__
    # A.__init__

    x = C()
    # C.__init__
    # A.__init__
    
    class D(B, C): pass                                                         # Runs B.__init__, C is next super in self's D MRO!
    x = D()                                                                     
    # B.__init__
    # C.__init__
    # A.__init__                                                                # Just one invocation of A.__init__

# The real magic behind this is the linear MRO list constructed for the class
# of self - because each class appears just once on this list, and because super
# dispatches to the next class on this list, it ensures an orderly invocation
# chain that visits each class just once. 

# IMPORTANT: Crucially, the next class following B in the MRO differs depending
# on the class of self - it's A for a B instance, but C for a D instance, 
# accounting for the order of constructors run.

    print(B.__mro__)
    # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    
    print(D.__mro__)
    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# By selecting a next class in the MRO sequence, a super call in a class's
# method propagates the call through the tree, so long as all classes do the
# same. In this mode super does not necessarily choose a superclass at all;
# it picks the next in the linearized MRO, which might be a sibling-or even
# a lower relative-in the class tree of a given instance.

print("-" * 20 + "#9 Some more stuff on super, didn't study it" + "-" * 20)

