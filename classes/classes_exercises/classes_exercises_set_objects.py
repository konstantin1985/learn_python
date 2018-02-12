


# USEFUL LINKS:



# USEFUL INFORMATION:

# Set objects. Experiment with the set class described in 
# "Extending Types by Embedding". 

class Set:
    
    def __init__(self, value = []):                         # Constructor 
        self.data = []                                      # Manages a list
        self.concat(value)
    
    def intersect(self, other):                             # other is any sequence 
        rv = []
        for x in other:
            if x in self.data:                              # Pick common items
                rv.append(x)
        return Set(rv)                                      # Return a new set
    
    def union(self, other):                                 # other is any sequence
        rv = self.data[:]                                   # Copy of my list
        for x in other:
            if x not in rv:
                rv.append(x)
        return Set(rv)
    
    def concat(self, value):                                # value: list, Set
        for x in value:                                     # Removes duplicates
            if x not in self.data:
                self.data.append(x)

    def __len__(self):                                      # len(self), if self
        return len(self.data)                               

    def __getitem__(self, key):                             # self[i], self[i:j]
        return self.data[key]                              

    def __and__(self, other):                               # self & other
        return self.intersect(other)
    
    def __or__(self, other):                                # self | other
        return self.union(other)
    
    def __repr__(self):                                     # print(self)
        return str(self.data)
    
    def __iter__(self):                                     # for x in self
        return iter(self.data)


# Run commands to do the following sorts of operations:

# a. Create two sets of integers, and compute their intersection
#    and union by using & and | operator expressions.

int1 = Set([1, 2, 3])
int2 = Set([3, 5, 7])
    
print(int1 & int2)                                          # [3]
print(int1 | int2)                                          # [1, 2, 3, 5, 7]
        
# b. Create a set from a string, and experiment with indexing 
#    your set. Which methods in the class are called?

str1 = Set('abbbc')
print(str1[0], str1[1], str1[2])                            # ('a', 'b', 'c')

# c. Try iterating through the items in your string set using
#    a for loop. Which methods run this time?

str1 = Set('abbbc')
for x in str1:
    print(x)                                                # a b c

# d. Try computing the intersection and union of your string
#    set and a simple Python string. Does it work?

str1 = Set('abc')
print(str1 & 'ab')                                          # ['a', 'b']

# e. Now, extend your set by subclassing to handle arbitrarily
#    many operands using the *args argument form. (Hint: see
#    the function versions of these algorithms in Chapter 18.)
#    Compute intersections and unions of multiple operands with
#    your set subclass. How can you intersect three or more sets,
#    given that & has only two sides?

print('-----')

class MultiSet(Set):
    """
    Inherits all Set names, but extends intersect and union to support
    multiple operands; note that "self" is still the first argument
    (stored in the *args argument now); also note that the inherited
    & and | operators call the new methods here with 2 arguments, but
    processing more than 2 requires a method call, not an expression;
    intersect doesn't remove duplicates here: the Set constructor does;
    """
    
    # It's intersection of self with others,
    # others may not intersect to be in the 
    # result in this implementation.
     
    def intersect(self, *others):   
        res = []                                            # args = ([1, 2, 3], [2, 3, 4], [1, 2, 3]) for line (2)
        for x in self:                                      # Scan first sequence                                                          
            for other in others:                            # For all other args
                if x not in other:                          # Item in each one? 
                    break                                   # No: break out of loop
                else:
                    res.append(x)                           # Yes: add item to end            
        return Set(res)
    
    def union(*args):                                       # self if args[0]
        res = []                                            # args = ([1, 2, 3, 4], [3, 4, 5], [0, 1, 2]) for line (1)        
        for seq in args:                                    # For all args
            for x in seq:                                   # For all nodes
                if not x in res:
                    res.append(x)                           # Add new items to result
        return Set(res)
    
x = MultiSet([1, 2, 3, 4])
y = MultiSet([3, 4, 5])
z = MultiSet([0, 1, 2])

# This could work for "Set", no problem (sequential application of operators)
print(x & y & z)
print(x | y | z)

# This will work only for "MultiSet"
print(x.union(y, z))                                        # [1, 2, 3, 4, 5, 0]   (1) 
print(x.intersect([1, 2, 3], [2, 3, 4], [1, 2, 3]))         # [1, 2, 3]

# f. How would you go about emulating other list operations in the set
#    class? (Hint: __add__ can catch concatenation, and __getattr__ can
#    pass most named list  method calls like append to the wrapped list.)






