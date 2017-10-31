

# Problem 7.1: Write a function that takes linked lists L and F and returns
# the merge of L and F. Your code should use O(1) additional storage
# it should reuse the nodes from the lists provided as input.
# Your function should use 0(1) additional storage. The only field you
# can change in a node is next.

# Last reference in a LL is None

import copy


class Node:
    
    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
    def __str__(self):
        return str(self.value)
    
    def GetValue(self):
        return self.value
    
    def GetNext(self):
        return self.nextNode
    
    def SetNext(self, nextNode = None):
        self.nextNode = nextNode


def Display(lst, rv):
    if lst:
        rv.append(lst.GetValue())
        Display(lst.GetNext(), rv)  # Call next node
    

def SimpleMerge(L1, L2):
    # Function changes L1
    
    # Deep copy L2 so it's not changed for the outside caller
    L2 = copy.deepcopy(L2)
    
    # If the first element of L2 is less than the first element of L1
    # Then simply switch labels of L1 and L2
    if L1.GetValue() > L2.GetValue():
        L1, L2 = L2, L1

    # Keep the pointer to the first element in L1
    # so we may return it  
    firstL1 = L1
    
    # Main logic
    while L1 or L2:
        
        # No more elements in L2, the rest of L1 is correct
        if not L2:
            break
        
        # No more elements in L1 and L2 isn't empty.
        # Add all remaining nodes from L2 to L1
        if not L1.GetNext() and L2:
            L1.SetNext(L2)
            break
        
        # Next L1 is bigger than current L1
        # Get current L2 and add it to L1 instead of the last L1
        # Last L1 add to the end of L1
        if L1.GetNext().GetValue() > L2.GetValue():
            temp = L1.GetNext()           
            L1.SetNext(L2)   
            # Very important to set L2 here and not after playing with L1
            # because L2 sits in L1->next, so it will be otherwise overridden 
            L2 = L2.GetNext()
            L1.GetNext().SetNext(temp)
        
        L1 = L1.GetNext()

    return firstL1
            
import unittest


class Ex7_1Test(unittest.TestCase):
    
    def test_DisplayFunction(self):
        n1 = Node(value = 10)
        n2 = Node(value = 20)
        n3 = Node(value = 30)
        n4 = Node(value = 40)
        n1.SetNext(n2)
        n2.SetNext(n3)
        n3.SetNext(n4)
        rv = []
        Display(n1, rv)
        self.assertEqual(rv, [10, 20, 30, 40])
    
    def test_SimpleMerge(self):
        
        n1 = Node(value = 1)
        n2 = Node(value = 3)
        n3 = Node(value = 7)
        n1.SetNext(n2)
        n2.SetNext(n3)
        
        p1 = Node(value = 3)
        p2 = Node(value = 6)
        p3 = Node(value = 7)
        p1.SetNext(p2)
        p2.SetNext(p3)
        
        m1 = Node(value = 2)
        m2 = Node(value = 4)
        m3 = Node(value = 5)
        m4 = Node(value = 9)
        m1.SetNext(m2)
        m2.SetNext(m3)
        m3.SetNext(m4)
        
        merged = SimpleMerge(n1, m1)
        rv = []
        Display(merged, rv)
        self.assertEqual(rv, [1, 2, 3, 4, 5, 7, 9])
        
        merged = SimpleMerge(p1, m1)
        rv = []
        Display(merged, rv)
        self.assertEqual(rv, [2, 3, 4, 5, 6, 7, 9])
        
    
if __name__ == "__main__":
    unittest.main()
