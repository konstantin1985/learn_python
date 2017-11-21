
# Although a linked list is supposed to be a sequence of nodes ending in 
# a null, it is possible to create a cycle in a linked list by making the
# next field of an element reference to one of the earlier nodes.

# Problem 7.2: Checking for cyclicity
# Given a reference to the head of a singly linked list L, how would you
# determine whether L ends in a null or reaches a cycle of nodes?
# Write a function that returns null if there doesn't exist a cycle, and
# the reference to the start of the cycle is a cycle is present 
# (You do not know the length of the list in advance)

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


def Display(lst, rv):
    if lst:
        rv.append(lst.GetValue())
        Display(lst.GetNext(), rv)

def FloydAlgorithm(lst):
    
    first = lst

    # 1. Find Cyclic or not
    
    # Hare moves 2 cell a time
    # Tortoise moves 1 cell a time
    # If there is a cycle, hare and tortoise will meet on the cycle
    
    hare = first
    tortoise = first
    
    while True:
        
        try:             # So there is no problem if we invoke null pointer
            hare = hare.GetNext().GetNext()
        except:
            return None  # There is no cycle, so return None
        tortoise = tortoise.GetNext()
        
        if hare is tortoise:
            break        # Loop found
     
    # 2. If Cyclic - find the start of the cycle
    
    # Hare starts from the beginning with the slow speed
    # Tortoise continue with the slow speed
    # Cell where they met is the beginning of the loop
    
    hare = first
    while (hare is not tortoise):
        hare = hare.GetNext()
        tortoise = tortoise.GetNext()
    
    return hare  # hare and tortoise are the same here
    

class Ex07_02Test(unittest.TestCase):
    
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
    
    def test_FloydCycle(self):
 
        # Simply check one element of LL
        n1 = Node(value = 10)
        node = FloydAlgorithm(n1)
        self.assertIsNone(node)
        
        # Check LL without cycles
        n2 = Node(value = 20)
        n3 = Node(value = 30)
        n4 = Node(value = 40)
        n5 = Node(value = 40)
        n1.SetNext(n2)
        n2.SetNext(n3)
        n3.SetNext(n4)
        n4.SetNext(n5)
        node = FloydAlgorithm(n1)
        self.assertIsNone(node)
        
        # Add a cycle to LL
        n5.SetNext(n3)
        node = FloydAlgorithm(n1)
        self.assertEqual(node, n3)
    
    
if __name__ == "__main__":
    unittest.main()