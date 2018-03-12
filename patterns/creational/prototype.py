

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 3

# USEFUL LINKS:
# 1) Dictionary items
#    https://www.tutorialspoint.com/python/dictionary_items.htm
# 2) Explanation of id()
#    https://stackoverflow.com/questions/15667189/what-is-the-id-function-used-for

# GENERAL INFORMATION:



print("-" * 20 + "# 1 Preliminaries" + "-" * 20)

# The Prototype design pattern helps us with creating object clones.
# In its simplest version, the Prototype pattern is just a clone()
# function that accepts an object as an input parameter and returns
# a clone of it. In Python, this can be done using the copy.deepcopy()
# function.

import copy


class A:
    
    def __init__(self):
        self.x = 18
        self.msg = 'Hello'
        
class B(A):
    
    def __init__(self):
        A.__init__(self)
        self.y = 34
    
    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

# In the main part, we create an instance of class B b, and use
# deepcopy() to create a clone of b named c. The result is that
# all the members of the hierarchy (at the point of time the
# cloning happens) are copied in the clone c.

if __name__ == "__main__":
    b = B()
    c = copy.deepcopy(b)
    print(str(b), str(c))                                # ('18, Hello, 34', '18, Hello, 34')
    print(b, c)                                          # (<__main__.B instance at 0xb731186c>, <__main__.B instance at 0xb7311cac>)
    
# The two objects reside in two different memory addresses
# (the 0x... part). This means that the two objects are two
# independent copies.
  
print("-" * 20 + "# 2 Use cases" + "-" * 20)

# The Prototype pattern is useful when we have an existing
# object and we want to create an exact copy of it. A copy
# of an object is usually required when we know that parts
# of the object will be modified but we want to keep the
# original object untouched. 

# Another case where Prototype comes in handy is when we want
# to duplicate a complex object: that is populated from a database
# and has references to other objects that are also populated
# from a database. It is a lot of effort to create an object 
# clone by querying the database(s) multiple times again. Using
# Prototype for such cases is more convenient.

# A deep copy is what we have seen so far: all data of the
# original object are simply copied in the clone, without
# making any exceptions. A shallow copy relies on references.
# Using shallow copies might be worthwhile if the available
# resources are limited (such as embedded systems) or performance
# is critical (such as high-performance computing).

# In Python, we can do shallow copies using the copy.copy()
# function. Python documentation, the differences between a
# shallow copy:
# - A shallow copy constructs a new compound object and then
#   (to the extent possible) inserts references into it to
#   the objects found in the original.
# - A deep copy constructs a new compound object and then,
#   recursively, inserts copies into it of the objects found
#   in the original.

# Shallow copies duplicate as little as possible. A shallow
# copy of a collection is a copy of the collection structure,
# not the elements. With a shallow copy, two collections now
# share the individual elements.

# Deep copies duplicate everything. A deep copy of a collection
# is two collections with all of the elements in the original
# collection duplicated.

print("-" * 20 + "# 3 Implementation" + "-" * 20)

# If we know that there are many similarities between two book
# editions, we can use cloning and modify only the different
# parts of the new edition.

from collections import OrderedDict

class Book:
    
    
    # Clients can pass more parameters in the form of keywords
    # (name=value) using the rest variable-length list. The line
    # self.__dict__.update(rest) adds the contents of rest to the
    # internal dictionary of the Book class to make them part of it.
    
    def __init__(self, name, authors, price, **rest):
        '''
        Examples of rest: publisher, length, tags, pub.date
        '''
        self.name = name
        self.authors = authors
        self.price = price                               # in US dollars                    
        self.__dict__.update(rest)
    
    # Since we don't know all the names of the added parameters,
    # we need to access the internal dict for making use of them
    # in __str__(). And since the contents of a dictionary do not
    # follow any specific order, we use an OrderedDict to force
    # an order; otherwise, every time the program is executed,
    # different outputs will be shown. 
    
    def __str__(self):
        mylist = []
        
        # dict.items(): Return a copy of the dictionary's list of
        # (key, value) pairs (list of tuples). One of Python 3's
        # changes is that items() now return iterators, and a list
        # is never fully built.
        ordered = OrderedDict(sorted(self.__dict__.items())) 
        for key in ordered.keys():
            mylist.append('{}: {}'.format(key, ordered[key]))
            if key == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)                           # INTERESING way to show lists


class Prototype:
    
    def __init__(self):
        self.objects = dict()                            # Register of objects
    
    # register() and unregister() methods, which can be used
    # to keep track of the objects that are cloned in a
    # dictionary. Note that this is just a convenience, and
    # not a necessity.

    def register(self, identifier, obj):
        self.objects[identifier] = obj
        
    def unregister(self, identifier):
        del self.objects[identifier]

    # Return copy of object identified by 'identifier' and
    # change some of its attributes by providing '**attr'
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}.format(identifier)')
        
        # Copy self.objects[identifier] object
        obj = copy.deepcopy(found)
        
        # Update attributes of the copied object
        obj.__dict__.update(attr)
        # Return updated copy
        return obj
         
def main():
    
    b1 = Book('The C Programming Language', ('Kernighan', 'Ritchie'), price=118,
              publisher='Prentice Hall', length=228, date='1978-02-22', tags=
              ('C', 'programming', 'algorithms', 'data structures'))
    
    prototype = Prototype()
    cid = 'k&r-first'                                    # id of the first edition of the book   
    prototype.register(cid, b1)                          # register instance in the prototype instance to make copies of it later on

    # Create send edition of the book by copying the first
    # edition and modifying some fields. Use 'cid' of the 
    # first edition for copying.
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    
    # authors: ('Kernighan', 'Ritchie')
    # date: 1978-02-22
    # length: 228
    # name: The C Programming Language
    # price: 118$
    # publisher: Prentice Hall
    # tags: ('C', 'programming', 'algorithms', 'data structures')
    
    # authors: ('Kernighan', 'Ritchie')
    # date: 1988-04-01
    # edition: 2
    # length: 274
    # name: The C Programming Language(ANSI)
    # price: 48.99$
    # publisher: Prentice Hall
    # tags: ('C', 'programming', 'algorithms', 'data structures')

    # id() an integer (or long integer) which is guaranteed to
    # be unique and constant for this object during its lifetime.
    # It's not the same as 'identifier' in 'Prototype'.

    print("ID b1: {} != ID b2: {}".format(id(b1), id(b2)))
    # ID b1: 3073499052 != ID b2: 3073511692
    # So instances are different.

    # The second edition of The C Programming Language book reuses
    # all the information that was set in the first edition, and
    # all the differences that we defined are only applied to the
    # second edition. The first edition remains unaffected.

if __name__ == "__main__":
    main()
    
    
    



