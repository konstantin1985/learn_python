

# Define the number of bits that are set to 1 in an unsigned 64-bit integer x
# to be the weight of x. Let Sk denote the set of unsigned 64-bit integers
# whose weight is k

# Problem 5.4: Suppose x \in Sk and k is not 0 or 64.
# How would you compute y \in Sk \{x} such that |y-x| is minimum?

import unittest

def FindClosestElementSimple(val):

    if (val & 1) == 0:

        # Extract the LSB = 1
        lsb = val & ~(val - 1)

        val &= ~lsb
        val |= (lsb >> 1)

    else:
        # Extract the LSB = 0
        lsb = ~val & ~((~val) - 1)
        val |= lsb
        val &= ~(lsb >> 1)

    return val


def FindClosestElementBetter(val):
    # Correct algorithm is to flip 2 least significant bits that are different

    for i in range(63):
        if ((val >> i) & 1) ^ ((val >> (i + 1)) & 1):
            # Important XOR with 11..11 flips elements
            # 10 ^ 11 = 01
            val ^= (1 << i) | (1 << (i + 1))
            # Very important that we return value here and for loop is end
            return val

class Ex5_4Test(unittest.TestCase):

    def AuxiliaryFunction(self, f):
        self.assertEquals(f(0b0110), 0b0101)
        self.assertEquals(f(0b1000), 0b0100)
        self.assertEquals(f(0b0011), 0b0101)
        self.assertEquals(f(0b0111), 0b1011)
        self.assertEquals(f(0b1011100), 0b1011010)

    def test_FindClosestElementSimple(self):
        #self.AuxiliaryFunction(FindClosestElementSimple)
        self.AuxiliaryFunction(FindClosestElementBetter)


if __name__ == "__main__":
    unittest.main()