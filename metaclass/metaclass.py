
#http://jfine-python-classes.readthedocs.org/en/latest/construct.html
#http://stackoverflow.com/questions/22609272/python-typename-bases-dict
print "First----------------------------------------------------"

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
print "First----------------------------------------------------"

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


print 'TestName = ', repr(TestName)