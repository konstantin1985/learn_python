

# Problem 5.3: Write a function that takes a 64-bit integer x and returns
# a 64-bit integer consisting of the bits of x in reverse order

import unittest


def SimpleBitReversal(val):
    # Also can do precomputing of the array
    rv = 0
    N = 64
    for i in range(64):
        currentBit = (val >> i) & 1
        rv |= (currentBit << (N - i -1))
    return rv

class Ex5_3Test(unittest.TestCase):

    def AuxiliaryFunction(self, f):
        self.assertEquals(SimpleBitReversal(1), 2 ** 63)
        self.assertEquals(SimpleBitReversal(0b11), 2 ** 63 + 2 ** 62)
        self.assertEquals(SimpleBitReversal(0b101), 2 ** 63 + 2 ** 61)
        self.assertEquals(SimpleBitReversal(2 ** 63), 1)
        self.assertEquals(SimpleBitReversal(2 ** 63 + 2 ** 62), 0b11)
        self.assertEquals(SimpleBitReversal(2 ** 63 + 2 ** 61), 0b101)

    def test_SimpleBitReversal(self):
        self.AuxiliaryFunction(SimpleBitReversal)

if __name__ == "__main__":
    unittest.main()

