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

print "-"*20 + "#5 Nested classes" + "-"*20

'''
Most importantly, the lookup rules for simple names like X never search enclosing
class statements-just defs, modules, and built-ins (it's the LEGB rule, not CLEGB!).
In method1, for example, X is found in a def outside the enclosing class that has the same
name in its local scope. To get to names assigned in the class (e.g., methods), we must
fetch them as class or instance object attributes, via self.X in this case.
'''

X = 1

def nester():
    X = 2
    print(X)
    class C:
        X = 3
        print X
        def method1(self):
            print(X)         #It's 2, not 3!!!
            print(self.X)
        def method2(self):
            X = 4
            print(X)
            self.X = 5       #Hides class
            print(self.X)
    I = C()
    I.method1()
    I.method2()
            

print(X) #1
nester() #2 3 2 3 4 5
    
print "-"*20 + "#6 Namespace dictionaries" + "-"*20

'''  
In Chapter 23, we learned that module namespaces have a concrete implementation as
dictionaries, exposed with the built-in __dict__ attribute. In Chapter 27 and Chap-
ter 28, we learned that the same holds true for class and instance objects-attribute
qualification is mostly a dictionary indexing operation internally, and attribute inher-
itance is largely a matter of searching linked dictionaries. In fact, within Python, in-
stance and class objects are mostly just dictionaries with links between them. Python
exposes these dictionaries, as well as their links, for use in advanced roles (e.g., for
'''

class Super(object):
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

'''
If we can't find attribute in instance we are looking for it in the class
'''
        
X = Sub()
print X.__dict__        #{}
print X.__class__       #<class '__main__.Sub'>
print Sub.__bases__     #(<class '__main__.Super'>,)
print Super.__bases__   #(<type 'object'>,)

Y = Sub()
X.hello()
print X.__dict__                    #{'data1': 'spam'}
X.hola()
print X.__dict__                    #{'data1': 'spam', 'data2': 'eggs'}

#Classes
print list(Sub.__dict__.keys())     #['__module__', '__doc__', 'hola']
print list(Super.__dict__.keys())   #['__dict__', '__module__', '__weakref__', 'hello', '__doc__']

print Y.__dict__                    #{} - still empty

'''
Because attributes are actually dictionary keys inside Python, there are really two ways
to fetch and assign their values-by qualification, or by key indexing
'''

print X.data1, X.__dict__['data1']  #spam spam
X.data3 = 'toast'
print X.__dict__                    #{'data1': 'spam', 'data3': 'toast', 'data2': 'eggs'}
X.__dict__['data3'] = 'ham'
print X.data3                       #ham
X.__dict__['data4'] = 'kozel'
print X.__dict__                    #{'data4': 'kozel', 'data1': 'spam', 'data3': 'ham', 'data2': 'eggs'}


print "-"*20 + "#7 Namespace links, tree climber" + "-"*20

def classtree(cls, indent):
    print(',' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)  #recursion

def instancetree(inst):
    print("Tree of %s" % inst)
    classtree(inst.__class__, 3)

class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
class E: pass
class F(D,E): pass

instancetree(B())
instancetree(F())


print "-"*20 + "#8 Documentation strings" + "-"*20

'''
The Python "best practice" rule of thumb is to use docstrings for func-
tional documentation (what your objects do) and hash-mark comments for more mi-
cro-level documentation (how arcane bits of code work).
'''

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)

print func.__doc__
c = spam()
print c.__doc__
c.method()
print c.method.__doc__

