

# Offline sampling

# Problem 20.2: Let A be an array of n distinct elements. Design an algorithm
# that returns a subset of k elements of A. All subsets should be equally likely.
# Use as few calls to the random number generator as possible and use O(1)
# additional storage. You can return the result in the same array as input.

import unittest

from random import randint

def Sampling(a, k):
    
    n = len(a)
    assert k < n
    
    for i in range(k):
        
        # Select from the left part of the array
        # The left part is getting smaller on each step
        index = randint(0,n-i-1)                             # 0 \leq index \LEQ n-i-1
        
        # Swap the selected element (index) with 
        # rightmost element in the left part of the array
        temp = a[n-i-1]
        a[n-i-1] = a[index]
        a[index] = temp
    
    # Return the rightmost k from the array a where the
    # random elements reside
    return a[-k:] 


class Ex20_02(unittest.TestCase):
    
    def test_SimpleSampling(self):
        
        a = ['a', 'c', 'd', 'e', 'f']
        rv = Sampling(a, 1)
        print(rv)
        rv = Sampling(a, 2)
        print(rv)
        rv = Sampling(a, 3)
        print(rv)

if __name__ == '__main__':
    unittest.main()