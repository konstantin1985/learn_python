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
        



print "-"*20 + "1" + "-"*20
