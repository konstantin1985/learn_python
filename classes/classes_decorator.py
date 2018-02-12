


# USEFUL LINKS:

# GENERAL INFORMATION:

# A way to run extra processing steps at function and class definition time with 
# explicit syntax.

# - Function decorators - they specify special operation modes for both simple 
#   functions and classes' methods by wrapping them in an extra layer of logic
#   implemented as another function, usually called a metafunction.

#   Function decorators turn out to be very general tools: they are useful for 
#   adding many types of logic to functions besides the static and class method
#   use cases. For instance, they may be used to augment functions with code that
#   logs calls made to them, checks the types of passed arguments during debugging,
#   and so on.

#   Python provides a few built-in function decorators for operations such as marking static
#   and class methods and defining properties

# - Class decorators - do the same for classes, adding support for management of 
#   whole objects and their interfaces. Though perhaps simpler, they often overlap
#   in roles with metaclasses.



print("-" * 20 + "#1 Function Decorator Basics" + "-" * 20)

# class C:
#     @staticmethod                                           # Function decoration syntax
#     def meth():
#         ...

# Internally, this syntax has the same effect as the following-passing the function
# through the decorator and assigning the result back to the original name:

# class C:
#     def meth():
#         ...
#     meth = staticmethod(meth)                                 # name rebinding equivalent

# Decoration rebinds the method name to the decorator's result. The net effect is that
# calling the method function's name later actually triggers the result of its 
# staticmethod decorator first. Because a decorator can return any sort of object, 
# this allows the decorator to insert a layer of logic to be run on every call. 
# The decorator function is free to return either the original function itself, or 
# a new proxy object that saves the original function passed to the decorator to be 
# invoked indirectly after the extra logic layer runs.

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
        
    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


a = Spam()
b = Spam()
Spam.printNumInstances()                                        # Calls from classes and instances work
# Number of instances created: 2
a.printNumInstances()
# Number of instances created: 2


print("-" * 20 + "#2 A First Look at User-Defined Function Decorators" + "-" * 20)

# The __call__ operator overloading method implements function-call interface
# for class instances.

# The following code uses this to define a call proxy class (tracer) that saves 
# the decorated function in the instance and catches calls tooriginal name. 
# Because this is a class, it also has state information-a counter of calls made.

class tracer:
    
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args):                                  # On later calls: add logic, run original
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)
    
@tracer
def spam(a, b, c):                                              # IMPORTANT: Same as spam = tracer(spam) 
    return a + b + c                                            # Wrap spam in a decorator object

print(spam(1, 2, 3))                                            # Really calls the tracer wrapper object
# call 1 to spam
# 6

print(spam('a', 'b', 'c'))                                      # Invokes __call__ in class
# call 2 to spam
# abc

# Because the spam function is run through the tracer decorator, when the original
# spam name is called it actually triggers the __call__ method in the class. This method
# counts and logs the call, and then dispatches it to the original wrapped function.

# As it is, this decorator works for any function that takes positional arguments, 
# but it does not handle keyword arguments, and cannot decorate class-level method
# functions.

# By using nested functions with enclosing scopes for state, instead of callable
# class instances with attributes, function decorators often become more broadly
# applicable to class-level methods too.

def tracer(func):
    def oncall(*args):                                          # On later calls
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0                                            # Closure variable
    return oncall                                               # Function pointer

class C:
    
    @tracer
    def spam(self, a, b, c):                                    # spam = tracer(spam)
        return a + b + c
    
x = C()
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))
    
print("-" * 20 + "#3 A First Look at Class Decorators and Metaclasses" + "-" * 20)

# Class decorators are similar to function decorators, but they are run at the end
# of a class statement to rebind a class name to a callable. As such, they can be 
# used to either manage classes just after they are created, or insert a layer of
# wrapper logic to manage instances when they are later created.

# The code structure:

# def decorator(aClass): ...
#
# @decorator
# class C: ...

# is mapped to the following equivalent:

# def decorator(aClass): ...
#
# class C: ...                                                  # Name rebinding equivalent
# C = decorator(C)


