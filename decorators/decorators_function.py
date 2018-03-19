
# MAIN SOURCE:
# Lutz "Mastering Python Patterns" Chapter 39


# USEFUL LINKS:
#
# 1) functools.wrap
#    https://stackoverflow.com/questions/308999/what-does-functools-wraps-do


# GENERAL INFORMATION:

# - Function decorators, added in Python 2.4, do name rebinding at function
#   definition time, providing a layer of logic that can manage functions
#   and methods, or later calls to them.

# - Class decorators, added in Python 2.6 and 3.0, do name rebinding at
#   class definition time, providing a layer of logic that can manage
#   classes, or the instances created by later calls to them.


print("-" * 20 + "# 1 The Basics" + "-" * 20)


# @decorator                                                    # Decorate function
# def F(arg):
#     ...
# F(99)                                                         # Call function

# Equivalent form:

# def F(arg):
#     ...
# F = decorator(F)                                              # Rebind function name to decorator result 
# F(99)                                                         # Essentially call decorator(F)(99)

# When the function F is later called, it's actually calling the object
# returned by the decorator, which may be either another object that
# implements required wrapping logic, or the original function itself.

# The method name is rebound to the result of a built-in function decorator,
# at the end of the def statement. Calling the original name later invokes
# whatever object the decorator returns.

# class C:
#     @staticmethod
#     def meth(...): ...                                        # meth = staticmethod(meth)

# class C:
#     @property
#     def name(self): ...                                       # name - property(name)

# A decorator itself is a callable that returns a callable. That is, it
# returns the object to be called later when the decorated function is
# invoked through its original name-either a wrapper object to intercept
# later calls, or the original function augmented in some way.

# 1) Add a post-creation step to function definition. Such a structure
#    might be used to register a function to an API, assign function
#    attributes, and so on.

# def decorator(F)
#    # Process function F
#    return F
#
# @decorator
# def func(): ...                                               # func = decorator(func)

# 2) The decorator returns a wrapper that retains the original function
#    in an enclosing scope. When the name func is later called, it really
#    invokes the wrapper function returned by decorator; the wrapper 
#    function can then run the original func because it is still available
#    in an enclosing scope. When coded this way, each decorated function
#    produces a new scope to retain state.

# def decorator(F):
#     def wrapper(*args):                                       # On wrapped function call
#         # Use F ad args
#         # F(*args) calls original function
#     return wrapper
#
# @decorator                                                    # func = decorator(func)
# def func(x, y):                                               # func is passed to decorator's F
#     ...
#
# func(6, 7)                                                    # 6, 7 are passed to wrapper's *args 


# 3) To do the same with classes, we can overload the call operation and
#    use instance attributes instead of enclosing scopes. When the name
#    func is later called now, it really invokes the __call__ operator 
#    overloading method of the instance created by decorator; the __call__
#    method can then run the original func because it is still available
#    in an instance attribute. When coded this way, each decorated function
#    produces a new instance to retain state.


# class decorator:
#     def __init__(self, func):                                 # On @ decoration 
#         self.func = func
#     def __call__(self, *args)                                 # On wrapped function call (when instance, not clas is called)
#         # Use self.func and args
#         # self.func
#
# @decorator
# def func(x, y):                                               # func = decorator(func)
#     ...
#
# func(6, 7)                                                    # 6, 7 are passed to __call__'s *args

# 4) The prior class-based coding works to intercept simple function calls, 
#    but it does not quite work when applied to class-level method functions.
#    The problem with this is that the self in the decorator's __call__ receives 
#    the decorator class instance when the method is later run, and the instance
#    of class C is never included in *args. This makes it impossible to dispatch
#    the call to the original method-the decorator object retains the original
#    method function, but it has no instance to pass to it.


# class decorator:
#     def __init__(self, func):                                 # func is method without instance
#         self.func = func
#     def __call__(self, *args):                                # self is decorator instance
#         # self.func(*args) fails!                             # C instance not in args
#
# class C:
#     @decorator
#     def method(self, x, y):                                   # method = decorator(method)
#         ...                                                   # Rebound to decorator instance

# 5) To support both functions and methods, the nested function alternative
#    works better. When coded this way wrapper receives the C class instance
#    in its first argument, so it can dispatch to the original method and
#    access state information. In previous example 'self' of decorator was
#    passed to call.

# def decorator(F):                                             # F is func or method without instance
#     def wrapper(*args):                                       # class instance is arg[0] for method
#         ...                                                   # F(*args) runs func or method 
#     return wrapper
#
# @decorator
# def func(x, y):                                               # func = decorator(func)
#     ... 
# func(6, 7)                                                    # really call wrapper(6, 7)
#
# class C:
#     @decorator
#     def method(self, x, y):                                   # method = decorator(method)
#         ...
#
# X = C()
# X.method(6, 7)                                                # Really calls wrapper(X, 6, 7) 

print("-" * 20 + "# 2 Decorator Nesting" + "-" * 20)


print("-" * 20 + "# 2 Decorator Arguments" + "-" * 20)


