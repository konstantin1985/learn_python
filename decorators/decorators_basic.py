
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

print "--------------4---------------------"


















