

# Problem 12.3: Let s be an array of strings. Write a function which 
# finds a closest pair of equal entries. For example, if 
# s = ["All", "work", "and", "no", "play", "makes", "for", "no", " work",
# "no", "fun", "and", "no", "results"], then the second and third
# occurrences of "no" is the closest pair.

import unittest
from collections import namedtuple


def FindClosestSimple(items):
    
    dictionary = {}
    
    Word = namedtuple('Word', ['last', "min_d"])
    
    # [0] - last occurrence
    # [1] - current minimal distance
    
    for i, item in enumerate(items):
        
        if item in dictionary:
            m = min(i - dictionary[item].last, dictionary[item].min_d)            
            dictionary[item] = Word(i, m)
        else:
            dictionary[item] = Word(i, float("Inf"))
    
    # DEBUG:
    # for k in dictionary:
    #     print(k, ":", dictionary[k])
    
    # Find minimum length
    min_d = float("Inf")
    for k in dictionary:
        if dictionary[k].min_d < min_d:
            min_d = dictionary[k].min_d

    # Create a list of words with min_d distance
    # So we can handle the case when several words have the same
    # minimal distance
    rv = []
    # sorted() so the rv will have the same key order for unit tests
    for k in sorted(dictionary):
        if dictionary[k].min_d == min_d:
            rv.append(k)
    
    return min_d, rv


class Ex12_03Test(unittest.TestCase):
    
    def test_FindClosestSimple(self):
        s = ["All", "work", "and", "no", "play", "makes", 
             "for", "no", "work", "no", "fun", "and", 
             "no", "results"]
        self.assertEqual(FindClosestSimple(s), (2, ["no"]))
        
        # What I don't like in the test is that 
        s = ["all", "yes", "all", "yes"]
        self.assertEqual(FindClosestSimple(s), (2, ["all", "yes"]))


if __name__ == "__main__":
    unittest.main()