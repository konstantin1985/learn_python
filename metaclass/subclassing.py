print "-"*20 + "subclassing int" + "-"*20
print type(True)
print bool.__bases__
print True + True #2


class MyBool(int):
    def __repr__(self):
        return "__repr__ MyBool: " + ['False', 'True'][self]
    
t = MyBool(1)
print repr(t)
print bool(2) == 1   #True
print MyBool(2) == 1 #False
print MyBool(2) == 2 #True

#http://www.rafekettler.com/magicmethods.html
class NewBool(int):
    
    def __new__(cls,value, v2):
        print "__new__"
        return int.__new__(cls, bool(value))
    
    def __init__(self, value, v2):
        print "__init__my"

y = NewBool(1, 2)

#Situation in c++
#http://stackoverflow.com/questions/15879533/base-derived-class-relationship
#http://www.cplusplus.com/forum/beginner/16914/

print int.__new__.__doc__ #T.__new__(S, ...) -> a new object with type S, a subtype of T














