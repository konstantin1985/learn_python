

# Problem 12.3: Let s be an array of strings. Write a function which 
# finds a closest pair of equal entries. For example, if 
# s = ["All", "work", "and", "no", "play", "makes", "for", "no", " work",
# "no", "fun", "and", "no", "results"], then the second and third
# occurrences of "no" is the closest pair.

import unittest
from collections import namedtuple

Rec = namedtuple('Rec123', ['name', 'age', 'jobs'])


def FindClosestSimple(items):
    
    dictionary = {}
    
    # Word = namedtuple('Word', ['last', "min_d"])
    
    # [0] - last occurrence
    # [1] - current minimal distance
    
    for i, item in enumerate(items):
        
        if item in dictionary:
            m = min(i - dictionary[item][0], dictionary[item][1])            
            dictionary[item] = (i, m)
        else:
            dictionary[item] = (i, float("Inf"))
    
    for k in dictionary:
        print(k, ":", dictionary[k])
    


class Ex12_03Test(unittest.TestCase):
    
    def test_FindClosestSimple(self):
        s = ["All", "work", "and", "no", "play", "makes", 
             "for", "no", "work", "no", "fun", "and", 
             "no", "results"]
        FindClosestSimple(s)
        pass
    

if __name__ == "__main__":
    unittest.main()