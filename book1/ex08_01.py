
# Problem 8.1: Design a stack that supports a max operation, which returns 
# the maximum value stored in the stack, and throws an exception if the stack is empty. 
# Assume elements are comparable. All operations must be O(1) time. 
# You can use O(n) additional space, beyond what is required for the elements themselves.



import unittest


class SimpleStack:
    # max in O(n), not in O(1)
    
    def __init__(self):
        self.st = []
    
    def Push(self, a):
        self.st.append(a)
    
    def Pop(self):
        return self.st.pop()
    
    def Max(self):
        
        if self.IsEmpty(): raise BaseException 
        
        maxst = float("-inf")
        temp = []
        
        while not self.IsEmpty():
            a = self.Pop()
            if a > maxst: maxst = a
            temp.append(a)
        
        # While temp is non-empty
        while temp:
            a = temp.pop()
            self.Push(a)
        
        return maxst

    def Top(self):
        return self.st[-1]
    
    def IsEmpty(self):
        # if the list isn't empty then return true
        # also can do bool(self.st)
        return not self.st    


class StackO_1:
    # Stack with all operations in O(1) time
    # https://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1

    def __init__(self):
        self.st = []
        # Stack with max elements (!), it runs in parallel with the main one
        # On certain element stack with max elements has max element for the
        # main stack below certain element
        self.maxst = []
        
        # Real stack        Max stack

        # 5  --> TOP        6
        # 1                 6
        # 6                 6
        # 4                 4
        # 2                 2

    def Push(self, a):
        
        # When the stack is empty, currentMax is "-inf" 
        if self.IsEmpty():
            currentMax = float("-inf")
        else:
            currentMax = self.maxst[-1]
        
        # Push to the stack with max elements either old (currentMax) or new maximum (a)
        if a > currentMax:
            self.maxst.append(a)
        else:
            self.maxst.append(currentMax)
        
        # Push the element to the real stack
        self.st.append(a)
        
    def Pop(self):
        self.maxst.pop()
        return self.st.pop()
    
    def Max(self):
        if self.IsEmpty(): raise BaseException 
        return self.maxst[-1]
    
    def Top(self):
        return self.st[-1]
    
    def IsEmpty(self):
        return not self.st

    def Print(self):
    # Just a debug information
        pass

class Ex8_1Test(unittest.TestCase):
    
    def Operations(self, stack):
        s = stack()
        s.Push(5)
        s.Push(10) 
        s.Push(3)
        self.assertEqual(s.IsEmpty(), False);
        self.assertEqual(s.Pop(), 3);
        self.assertEqual(s.Pop(), 10);
        self.assertEqual(s.Top(), 5);
        self.assertEqual(s.Pop(), 5);
        self.assertEqual(s.IsEmpty(), True);
    
    def Max(self, stack):
        s = stack()       
        s.Push(5); s.Push(10); s.Push(3); s.Push(9)
        self.assertEqual(s.Max(), 10);
        self.assertEqual(s.Pop(), 9);
        self.assertEqual(s.Pop(), 3);
        self.assertEqual(s.Pop(), 10);
        self.assertEqual(s.Pop(), 5);
        self.assertEqual(s.IsEmpty(), True);
        self.assertRaises(BaseException, s.Max)  # important how we handle raise exceptions
    
    def test_SimpleStack(self):
        self.Operations(SimpleStack)
        self.Max(SimpleStack)
        
    def test_StackO_1(self):
        self.Operations(StackO_1)
        self.Max(StackO_1)

        
if __name__ == "__main__":
    unittest.main()
