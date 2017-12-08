# k-balanced nodes

# Define a node in a binary tree to be k-balanced if the difference in the number of
# nodes in its left and right subtrees is no more than k.

# Problem 9.2: Design an algorithm that takes as input a binary tree and positive
# integer k, and returns a node u in the binary tree such that u is not k-balanced, 
# but all of u's descendants are k-balanced. If no such node exists, return null.

import unittest

class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    
    def __init__(self):
        self.root = None
    
    def GetRoot(self):
        return self.root
    
    def Add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__Add(value, self.root)
    
    def PrintTree(self):
        if self.root != None:
            self.__PrintTree(self.root)
        print('')
        
    def __Add(self, value, node):
        
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.__Add(value, node.left)    
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self.__Add(value, node.right)
                
    def __PrintTree(self, node):
        if node != None:
            self.__PrintTree(node.left)
            print(node.value),
            self.__PrintTree(node.right)
        
    def GetNumberOfSubnodes(self, node):
        '''
        How many nodes are below this one
        '''
        if node != None:
            return self.__GetNumberOfSubnodes(node, 0)
        else:
            return 0
            
    def __GetNumberOfSubnodes(self, node, num):
        if node != None:
            num = self.__GetNumberOfSubnodes(node.left, num)
            num += 1
            num = self.__GetNumberOfSubnodes(node.right, num)
        return num
        
    def GetNotKBalancedNode(self, k):
        assert k > 0
        return self.__GetNotKBalancedNode(k, self.root)
    
    def __GetNotKBalancedNode(self, k, node):
        '''
        Traverse tree as we do for printing: from left to right
        '''
        if node != None:
            rv = self.__GetNotKBalancedNode(k, node.left)
            if rv != None: return rv
                   
            L = self.GetNumberOfSubnodes(node.left)
            R = self.GetNumberOfSubnodes(node.right)
            
            # Debug info
            # print("node.value:", node.value)
            # print("L:", L)
            # print("R:", R)
            
            if abs(L - R) > k:
                return node.value
        
            rv = self.__GetNotKBalancedNode(k, node.right)
            if rv != None: return rv
       
class Ex09_02(unittest.TestCase):
    
    
    
    def test_GetNotBalancedSimpleLeft(self):
        
        #        0
        #     -1   1
        #  -2
        #     -1.5
        #  -1.8   -1.3 
        
        t = Tree()
        t.Add(0)
        t.Add(1)
        t.Add(-1)
        t.Add(-2)
        t.Add(-1.5)
        t.Add(-1.8)
        t.Add(-1.3)
        self.assertEqual(t.GetNotKBalancedNode(3), -1)

    def test_GetNotBalancedSimpleRight(self):
        
        #        0
        #     -1   1
        #            2
        #         1.5
        #      1.3   1.8
        
        t = Tree()
        t.Add(0)
        t.Add(-1)
        t.Add(1)
        t.Add(2)
        t.Add(1.5)
        t.Add(1.8)
        t.Add(1.3)
        
        # Here we have an error, because 1 isn't balanced as well
        self.assertEqual(t.GetNotKBalancedNode(3), 0)
    

if __name__ == "__main__":
    unittest.main()
    
    