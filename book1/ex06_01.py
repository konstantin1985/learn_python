# About sorting

# Problem 6.1: Write a function that takes an array A and an index i into A, and
# rearranges the elements such that all elements less that A[i] appear first,
# followed by elements equal to A[i], followed by elements greater than A[i].
# Your algorithm should have O(1) space complexity and O(|A|) time complexity.

import unittest

#|less->|equal->|don't know|<-more|
#              >>>

def Sort(A, i):

    # Need 3 pointer to keep 0(1) space
    less = 0
    equal = 0
    more = len(A) - 1

    pivot = A[i]

    while equal <= more:

        if A[equal] < pivot:
            temp = A[less]
            A[less] = A[equal]
            A[equal] = temp
            less += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            temp = A[more]
            A[more] = A[equal]
            A[equal] = temp
            more -= 1

    return A


class Ex6_1Test(unittest.TestCase):

    def test_Sort(self):
        print Sort([9, 8, 5, 3, 2], 2)  # [2, 3, 5, 8, 9]
        print Sort([8, 9, 5, 2, 3], 2)  # [3, 2, 5, 9, 8]
        print Sort([1, 2, 3, 4, 5], 4)  # [1, 2, 3, 4, 5]
        print Sort([5, 4, 3, 2, 1], 4)  # [1, 3, 2, 4, 5]
        print Sort([5, 4, 7, 8, 9], 4)  # [5, 4, 7, 8, 9]


if __name__ == "__main__":
    unittest.main()