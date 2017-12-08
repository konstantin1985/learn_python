

# 13.5 Intersect two sorted arrays

# A natural implementation for a search engine is to retrieve 
# documents that match the set of words in a query by maintaining
# an inverted index. Each page is assigned an integer identifier,
# its document-ID. An inverted index is a mapping that takes a word
# w and returns a sorted array of page-ids which contain w - the sort
# order could be, for example, the page rank in descending order.
# When a query contains contains multiple words, the search engine
# finds the sorted array for each word and then computes the
# intersection of these arrays - these are the pages containing all the 
# words in the query. The most computationally intensive step of 
# doing this is finding the intersection of the sorted array.

# Problem 13.5: Given sorted arrays A and B of lengths n and m
# respectively, return an array C containing elements common to A and B.
# The array C should be free of duplicates. How would you perform this
# intersection if (1.) n \almost\eq m (2.) n \much\less m

import unittest


def UnionSameLength(a, b):
    
    c = []
    ai, bi = 0, 0
    n, m = len(a), len(b)
    
    # != n and !=m, not n-1 and m-1, because the last element should
    # also be checked
    while (ai != n) and (bi != m):  
                
        if a[ai] == b[bi]:
            # print("Case 1: ",ai,a[ai],bi,b[bi])
            c.append(a[ai])
            ai += 1
            bi += 1
        
        elif a[ai] > b[bi]:
            # print("Case 2: ",ai,a[ai],bi,b[bi])
            bi += 1
        
        elif a[ai] < b[bi]:
            # print("Case 3: ",ai,a[ai],bi,b[bi])
            ai += 1
    
    return c
        

def UnionLessLength(a, b):
    # n is much less m
    # Binary search code is here:
    # https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
    
    c = []
    n, m = len(a), len(b) 

    for x in a:

        # Binary search in a bigger array
        lo, hi = 0, m
        
        while lo < hi:  
            
            mid = (hi+lo)//2
            
            if b[mid] < x:          
                lo = mid + 1  # Very important + 1 here 
            
            elif b[mid] > x:
                hi = mid
            
            else:
                c.append(x)
                break
    
    return c

        
class Ex13_05test(unittest.TestCase):
    
    def test_UnionSameLength(self):
        a = [1, 10, 23, 100, 101, 102, 321]
        b = [1, 24, 101, 102, 103, 203, 400]
        self.assertEqual(UnionSameLength(a,b), [1, 101, 102])
        b = [320, 321, 322]
        self.assertEqual(UnionSameLength(a,b), [321])
        b = [105, 106, 107, 108]
        self.assertEqual(UnionSameLength(a,b), [])
    
    def test_UnionLessLength(self):
        a = [2, 10]
        b = [1, 10, 23, 100, 101, 102, 321]
        self.assertTrue(UnionLessLength(a,b), [10])
        a = [2, 10, 102]
        self.assertTrue(UnionLessLength(a,b), [10, 102])


if __name__ == "__main__":
    unittest.main()
