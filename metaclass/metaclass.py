
#http://jfine-python-classes.readthedocs.org/en/latest/construct.html
#http://stackoverflow.com/questions/22609272/python-typename-bases-dict

print "-"*20 + "1" + "-"*20

class A(object):
    '''
    Kozel, Osel
    Barashek
    :param mac: MAC-address
    '''
    pass

print A.__dict__.keys()
print A.__doc__

#http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
print "-"*20 + "2" + "-"*20

def test_metaclass(name, bases, dict):
    print 'The Class Name is', name
    print 'The Class Bases are', bases
    print 'The dict has', len(dict), 'elems, the keys are', dict.keys()

    return "yellow"

class TestName(object, None, int, 1):
    __metaclass__ = test_metaclass
    foo = 1
    def baz(self, arr):
        pass

#print 'TestName = ', repr(TestName)


print "-"*20 + "3" + "-"*20

def substitute_init(self, id, *args, **kwargs):
    print "substitute_init"
    
def kozel_fcn(self, a):
    print "kozel_fcn + " + a 
    
class FooMeta(type):

    def __new__(cls, name, bases, attrs):
        attrs['__init__'] = substitute_init
        attrs['kozel'] = kozel_fcn
        return super(FooMeta, cls).__new__(cls, name, bases, attrs)

class Foo(object):

    __metaclass__ = FooMeta

    def __init__(self, value1):
        pass

a = Foo("kozlik")
a.kozel("a")








