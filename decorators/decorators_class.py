
# MAIN SOURCE:
# Lutz "Mastering Python Patterns" Chapter 39


# USEFUL LINKS:


# GENERAL INFORMATION:


print("-" * 20 + "# 1 The Basics" + "-" * 20)

# Rather than wrapping individual functions or methods, though, class
# decorators are a way to manage classes, or wrap up instance construction
# calls with extra logic that manages or augments instances created from a
# class. In the latter role, they may manage full object interfaces.

# @decorator                                               # Decorate class
# class C:
#     ...
# x = C(99)                                                # Make an instance 

# Is equivalent to the followin

# class C:
#     ...
# C = decorator(C)                                         # Rebind class name to decorator result
# 
# X = C(99)                                                # Essentially calls decorator(C)(99)

# The net effect is that calling the class name later to create an instance
# winds up triggering the callable returned by the decorator, which may or
# may not call the original class itself.

# To insert a wrapper layer that intercepts later instance creation calls,
# return a different callable object. The callable returned by such a class
# decorator typically creates and returns a new instance of the original
# class, augmented in some way to manage its interface.


def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:                                                   # C = decorator(C)
    def __init__(self, x, y):                              # Run by Wrapper.__init__
        self.attr = 'spam'
        
x = C(6, 7)                                                # Really calls Wrapper(6, 7)
print(x.attr)                                              # Runs Wrapper.__getattr__, prints "spam"

# Like function decorators, class decorators are commonly coded as either
# "factory" functions that create and return callables, classes that use
# __init__ or __call__ methods to intercept call operations, or some
# combination thereof. Factory functions typically retain state in enclosing
# scope references, and classes in attributes.




