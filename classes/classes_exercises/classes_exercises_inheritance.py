

# USEFUL LINKS:

# Concatenate dictionaries:
# https://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python/1781590

# Inheritance. Write a class called Adder that exports a method add(self, x, y)
# that prints a "Not Implemented" message. Then, define two subclasses of Adder
# that implement the add method:

# ListAdder
# With an add method that returns the concatenation of its two list arguments

# DictAdder
# With an add method that returns a new dictionary containing the items in both
# its two dictionary arguments (any definition of dictionary addition will do)

class Adder:
    def add(self, x, y):
        print("Not Implemented")
        
class ListAdder(Adder):    
    def add(self, x, y):                                         # Concatenate lists
        return x + y
    
class DictAdder(Adder):    
    def add(self, x, y):                                         # Concatenate dictionaries
        rv = {}
        rv.update(x)
        rv.update(y)                                             # Pay attention that "return x.update(y)" returns None 
        return rv

a = ['1', '2', '3']
b = ['a', 'b', 'c']

la = ListAdder()
print(la.add(a, b))                                              # ['1', '2', '3', 'a', 'b', 'c']

c = {1: 'a', 2: 'b', 3: 'c'}
d = {'d': 123, 'e': '456'}

da = DictAdder()
print(da.add(c, d))                                              # {1: 'a', 2: 'b', 3: 'c', 'e': '456', 'd': 123}

print("-----")

# Now, extend your Adder superclass to save an object in the instance
# with a constructor (e.g., assign self.data a list or a dictionary), 
# and overload the + operator with an __add__ method to automatically
# dispatch to your add methods (e.g., X +Y triggers X.add(X.data,Y)).
# Where is the best place to put the constructors and operator overloading
# methods (i.e., in which classes)? What sorts of objects can you add
# to your class instances?

class Adder2:
    
    def __init__(self, data = []):
        print("Adder2.__init__")
        self.data = data
    
    def __add__(self, y):
        return self.add(self.data, y)
    
    def __radd__(self, y):
        return self.add(self.data, y)
    
    def add(self, x, y):
        print("Not Implemented")
        
class ListAdder2(Adder2):
    
    # IMPORTANT:
    # We don't need constructors in subclasses, because __init__
    # of the superclass is automatically called if subclass doesn't
    # have it's own __init__ (remember how we find stuff in the 
    # class hierarchy). If subclass has __init__ then we need to 
    # call __init__ of superclass explicitly like:
    # Adder2.__init__(self, data) 
    
    def add(self, x, y):                                         
        return x + y                                             
    
class DictAdder2(Adder2):
    
    def add(self, x, y):
        rv = {}                                                  # So we don't update self.data here?!
        rv.update(x)
        rv.update(y)
        return rv


la2 = ListAdder2(['1', '2', '3'])
 
val = la2 + ['a', 'b', 'c']
print(val)                                                       # __add__ ['1', '2', '3', 'a', 'b', 'c']

val = ['100', '200'] + la2
print(val)                                                       # __radd__ ['1', '2', '3', '100', '200']

da2 = DictAdder2({1: 'a', 2: 'b', 3: 'c'})

val = da2 + {'d': 123, 'e': '456'}
print(val)                                                       # __add__ {1: 'a', 2: 'b', 3: 'c', 'e': '456', 'd': 123}

val = {10: 1000} + da2           
print(val)                                                       # __radd__ {1: 'a', 2: 'b', 3: 'c', 10: 1000}

print("-----")

# In practice, you might find it easier to code your add methods to accept just one
# real argument (e.g., add(self,y)), and add that one argument to the instance's
# current data (e.g., self.data + y). Does this make more sense than passing two
# arguments to add? Would you say this makes your classes more "object-oriented"?

class Adder3:
    
    def __init__(self, data):
        self.data = data
    
    def __add__(self, y):
        return self.add(y)
    
    def __radd__(self, y):
        return self.add(y)
    
    def add(self, y):
        print("Not Implemented")
        
class ListAdder3(Adder3):
       
    # Addition here is commutative
    # Elements are added to the end of the list all the time
    # irrespective of what is called __add__ or __radd__
    def add(self, y):
        return self.data + y 

class DictAdder3(Adder3):
    
    # Not necessary, see explanation above
    # def __init__(self, data = {}):
    #     Adder3.__init__(self, data)
    
    def add(self, y):
        rv = self.data.copy()
        rv.update(y)
        return rv

la3 = ListAdder3(['1', '2', '3'])
 
val = la3 + ['a', 'b', 'c']
print(val)                                                       # __add__ ['1', '2', '3', 'a', 'b', 'c']

val = ['100', '200'] + la3
print(val)                                                       # __radd__ ['1', '2', '3', '100', '200']

da3 = DictAdder3({1: 'a', 2: 'b', 3: 'c'})

val = da3 + {'d': 123, 'e': '456'}
print(val)                                                       # __add__ {1: 'a', 2: 'b', 3: 'c', 'e': '456', 'd': 123}

val = {10: 1000} + da3           
print(val)                                                       # __radd__ {1: 'a', 2: 'b', 3: 'c', 10: 1000}

