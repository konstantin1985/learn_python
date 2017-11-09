
#x & (x-1) = x with the LSB cleared
#x &!(x-1) = extracts the lowest set bit of x (all other bits are cleared)
#x + (x >> 1) = binary reflected Gray code for x
#Program takes 64 bit integer and swaps bit at i and j positions

import unittest

def BitSwapSimple(val, i, j):
    
    bit_i = (val >> i) & 1
    bit_j = (val >> j) & 1
    
    if bit_i == 1:
        val |= (1 << j) 
    else:
        val &= ~(1 << j)
    
    if bit_j == 1:
        val |= (1 << i)
    else:
        val &= ~(1 << i)
    
    return val 

def BitSwapBetter(val, i, j):
    
    '''
    xor operation with 1 inverse bit
    00 0
    01 1 !
    10 1
    11 0 !
    '''
    
    # Check that bits in i and j aren't equal
    if ((val >> i) & 1) != ((val >> j) & 1):
        # Flip bits
        val ^= (1 << i) | (1 << j)
        
    pass

'''
Less clear way to do it
https://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit
Changing the nth bit to x
Setting the nth bit to either 1 or 0 can be achieved with the following:
number ^= (-x ^ number) & (1 << n);
Bit n will be set if x is 1, and cleared if x is 0.
'''

class Ex5_2Test(unittest.TestCase):

    def AuxiliaryFunction(self, f):
        self.assertEqual(f(5,0,1),6)
        self.assertEqual(f(5,1,0),6)
        self.assertEqual(f(5,1,2),3)
        self.assertEqual(f(5,2,1),3)
        self.assertEqual(f(5,0,2),5)
        self.assertEqual(f(5,2,0),5)
    
    def test_BitSwapSimple(self):
        self.AuxiliaryFunction(BitSwapSimple)
    
    def BitSwapBetter(self):
        self.AuxiliaryFunction(BitSwapBetter)

if __name__ == "__main__":
    unittest.main()