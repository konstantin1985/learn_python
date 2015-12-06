print "-"*20 + "#1 Class attributes" + "-"*20

'''
Assignments to instance attributes create or change the names in the instance, rather
than in the shared class. More generally, inheritance searches occur only on attribute
references, not on assignment: assigning to an object's attribute always changes that
object, and no other.
'''

class SharedData:
    spam = 42;
    
x = SharedData()
y = SharedData()
print x.spam, y.spam #42 42
x.spam = 10          #we create new attribute spam here
print x.spam, y.spam #10 42
SharedData.spam = 20
print x.spam, y.spam #10 20

class MixedNames:
    data = 'spam'
    
    def __init__(self, value):
        self.data = value
    
    def display(self):
        print "MixedNames.data: " + MixedNames.data + " self.data: " + self.data

mn = MixedNames("kozel")
mn.display()

print "-"*20 + "#2 Class methods" + "-"*20

'''
C++ programmers may recognize Python's self argument as being similar to C++'s
this pointer. In Python, though, self is always explicit in your code: methods must
always go through self to fetch or change attributes of the instance being processed
by the current method call.
'''

class NextClass:
    def printer(self, value):
        self.value = value
        print(self.value)

nc = NextClass()
nc.printer("instance printer")
print nc.value #instance printer
NextClass.printer(nc, "class printer")
print nc.value #class printer


print "-"*20 + "#3 Superclass constructors" + "-"*20

'''
Methods are normally called through instances. Calls to methods through a class,
though, do show up in a variety of special roles. One common scenario involves the
constructor method. The __init__ method, like all attributes, is looked up by inheri-
tance. This means that at construction time, Python locates and calls just one
__init__ . If subclass constructors need to guarantee that superclass construction-time
logic runs, too, they generally must call the superclass's __init__ method explicitly
through the class
'''

class Super(object):
    def __init__(self):
        print "Super.__init__"

#http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
class Sub(Super):
    def __init__(self):
        print "Sub.__init__"
        #Super.__init__(self)             #One way to call superclass constructor
        super(Sub, self).__init__()       #Preferred way to call superclass constructor
        
s = Sub()

print "-"*20 + "#4 Superclass methods" + "-"*20

class Super(object):
    def method(self):
        print "in Super.method()"

class Sub(Super):
    def method(self):
        print "starting Sub.method()"
        Super.method(self)
        print "starting Sub.method()"

sup = Super()
sup.method()

sub = Sub()
sub.method()
