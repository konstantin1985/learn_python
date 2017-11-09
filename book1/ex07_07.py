# Deletion from a singly linked list

# Given a node in a singly LL, deleting it in O(1) appears impossible
# because its predecessor's next field has to be updated. Surprisingly,
# it can be done with one small caveat - the node to delete cannot be the
# last one in the list and it is easy to copy the value part of a node

# Problem 7.7.: Let v be a node in a singly linked list L. 
# Node v is not the tail delete it in O(1) time.

import unittest


class Node:
    
    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
    def GetValue(self):
        return self.value
    
    def SetValue(self, value):
        self.value = value 
    
    def GetNext(self):
        return self.nextNode
    
    def SetNext(self, nextNode):
        self.nextNode = nextNode


def Display(lst, rv):

    if lst:
        rv.append(lst.GetValue())
        Display(lst.GetNext(), rv)


def SimpleRemove(node):
    
    if not node.GetNext():
        print "Can't delete last element"
        return

    node.SetValue(node.GetNext().GetValue())
    node.SetNext(node.GetNext().GetNext())
    

class Ex7_7Test(unittest.TestCase):
    
    def test_SimpleDelete(self):
        n1 = Node(value = 1)
        n2 = Node(value = 3)
        n3 = Node(value = 7)
        n4 = Node(value = 15)
        n1.SetNext(n2)
        n2.SetNext(n3)
        n3.SetNext(n4)
        SimpleRemove(n3)
        rv = []
        Display(n1, rv)
        self.assertEqual(rv, [1, 3, 15])


if __name__ == "__main__":
    unittest.main()
    