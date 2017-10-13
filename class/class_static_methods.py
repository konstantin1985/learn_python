class Test:
    #regular instance method:
    def MyMethod(self):
        print "MyMethod"
    #class method:
    @classmethod
    def MyClassMethod(cl):
        print "MyClassMethod"
    #static method:
    @staticmethod
    def MyStaticMethod():
        print "MyStaticMethod"
    
    
t = Test()
t.MyMethod()
t.MyClassMethod()
t.MyStaticMethod()

#Test.MyMethod()
Test.MyClassMethod() #MyClassMethod
Test.MyStaticMethod() #MyStaticMethod

MyStaticMethod()

print "Oslik"