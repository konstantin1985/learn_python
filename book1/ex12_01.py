

# A hash function has one hard requirement - two keys that are
# identical should yield the same hash code. This may seem obvious,
# but is easy to get wrong, e.g. by writing a hash function that is
# based on address rather than contents.

# Problem 12.1: Design a hash function that is suitable for words in a 
# dictionary


import unittest 


def CalculateSimpleHash(string):
    ORDER = 256  # the larger the better
    h = 0        # hash
    
    # Very import to have i here, so "kor" and "ork" give different values.
    # With i we account for the position of a letter.
    for i, s in enumerate(string):
        h = (h + i * ord(s)) % ORDER
    return h


class Ex12_01Test(unittest.TestCase):
    
    def test_SimpleHash(self):        
        self.assertEqual(CalculateSimpleHash("kor"), 83)
        self.assertEqual(CalculateSimpleHash("ork"), 72)
        self.assertEqual(CalculateSimpleHash("rok"), 69)
        self.assertEqual(CalculateSimpleHash("ab"), 98)
        self.assertEqual(CalculateSimpleHash("ba"), 97)
        

if __name__ == "__main__":
    unittest.main()