print "-"*20 + "1" + "-"*20 

class A(object):
    def method(*argv):
        return argv

a = A()
print a.method                   #<bound method A.method of <A object at 0x...>>
print a.method('an arg')         #(<A object at 0x...>, 'an arg'), - first argument for bound method is instance
print a.method('an arg')[0] is a #True

print "-"*20 + "@staticmethod" + "-"*20 

class A(object):
    @staticmethod
    def method(*argv):
        return argv

a = A()
print a.method                   #<function method at 0xb72f59cc>
print a.method('an arg')         #('an arg',) - no instance
print a.method('an arg')[0] is A #False
print a.method('an arg')[0] is a #False
print A.method                   #<function method at 0xb73719cc>
print A.method('an arg')         #('an arg',)

print "-"*20 + "@classmethod" + "-"*20

class A(object):
    @classmethod
    def method(*argv):
        return argv

a = A()
print a.method                   #<bound method type.method of <class '__main__.A'>> - bound method of class
print a.method('an arg')         #(<class '__main__.A'>, 'an arg') - class as a first argument
print a.method('an arg')[0] is A #True
print a.method('an arg')[0] is a #False
print A.method                   #<bound method type.method of <class '__main__.A'>> - bound method of class
print A.method('an arg')         #(<class '__main__.A'>, 'an arg')

print "-"*20 + "call() decorator" + "-"*20

def call(*argv, **kwargs):
    def call_fn(fn):
        return fn(*argv, **kwargs)
    return call_fn

@call(5)
def table(n):
    value = []
    for i in range(n):
        value.append(i*i)
    return value

print len(table)
print table
