

# USEFUL LINKS:
# https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print

# PROBLEM:
# Make a subclass of MyList from exercise 2 (op_overloading.py) called MyListSub, which
# extends MyList to print a message to stdout before each call to the + overloaded
# operation and counts the number of such calls. MyListSub should inherit basic
# method behavior from MyList. Adding a sequence to a MyListSub should print a
# message, increment the counter for + calls, and perform the superclass's method.

# Also, introduce a new method that prints the operation counters to stdout, and
# experiment with your class interactively. Do your counters count calls per instance,
# or per class (for all instances of the class)? How would you program the other
# option? (Hint: it depends on which object the count members are assigned to: class
# members are shared by instances, but self members are per-instance data.)

import sys
from classes_exercises_op_overloading import MyList2

class MyListSub(MyList2):
    
    class_count = 0                                          # It counts per class
    
    def __init__(self, data):
        self.instance_count = 0                              # It counts per instance
        MyList2.__init__(self, data)
        
    def __add__(self, other):
        sys.stdout.write("__add__ call\n")
        MyListSub.class_count += 1
        self.instance_count += 1
        rv = MyList2.__add__(self, other)                    # The problem here is that MyList2 is returned instead of MyListSub
        if isinstance(rv, MyList2):
            return MyListSub(rv.data)
        else:
            return rv                   
        
    def __radd__(self, other):
        sys.stdout.write("__radd__ call\n")
        MyListSub.class_count += 1
        self.instance_count += 1
        rv = MyList2.__radd__(self, other)                   # The problem here is that MyList2 is returned instead of MyListSub
        if isinstance(rv, MyList2):
            return MyListSub(rv.data)
        else:
            return rv                   
        
    def print_counters(self):
        sys.stdout.write("class_count = %s\n" % (MyListSub.class_count,))
        sys.stdout.write("instance_count) = %s\n" % (self.instance_count,))

mls = MyListSub(['a', 'b'])
mls = mls + ['c', 'd']
print(mls)                                                   # ['a', 'b', 'c', 'd']
print(mls[1:])                                               # ['b', 'c', 'd']
print(isinstance(mls, MyListSub))                            # True
mls.print_counters()                                         # count = 1
# class_count = 1
# instance_count) = 0                                        # because 'mls' here 'mls = mls + ['c', 'd']' is the new one

mls = MyListSub(['a', 'b'])
print(mls + ['c'])
mls.print_counters()
# class_count = 2
# instance_count) = 1
