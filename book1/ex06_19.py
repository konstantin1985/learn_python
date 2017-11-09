

# Problem 6.19: Implement a function for reversing the words
# in a string. Your function should use O(1) space.

# Alice likes Bob -> Bob likes Alice

import unittest


def ReverseSimple(stringToReverse):
    
    words = stringToReverse.split()
    return ' '.join(reversed(words))


# Need a solution in O(1) space
# May be get a word and then shift it to the beginning of the string?


class Ex6_19Test(unittest.TestCase):
    
    def test_ReverseSimple(self):
        self.assertEqual(ReverseSimple('Word'), 'Word')
        self.assertEqual(ReverseSimple('Alice likes Bob'), 'Bob likes Alice')


if __name__ == "__main__":
    unittest.main()