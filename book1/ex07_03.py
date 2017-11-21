

# It is relatively straightforward to find the median of a sorted linked list
# in O(n) time. However, this problem becomes trickier if the list is circular.

# Problem 7.3  Write a function that takes a sorted circular singly linked 
# list and a pointer to an arbitrary node in the list, and returns the median 
# of the linked list.

import unittest

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
        

def FindMedian(lst):
    
    first = lst
    current = lst.GetNext()
    minCell = lst
    
    # Count number of elements in the loop and
    # find the cell with the minimum value
    count = 1    
    while first is not current:
        # Important to have it before the "current.GetNext()"
        # because "current = lst.GetNext()" already
        if minCell.GetValue() > current.GetValue():
            minCell = current
            
        current = current.GetNext()
        count += 1

    # We need to traverse half of the cells starting
    # from the minCell to get a median value    
    count = count // 2
    current = minCell
    
    for _ in range(count):
        current = current.GetNext()
    
    # Return median value
    return current

class Ex07_03Test(unittest.TestCase):
    
    def test_FindMedianOdd(self):
        n1 = Node(value = 10)
        n2 = Node(value = 20)
        n3 = Node(value = 30)
        n4 = Node(value = 40)
        n5 = Node(value = 50)
        n1.SetNext(n2)
        n2.SetNext(n3)
        n3.SetNext(n4)
        n4.SetNext(n5)
        n5.SetNext(n1)
        self.assertEqual(FindMedian(n1), n3)
        self.assertEqual(FindMedian(n2), n3)
        self.assertEqual(FindMedian(n3), n3)
        self.assertEqual(FindMedian(n4), n3)
        self.assertEqual(FindMedian(n5), n3)
        
    def test_FindMedianEven(self):
        n1 = Node(value = 10)
        n2 = Node(value = 20)
        n3 = Node(value = 30)
        n4 = Node(value = 40)
        n1.SetNext(n2)
        n2.SetNext(n3)
        n3.SetNext(n4)
        n4.SetNext(n1)
        
        # May add functionality to distinguish between
        # even and odd number of nodes and if even then
        # return two cells
        self.assertEqual(FindMedian(n1), n3)
        self.assertEqual(FindMedian(n2), n3)
        self.assertEqual(FindMedian(n3), n3)
        self.assertEqual(FindMedian(n4), n3)
        
    
if __name__ == "__main__":
    unittest.main()