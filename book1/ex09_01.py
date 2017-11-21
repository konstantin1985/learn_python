

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
            self.root = Node(value)
        else:
            self.__Add(value, self.root)
    
    def GetRoot(self):
        return self.root
    
    def PrintTree(self):
        if (self.root != None):                     # ?`r "if self.root" is the same or not?
            self.__PrintTree(self.root)
    
    def GetHeight(self):
        pass
    
    def __Add(self, value, node):
        
        if value < node.value:                      # Add to the left if value is less than node.value
            if (node.left != None):
                self.__Add(value, node.left)
            else:
                node.left = Node(value)
        
        else:                                       # Add to the right if value is more than node.value
            if (node.right != None):
                self.__Add(value, node.right)
            else:
                node.right = Node(value)

    def __PrintTree(self, node):
        if(node != None):
            self.__PrintTree(node.left)             # Go to the left-most node (until the node.left is None)
            print str(node.value) + ' '             # Print current node
            self.__PrintTree(node.right)


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
        tree.PrintTree()  # 0 2 3 4 8
        
        pass


if __name__ == "__main__":
    unittest.main()




'''
class TreeNode:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

class Tree:
    def __init__(self):
        self.root = None;

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value);
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value);
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value);

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

def main():
    testTree = Tree()
    testTree.addNode(testTree.root, 200)
    testTree.addNode(testTree.root, 300)
    testTree.addNode(testTree.root, 100)
    testTree.addNode(testTree.root, 30)
    testTree.printInorder(testTree.root)

# main()



class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
# print (tree.find(3)).v
# print tree.find(10)
# tree.deleteTree()
# tree.printTree()
'''
    
    
'''    
or each node of the tree, get the height of left sub­tree and right sub­tree and check the dif­fer­ence , if it is greater than 1, return false.

public static int getHeight(Node root){
        if(root==null)return 0;
        return (1+ Math.max(getHeight(root.left), getHeight(root.right)));
    }
    public static boolean isBalancedNaive(Node root){
        if(root==null)return true;
        int heightdifference = getHeight(root.left)-getHeight(root.right);
        if(Math.abs(heightdifference)>1){
            return false;
        }else{
            return isBalancedNaive(root.left) && isBalancedNaive(root.right);
        }
    }
'''


