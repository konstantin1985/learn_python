
'''
Clearest explanation of decorators:
http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484
'''

print "--------------1---------------------"
#Function can return another function

def Do(what):
    
    def Kozel():
        print "Kozel"
    
    def Osel():
        print "Osel"
    
    if what == "k":
        return Kozel
    elif what == "o":
        return Osel
    else:
        raise ValueError()

Do = Do("k")
Do()


print "--------------2---------------------"
#Basic decorator

def PrintKozel():
    print "Kozel"

def BD(fcn):
    
    def Wrapper():
        print "Before"
        fcn()
        print "After"
    
    return Wrapper    
    
PrintKozel = BD(PrintKozel)
PrintKozel()

print "--------------3---------------------"
#Python decoration

@BD
@BD
def PrintOsel():
    print "Osel"

PrintOsel()

print "-"*20 + "call decorator" + "-"*20


def call(*argv, **kwargs):
    print repr(argv)
    print repr(kwargs)
    def call_fn(fn):
        return fn(*argv, **kwargs)
    return call_fn

@call(5)
def table(n):
    value = []
    for i in range(n):
        value.append(i*i)
    return value


#table = call(5)(table)
print table















