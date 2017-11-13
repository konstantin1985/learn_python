
# -14 0 2 108 108 243 285 285 285 401 (Fig 11.1)

# Problem 11.1: Write a method that takes a sorted array A and a key k
# and returns the index of the first occurrence of k in A. Return -1
# if k doesn't appear in A. For example, when applied to the array in
# Figure 11.1 your algorithm should return 3 if k = 108; if k=285, your
# algorithm should return 6

import unittest

# items is a sorted list
def FindSimple(items, k):
    
    U = len(items) - 1
    L = 0
    
    # Very important to have "<=" here
    while(L <= U):
    
        M = (U + L) // 2
                    
        if k > items[M]:
            # M position is already checked
            # Very important, otherwise we'll stuck sometimes 
            # For 3 elements M = (U + L) // 2 won't give 2
            L = M + 1        
        elif k == items[M]:
            break
        else:
            # M position is already checked
            U = M - 1
    else:
        return -1  # loop wasn't braked, so the element wasn't found
    
    # Additional small search    
    index = M
    while(index >= 0):
        if items[index] == items[M]: 
            index -= 1
        else:
            return index + 1
    return 0 


class Ex11_01Test(unittest.TestCase):
    
    def test_FindSimple(self):
        items = [10, 20, 30]
        self.assertEqual(FindSimple(items, 10), 0)
        self.assertEqual(FindSimple(items, 20), 1)
        self.assertEqual(FindSimple(items, 30), 2)
        self.assertEqual(FindSimple(items, 40), -1)
        
        items = [10, 20, 30, 40]
        self.assertEqual(FindSimple(items, 30), 2)
    
    def test_FindSimpleMultiple(self):
        items = [-14, 0, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(FindSimple(items, -14), 0)
        self.assertEqual(FindSimple(items, 2), 2)
        self.assertEqual(FindSimple(items, 108), 3)
        self.assertEqual(FindSimple(items, 285), 6)
        
    
if __name__ == "__main__":
    unittest.main()
    
    