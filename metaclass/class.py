print "-"*20 + "1" + "-"*20
'''
Class and instance attributes
'''

class First():
    a = "Kozel"
    
    def FirstSetClassAttribute(self):
        First.a = "Baran"
    
a = First()
b = First()
c = First()
print "a: " + a.a + "  b: " + b.a + "  c: " + c.a #a: Kozel  b: Kozel  c: Kozel

print repr(First.__dict__) #{'a': 'Kozel', 'FirstSetClassAttribute': <function FirstSetClassAttribute at 0xb737872c>, '__module__': '__main__', '__doc__': None}
print repr(b.__dict__) #{} - nothing besides class attributes, "a" attribute is looked up in First class
b.a = "Osel"
print "a: " + a.a + "  b: " + b.a + "  c: " + c.a #a: Kozel  b: Osel  c: Kozel
print repr(First.__dict__) #{'a': 'Kozel', 'FirstSetClassAttribute': <function FirstSetClassAttribute at 0xb737872c>, '__module__': '__main__', '__doc__': None}
print repr(b.__dict__) #{'a': 'Osel'}

a.FirstSetClassAttribute()
#c.a is also "Baran", because c doesn't have "a" attribute on their own
print "a: " + a.a + "  b: " + b.a + "  c: " + c.a #a: Baran  b: Osel  c: Baran

d = First()
print "a: " + a.a + "  b: " + b.a + "  c: " + c.a + "  d: " + d.a #a: Baran  b: Osel  c: Baran  d: Baran

class First1():
    a = "Kozel"
    def __init__(self):
        self.a = "Osel"

a = First1()
print repr(a.__dict__) #{'a': 'Osel'} - because the attribute of OBJECT (self.a) was made in class constructor
print repr(First1.__dict__) #{'a': 'Kozel', '__module__': '__main__', '__doc__': None, '__init__': <function __init__ at 0xb736872c>}
    
class First2():
    def SetVariable(self):
        self.a = "Barashek"

a = First2()
print repr(a.__dict__) #{}
a.SetVariable()
print repr(a.__dict__) #{'a': 'Barashek'}

print "-"*20 + "2" + "-"*20
'''
Class and instance methods
'''

def MethodKozel(self):
    print "MethodKozel"

class Second():
    
    def MyMethod(self):
        print "Second::MyMethod"
        
a = Second()
print repr(a.__dict__) #{}
a.MyMethod() #Second::MyMethod
a.MyMethod = MethodKozel 
print repr(a.__dict__) #{'MyMethod': <function MethodKozel at 0xb73549cc>}
a.MyMethod(a) #"MethodKozel", doesn't work without "a" in brackets
Second.MyMethod(a) #Second::MyMethod

print "-"*20 + "3" + "-"*20
'''
Invoke methods through __getattribute__, bound/unbound methods
https://docs.python.org/2/howto/descriptor.html
'''

class Third(object):
    def __init__(self):
        pass
    def Kozel(self):
        print "Third::Kozel"
    
print repr(Third.__dict__)
'''
dict_proxy({'__dict__': <attribute '__dict__' of 'Third' objects>, 
            '__module__': '__main__', 
            '__weakref__': <attribute '__weakref__' of 'Third' objects>, 
            '__doc__': None, 
            '__init__': <function __init__ at 0xb7344c34>})
'''

print repr(Third.Kozel.__dict__) #{}

print repr(object.__dict__)
'''
dict_proxy({'__setattr__': <slot wrapper '__setattr__' of 'object' objects>, 
            '__reduce_ex__': <method '__reduce_ex__' of 'object' objects>, 
            '__new__': <built-in method __new__ of type object at 0xb771ad00>, 
            '__reduce__': <method '__reduce__' of 'object' objects>, 
            '__str__': <slot wrapper '__str__' of 'object' objects>, 
            '__format__': <method '__format__' of 'object' objects>, 
            '__getattribute__': <slot wrapper '__getattribute__' of 'object' objects>,  #it's here
            '__class__': <attribute '__class__' of 'object' objects>, 
            '__delattr__': <slot wrapper '__delattr__' of 'object' objects>, 
            '__subclasshook__': <method '__subclasshook__' of 'object' objects>, 
            '__repr__': <slot wrapper '__repr__' of 'object' objects>, 
            '__hash__': <slot wrapper '__hash__' of 'object' objects>, 
            '__sizeof__': <method '__sizeof__' of 'object' objects>, 
            '__doc__': 'The most base type', 
            '__init__': <slot wrapper '__init__' of 'object' objects>})
''' 

a = Third()
print Third.__dict__["Kozel"].__get__(a, type(a))  #<bound method Third.Kozel of <__main__.Third object at 0xb732ecac>>
Third.__dict__["Kozel"].__get__(a, type(a))()      #Third::Kozel
print Third.__dict__["Kozel"].__get__(None, Third) #<unbound method Third.Kozel>
#Third.__dict__["Kozel"].__get__(None, Third)()    #error
Third.__dict__["Kozel"].__get__(None, Third)(a)    #Third::Kozel

print Third.__getattribute__(a, "Kozel") #<bound method Third.Kozel of <__main__.Third object at 0xb72dad4c>>
print a.__getattribute__("Kozel") #<bound method Third.Kozel of <__main__.Third object at 0xb7315d2c>>

class Third1(object):
    
    def __getattribute__(self, name):
        print "getting `{}`".format(str(name))
        return object.__getattribute__(self, name)

    def Kozel(self):
        print "Third1::Kozel"

    def getx(self): 
        print 'getx'
        return self.__x
    
    def setx(self, v): 
        print 'setx'
        self.__x = v
    
    def delx(self): 
        print 'delx'
        del self.__x
        
    x = property(getx, setx, delx, "I'm the x property")

f = Third1()
f.bamf = 10
print f.bamf #"getting `bamf`" "10"
f.Kozel() #getting `Kozel` Third1::Kozel

f.x = "Oslik" #setx
print f.x #getting `x`   getx    getting `_Third1__x`

print "-"*20 + "Parts of an empty class" + "-"*20
'''
http://jfine-python-classes.readthedocs.org/en/latest/construct.html#the-empty-class
'''

class A(object):
    '''
    Kozel class
    '''
    pass

print A.__dict__
print sorted(A.__dict__.keys())
print A.__bases__
print A.__mro__
print A.__doc__

print "-"*20 + "dict_from_class(), exclude standard keys" + "-"*20
'''
http://jfine-python-classes.readthedocs.org/en/latest/construct.html#the-empty-class
http://www.python-course.eu/sets_frozensets.php
'''

class A(object):
    pass

_excluded_keys = set(A.__dict__.keys())
print _excluded_keys
print type(_excluded_keys)

def dict_from_class(cls):
    return dict((key, value) for (key, value) in cls.__dict__.items()
                             if key not in _excluded_keys)

class B(object):
    
    s = "a string"
    
    def Method(self):
        pass

print dict_from_class(A)
print dict_from_class(B)












