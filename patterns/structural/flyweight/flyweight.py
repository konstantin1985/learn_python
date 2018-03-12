

# MAIN SOURCE:
# Kasampalis "Mastering Python Patterns" Chapter 7

# USEFUL LINKS:
#
# 1) Python __new__
#    https://stackoverflow.com/questions/674304/why-is-init-always-called-after-new
#
# 2) __new__ method explained (also singleton pattern with __new__)
#    http://howto.lintel.in/python-__new__-magic-method-explained/
#
# 3) Python Enum()
#    https://docs.python.org/3/library/enum.html#programmatic-access-to-enumeration-members-and-their-attributes

# GENERAL INFORMATION:

# Object-oriented systems can face performance issues due to the overhead of
# object creation. Performance issues usually appear in embedded systems with
# limited resources, such as smartphones and tablets. The same problem can 
# appear in large and complex systems are where we need to create a very large
# number of objects (and possibly users) that need to coexist at the same time.

# Apart from memory usage, performance is also a consideration. Graphics software,
# including computer games, should be able to render 3D information (for example,
# a forest with thousands of trees or a village full of soldiers) extremely fast. 
# If each object of a 3D terrain is created individually and no data sharing is
# used, the performance will be prohibitive.

# The Flyweight design pattern is a technique used to minimize memory usage and
# improve performance by introducing data sharing between similar objects.
# A Flyweight is a shared object that contains state-independent, immutable
# (also known as intrinsic) data. The state-dependent, mutable (also known as
# extrinsic) data should not be part of Flyweight because this is information that
# cannot be shared since it differs per object. If Flyweight needs extrinsic data,
# they should be provided explicitly by the client code.

# In FPS games, the players (soldiers) share some states, such as representation 
# and behavior. For example, all soldiers of the same team look the same (
# representation). In the same game, all soldiers (of both teams) have some common
# actions, such as jump, duck, and so forth (behavior). This means that we can
# create a Flyweight that will contain all the common data. Of course, the soldiers
# also have many mutable data that are different per soldier and will not be a part
# of the Flyweight, such as weapons, health, locations, and so on.

# Flyweight is an optimization design pattern.

# In general we use Flyweight when an application needs to create a large number of
# computationally expensive objects that share many properties. The important point
# is to separate the immutable (shared) properties, from the mutable.

print("-" * 20 + "# 1 Use Cases" + "-" * 20)

# Flyweight is all about improving performance and memory usage. All embedded
# systems (phones, tablets, game consoles, microcontrollers, and so forth) and
# performance-critical applications (games, 3D graphics processing, real-time
# systems, and so forth) can benefit from it.

# The Gang Of Four (GoF) book lists the following requirements that need to be
# satisfied to effectively use the Flyweight Pattern:
# - The application needs to use a large number of objects.
# - There are so many objects that it's too expensive to store/render them. 
#   Once the mutable state is removed (because if it is required, it should
#   be passed explicitly to Flyweight by the client code), many groups of 
#   distinct objects can be replaced by relatively few shared objects.
# - Object identity is not important for the application. We cannot rely on
#   object identity because object sharing causes identity comparisons to 
#   fail (objects that appear different to the client code, end up having
#   the same identity).

# Note the difference between memoization and the Flyweight pattern. Memoization
# is an optimization technique that uses a cache to avoid recomputing results
# that were already computed in an earlier execution step. Memoization does not
# focus on a specific programming paradigm such as object-oriented programming
# (OOP). In Python, memoization can be applied on both methods and simple 
# functions. Flyweight is an OOP-specific optimization design pattern that
# focuses on sharing object data.

print("-" * 20 + "# 2 Implementation" + "-" * 20)

# In this example, we will create a very small forest of fruit trees. It is
# small to make sure that the whole output is readable in a single terminal
# page. However, no matter how large you make the forest, the memory allocation
# stays the same. 

# The pool variable is the object pool (in other words, our cache). Notice that
# pool is a class attribute (a variable shared by all instances). Using the 
# __new__() special method, which is called before __init__(), we are converting
# the Tree class to a metaclass that supports self-references. This means that 
# cls references the Tree class. When the client code creates an instance of Tree,
# they pass the type of the tree as tree_type. The type of the tree is used to
# check if a tree of the same type has already been created. If that's the case,
# the previously created object is returned; otherwise, the new tree type is added
# to the pool and returned.

# Use __new__ when you need to control the creation of a new instance. Use __init__
# when you need to control initialization of a new instance.

# __new__ is the first step of instance creation. It's called first, and is 
# responsible for returning a new instance of your class. In contrast, __init__
# doesn't return anything; it's only responsible for initializing the instance
# after it's been created.

# __new__ is static class method, while __init__ is instance method.  __new__ has
# to create the instance first, so __init__ can initialize it. Note that __init__
# takes self as parameter. Until you create instance there is no self.

from enum import Enum
import random

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

# Another way to make the same enum
# class TreeType(Enum):
#     apple_tree = 1
#     cherry_tree = 2
#     peach_tree = 3

class Tree(object):
    
    # class attribute (static variable)
    pool = dict()
    
    # no 'self' argument, because it's a static class method
    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type   # intrinsic data
        return obj
    
# The render() method is what will be used to render a tree on the screen. Notice
# how all the mutable (extrinsic) information not known by Flyweight needs to be
# explicitly passed by the client code. In this case, a random age and a location
# of form x, y is used for every tree.

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.
              format(self.tree_type, age, x, y))


def main():
    
    rnd = random.Random()
    age_min, age_max = 1, 30   # in years
    min_point, max_point = 0, 100
    tree_counter = 0
    
    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
        
    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
    
    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
        
    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))
    
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
      
    print("{} = {}? {}".format(id(t4), id(t5), id(t4) == id(t5)))
    print("{} = {}? {}".format(id(t5), id(t6), id(t5) == id(t6)))
          
        
if __name__ == "__main__":
    main() 

# OUTPUT:
# render a tree of type TreeType.apple_tree and age 21 at (78, 32)
# render a tree of type TreeType.apple_tree and age 19 at (2, 34)
# render a tree of type TreeType.apple_tree and age 13 at (90, 47)
# render a tree of type TreeType.apple_tree and age 18 at (51, 92)
# render a tree of type TreeType.apple_tree and age 10 at (72, 25)
# render a tree of type TreeType.apple_tree and age 29 at (48, 32)
# render a tree of type TreeType.apple_tree and age 23 at (89, 26)
# render a tree of type TreeType.apple_tree and age 29 at (80, 68)
# render a tree of type TreeType.apple_tree and age 17 at (9, 3)
# render a tree of type TreeType.apple_tree and age 25 at (35, 48)
# render a tree of type TreeType.cherry_tree and age 27 at (25, 26)
# render a tree of type TreeType.cherry_tree and age 22 at (19, 95)
# render a tree of type TreeType.cherry_tree and age 14 at (90, 77)
# render a tree of type TreeType.peach_tree and age 13 at (48, 40)
# render a tree of type TreeType.peach_tree and age 23 at (82, 60)
# render a tree of type TreeType.peach_tree and age 26 at (28, 68)
# render a tree of type TreeType.peach_tree and age 17 at (4, 38)
# render a tree of type TreeType.peach_tree and age 26 at (80, 18)
# trees rendered: 18
# trees actually created 3
# 3072941068 = 3072941068? True
# 3072941068 = 3072940812? False
