

# A binary tree is said to be balanced if for each node in the tree, the difference in the height
# of its left and right subtrees is at most one.

# Problem 9.1 Write a function that takes as input the root of a binary tree and returns true or 
# false depending of whether the tree is balanced. Use O(h) additional storage, where h is the 
# height of the tree.

# USEFUL LINKS:
# http://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

# https://stackoverflow.com/questions/2708914/how-to-add-add-node-in-binary-tree
# You traverse the binary tree from the root:

# - if your new element is less or equal than the current node, you go to the left subtree, 
#   otherwise to the right subtree and continue traversing

# - if you arrived at a node, where you can not go any deeper, because there is no subtree, 
#   this is the place to insert your new element

#               (5)Root
#      (3)-------^--------(7)
# (2)---^----(5)           ^-----(8)
#        (5)--^

# You start at (5), then go left (since 5 <= 5) to (3), then go right (since 5 > 3) to (5), 
# then you want to go to the left subtree (since 5 <= 5), but you see that there is no subtree, 
# so this is the place to insert your new element (5).

# Site with problems
# https://leetcode.com/problems/balanced-binary-tree/description/

import unittest


class Node:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

class Tree:
    
    def __init__(self):
        self.root = None

    def Add(self, value):
        if not self.root:
            self.root = Node(value)                 # Add root value if the tree is empty
        else:
            self.__Add(value, self.root)
    
    def GetRoot(self):
        return self.root
    
    def PrintTree(self):
        if (self.root != None):                     # ?`r "if self.root" is the same or not?
            self.__PrintTree(self.root)
    
    def __Add(self, value, node):
        
        if value < node.value:                      # Add to the left if value is smaller than node.value
            if (node.left != None):
                self.__Add(value, node.left)
            else:
                node.left = Node(value)
        
        else:                                       # Add to the right if value is larger than node.value
            if (node.right != None):
                self.__Add(value, node.right)
            else:
                node.right = Node(value)

    def __PrintTree(self, node):
        if(node != None):
            self.__PrintTree(node.left)             # Go to the left-most node (until the node.left is None)
            print str(node.value) + ' '             # Print current node
            self.__PrintTree(node.right)

    def GetHeight(self, node):
        if node == None: 
            return 0
        height = 1 + max(self.GetHeight(node.left), self.GetHeight(node.right))
        return height
    
    def IsBalancedNaive(self, node):
        if node == None: return True                 # empty subtree is balanced
        
        diff = abs(self.GetHeight(node.left) - self.GetHeight(node.right))
        if diff > 1:
            return False                             # subtree starting with the node isn't balanced
        else:
            # Check whether the subtrees are balanced
            return self.IsBalancedNaive(node.left) and self.IsBalancedNaive(node.right) 
        
    
class Ex09_01Test(unittest.TestCase):
    
    def test_TestTree(self):
             
        #     3
        # 0     4
        #   2      8
        
        tree = Tree()
        tree.Add(3)
        tree.Add(4)
        tree.Add(0)
        tree.Add(8)
        tree.Add(2)
        tree.PrintTree()                          # 0 2 3 4 8
        root = tree.GetRoot()                     # 3
        print(tree.GetHeight(root))               # True
        print(tree.IsBalancedNaive(root))
        
        
        #            3
        #          0   4
        #       -1   2   8
        #    -2
        
        tree.Add(-1)
        tree.Add(-2)
        tree.PrintTree()                          # -2 -1 0 2 3 4 8
        print(tree.GetHeight(root))               # 4
        print(tree.IsBalancedNaive(root))         # True
        
        #            3
        #          0   4
        #       -1   2   8
        #    -2
        # -3
        
        
        tree.Add(-3)
        tree.PrintTree()                          # -3 -2 -1 0 2 3 4 8
        print(tree.GetHeight(root))               # 5
        print(tree.IsBalancedNaive(root))         # False
        

if __name__ == "__main__":
    unittest.main()





