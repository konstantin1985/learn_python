

# USEFUL LINKS:
# https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python

# PROBLEM:
# Operator overloading. Write a class called MyList that shadows ("wraps") a Python
# list: it should overload most list operators and operations, including +, indexing,
# iteration, slicing, and list methods such as append and sort. See the Python reference
# manual or other documentation for a list of all possible methods to support. Also,
# provide a constructor for your class that takes an existing list (or a MyList instance)
# and copies its components into an instance attribute. Experiment with your class
# interactively.


class MyListIterator:
    
    def __init__(self, data):
        self.data = data                                                   # Don't need to copy here, since 
        self.offset = 0
    
    def __next__(self):
        print("__next__")
        if self.offset >= len(self.data):
            raise StopIteration
        else:
            item = self.data[self.offset]
            self.offset += 1
            return item
    
    next = __next__                                                        # next in Python 2.X, __next__ in Python 3.X

class MyList:
    
    # Note that it's important to copy the start value by calling list
    # instead of slicing here, because otherwise the result may not be
    # a true list and so will not respond to expected list methods, 
    # such as append (e.g., slicing a string returns another string,
    # not a list).

    def __init__(self, data = []):
        self.data = list(data)                                                # Need to copy [:] because list is mutable 
        
    def __add__(self, other):
        return MyList(self.data + other.data)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return MyList(self.data[index])
        else:
            return self.data[index]                                        # Return element if it's indexing
    
    def __iter__(self):                                                    # Also can implement with yield (MyListIterator isn't required in this case).               
        print("__iter__")                                                  # When iter() call is invoked on the MyList object, it returns MyListIterator object.
        return MyListIterator(self.data)                                   # Then we iterate over MyListIterator object with next() calls.
        
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return str(self.data)
    
    def append(self, x):
        self.data.append(x)

    def sort(self):
        self.data.sort()

if __name__ == "__main__":

    l = [1, 2, 3]
    ml1 = MyList(l)
    l[1] = 100                                                                 # If we don't copy data in MyList.__init__, the output of print(ml1) will be [1, 100, 3]
    print(ml1)                                                                 # [1, 2, 3]
    
    ml2 = MyList([4, 5, 6])
    print(ml2)                                                                 # [4, 5, 6]
    
    # +
    ml = ml1 + ml2
    print(ml)                                                                  # [1, 2, 3, 4, 5, 6]
    
    # indexing/slicing
    ml = MyList(['a', 'b', 'c', 'd', 'e', 'f'])
    print(ml[3])                                                               # d
    print(ml[2:4])                                                             # [c, d]
    ml[2:4] = 'pt'
    print(ml)                                                                  # ['a', 'b', 'p', 't', 'e', 'f']
    
    # iteration
    ml = MyList(['a', 'b', 'c', 'd'])
    for x in ml:
        print(x.upper()),                                                      # A B C D
    print('')
    
    # append
    ml = MyList([1, 2])
    ml.append(3)
    print(ml)                                                                  # [1, 2, 3]                                               
    
    # sort
    ml = MyList([1, 3, 4, 2])
    ml.sort()
    print(ml)                                                                  # [1, 2, 3, 4]

# Things to explore:

# a. Why is copying the initial value important here?
# -  list is a mutable object, if it's changed elsewhere, the self.data in MyList
#    will also change if we don't make a copy.

# b. Can you use an empty slice (e.g., start[:]) to copy the initial value if it's
#    a MyList instance?
# -  no, we'll get MyList instance, not list.

# c. Is there a general way to route list method calls to the wrapped list?
# -  use __getattr__, see MyList2 class below. 

# d. Can you add a MyList and a regular list? How about a list and a MyList instance?
# -  we can, but we need to check types, see MyList2 class below.

# e. What type of object should operations like + and slicing return? What about
#    indexing operations?
# -  slicing - MyList, indexing - element of the list.

# f. If you are working with a reasonably recent Python release (version 2.2 or
#    later), you may implement this sort of wrapper class by embedding a real list
#    in a standalone class, or by extending the built-in list type with a subclass.
#    Which is easier, and why?
# -  extending built-in is easier.

class MyList2:
    
    def __init__(self, data = []):
        
        # Note that it's important to copy the start value by calling list
        # instead of slicing here, because otherwise the result may not be
        # a true list and so will not respond to expected list methods, 
        # such as append (e.g., slicing a string returns another string,
        # not a list).
        
        #self.data = data[:]
        self.data = list(data)   
    
    def __getattr__(self, attrname):                                       # sort, append, etc. methods of list        
        return getattr(self.data, attrname)
    
    def __repr__(self):
        return str(self.data)
    
    def __add__(self, other):
        
        if isinstance(other, MyList):
            return MyList2(self.data + other.data)
        
        elif isinstance(other, list):
            return MyList2(self.data + other)
            
        else:
            raise BaseException
    
    # Need to implement specific __radd__ if + is non-commutative
    def __radd__(self, other):
        return self.__add__(other)

if __name__ == "__main__":

    ml2 = MyList2([1, 3, 2, 5, 4])
    print(ml2)                                                             # [1, 3, 2, 5, 4]
    ml2.sort()                                                                  
    print(ml2)                                                             # [1, 2, 3, 4, 5]
    
    ml2 = MyList2(['a', 'b', 'c'])
    mlrv = ml2 + ['d', 'e']                                                          
    print(mlrv)                                                            # ['a', 'b', 'c', 'd', 'e']
    mlrv = ['d', 'e'] + ml2
    print(mlrv)                                                            # ['a', 'b', 'c', 'd', 'e'] - need to implement specific __radd__ if + is non-commutative

