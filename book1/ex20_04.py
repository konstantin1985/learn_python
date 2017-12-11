# 20.4 Uniform random number generation

# Five friends have to select a designated driver using a single
# unbiased coin. The process should be fair to everyone.

# Problem 20.4: How would you implement a random number
# generator that generates a random integer i in [a,b], given
# a random number generator that produces either 0 or 1 with
# equal probability? All generated values should have equal
# probability. What is the run time of your algorithm, assuming
# each call to the given random number generator takes O(1) time?

# a = 1, b = 3

# 00
# 01
# 10

# 00
# 01
# 10
# 11

import unittest
from random import randint
import math

# return randint(a,b)

def SimpleGenerator(a,b):
    
    assert a < b
    
    # Shift a and b so we generate a random number starting from 0
    shift = a
    a = 0
    b = b - shift
    
    # Number of bits in b (b = 3 -> Nbits = 2; b = 2 -> Nbits = 2)
    Nbits = int(math.log(b, 2)) + 1
    
    while True:
        rv = 0
        for i in range(Nbits):
            rv |= randint(0, 1) << i
        
        # Number can be bigger than b, so simply discard this number and get another
        if rv <= b: break
    
    # Shift back to the [a,b] range
    rv = rv + shift
    
    return rv


class Ex20_04(unittest.TestCase):
        
    def test_SimpleGeneratorFromZero(self):
        
        a,b = 0,3
        
        # Create dictionary with zero values
        d = dict.fromkeys(range(a, b + 1), 0)
        
        # Generate a lot of random numbers and fill the dictionary
        # with how many times they occurred
        for _ in range(100000):
            v = SimpleGenerator(a, b)
            d[v] = d[v] + 1
        
        print(d)
        
        for key in d:
            self.assertAlmostEqual(d[key], 25000, delta = 25000 * 0.02)

    def test_SimpleGeneratorFromNonZero(self):
        
        a,b = 10,14
        
        # Create dictionary with zero values
        d = dict.fromkeys(range(a, b + 1), 0)
        
        # Generate a lot of random numbers and fill the dictionary
        # with how many times they occurred
        for _ in range(100000):
            v = SimpleGenerator(a, b)
            d[v] = d[v] + 1
        
        print(d)
        
        for key in d:
            self.assertAlmostEqual(d[key], 20000, delta = 25000 * 0.02)
    

if __name__ == "__main__":
    unittest.main()