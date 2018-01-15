

# Problem 5.7: Write a function that performs base conversion. Specifically, the
# input is an integer base b1, a string s, representing an integer x in base b1,
# and another integer base b2; the output is the string representing the integer
# x in base b2. Assume 2 \leq b1,b2 \leq 16. Use "A" to represent 10, "B" for 11,
# ..., and "F" for 15.

import unittest


def ConvertToDecimal(b,s):
    # From number as string 's' of base 'b' to decimal number
    
    assert (b <= 16) and (b >= 2)
    
    rv = 0
    for i, letter in enumerate(reversed(s)):
        
        if letter == 'A':
            val = 10
        elif letter == 'B':
            val = 11
        elif letter == 'C':
            val = 12
        elif letter == 'D':
            val = 13
        elif letter == 'E':
            val = 14
        elif letter == 'F':
            val = 15
        else:
            val = int(letter)
        
        rv += val * (b ** i)
        
    return rv

def ConvertFromDecimal(s,b):
    # From decimal 's', to number as string of base 'b'
    # http://www.permadi.com/tutorial/numDecToHex/

    assert (b <= 16) and (b >= 2)
    
    bNum = []  # list of numbers in 's' in system 'b'
    
    # FROM LOWEST to highest number in system b
    # The last element in bNum is MSB
    while s != 0:    
        bNum.append(s % b)
        s = s // b
    
    # Convert to string in system b
    rv = ''
    for num in reversed(bNum):

        if num == 10:
            letter = 'A'
        elif num == 11:
            letter = 'B'
        elif num == 12:
            letter = 'C'
        elif num == 13:
            letter = 'D'
        elif num == 14:
            letter = 'E'
        elif num == 15:
            letter = 'F'
        else:
            letter = str(num)
        
        rv += letter
    
    return rv   

def ConvertSimple(b1,s,b2):
    d = ConvertToDecimal(b1,s)
    rv = ConvertFromDecimal(d,b2)
    return rv


class Ex05_07(unittest.TestCase):
    
    def test_ConvertToDecimal(self):
        self.assertEqual(ConvertToDecimal(16,'B235CA1'), 186866849)
        self.assertEqual(ConvertToDecimal(8,'12462547'), 2778471)
        self.assertEqual(ConvertToDecimal(2,'1000101'), 69)
    
    def test_ConvertFromDecimal(self):
        self.assertEqual(ConvertFromDecimal(4268746,16), '4122CA')
        self.assertEqual(ConvertFromDecimal(522896,8), '1775220')
        self.assertEqual(ConvertFromDecimal(123,2), '1111011')
        
    def test_ConvertSimple(self):
        self.assertEqual(ConvertSimple(16,'AB14D3',8), '52612323')
        self.assertEqual(ConvertSimple(2,'100101101010',16), '96A')
    

if __name__ == "__main__":
    unittest.main()