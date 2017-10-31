

# Problem 6.18: Implemented run-length encoding and decoding
# functions. Assume the string to be encoded consists of 
# letters of the alphabet, with no digits, and the string
# to be decoded is a valid encoding.

# RLE: 'aaaabcccaa' is '4a1b3c2a'
# Inverse: '3r4f2e' returns 'eeeffffee'

import unittest

def SimpleEncoding(stringToCode):
    
    if not stringToCode:
        return ''
    
    rv = ''
    k = 1   # counter within a group, IMPORTANT that it's 1, not 0 (see main loop)
    
    # So we can process the element before the last without problems
    stringToCode = stringToCode + '0'
    
    # Initial 'previous' element
    previous = stringToCode[0]
    
    for s in stringToCode[1:]:
        
        if s == previous:
            k += 1
        else:
            rv =  rv + str(k) + previous  # add previous element 
            previous = s
            k = 1
   
    return rv


def SimpleDecoding(stringToDecode):
    
    if not stringToDecode:
        return ''

    rv = ''
    
    # We use range(start, end, step)
    for i in range(0, len(stringToDecode), 2):
        num = int(stringToDecode[i])
        value = stringToDecode[i+1]
        rv = rv + value * num
    
    return rv


class Ex6_18Test(unittest.TestCase):
    
    def test_SimpleEncoding(self):
        self.assertEqual(SimpleEncoding(''), '')
        self.assertEqual(SimpleEncoding('a'), '1a')
        self.assertEqual(SimpleEncoding('aaaa'), '4a')
        self.assertEqual(SimpleEncoding('abb'), '1a2b')
        self.assertEqual(SimpleEncoding('aabb'), '2a2b')
        self.assertEqual(SimpleEncoding('aaaabcccaa'), '4a1b3c2a') 
        
    def test_SimpleDecoding(self):
        self.assertEqual(SimpleDecoding(''), '')
        self.assertEqual(SimpleDecoding('2a'), 'aa')
        self.assertEqual(SimpleDecoding('3a1b'), 'aaab')
        self.assertEqual(SimpleDecoding('3r4f2e'), 'rrrffffee')
    
if __name__ == '__main__':
    unittest.main()