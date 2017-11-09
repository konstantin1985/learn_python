# Find parity for a large number of unsigned integers

import unittest

def RightShift(val,pos):
    return val >> pos

def SimpleParity(val):
    parity = 0
    while (val):
        # If LSB = 1 then flip parity value
        parity ^= val & 1
        val = RightShift(val,1)
    return parity

def LessSimpleParity(val):
    parity = 0
    while (val):
        parity ^= 1
        val &= (val-1)
    return parity

# Store values in memory
l16 = []
def FillList():
    for i in range (2**16):
        l16.append(SimpleParity(i))

def CalculateParityWithMemory(val):
    
    parity = l16[RightShift(val,48)]^\
             l16[RightShift(val,32) & 0xFFFF]^\
             l16[RightShift(val,16) & 0xFFFF]^\
             l16[val & 0xFFFF]
    return parity

class Ex5_1Test(unittest.TestCase):
    
    def AuxiliaryFunction(self, f):
        self.assertEqual(f(0),0)
        self.assertEqual(f(1),1)
        self.assertEqual(f(1),1)
        self.assertEqual(f(7),1)
        self.assertEqual(f(230),1)
        self.assertEqual(f(547),0)
        self.assertEqual(f(10486307),0)
        self.assertEqual(f(10486306),1)
    
    def test_RightShiftTest(self):
        self.assertEqual(RightShift(1000,0),1000)
        self.assertEqual(RightShift(1000,3),125)
        self.assertEqual(RightShift(1,48),0)
        self.assertEqual(RightShift(1,32),0)
        self.assertEqual(RightShift(1,16),0)
        self.assertEqual(RightShift(0,3),0)
    
    def test_SimpleParityTest(self):
        self.AuxiliaryFunction(SimpleParity)
        
    def test_LessSimpleParity(self):
        self.AuxiliaryFunction(LessSimpleParity)
    
    def test_CalculateParityWithMemory(self):
        FillList()
        self.AuxiliaryFunction(CalculateParityWithMemory)
    
if __name__ == '__main__':
    unittest.main()
