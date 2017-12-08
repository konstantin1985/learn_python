

# Problem 6.10: Given an array A of n elements and a permutation P, compute P(A) using only
# constant additional storage

import unittest

def PermutationSimple(A, P):
    # With additional storage
    B = [0] * len(A)
    for i in range(len(A)):
        B[P[i]] = A[i]
    return B

def PermutationMinus(A, P):
    # No additional storage B here

    for i in range(len(A)):
        if P[i] >= 0:
            tempi = i
            tempa = A[i]
            while True:

                # Save element in position next_tempi because we'll overwrite it
                next_tempi = P[tempi]
                next_tempa = A[next_tempi]
                A[next_tempi] = tempa

                P[tempi] -= len(P)  # Simply do P[tempi] *= 1 won't work because there is 0
                tempi = next_tempi
                tempa = next_tempa

                if tempi == i:
                    break

    # We played with P so now we must make it correct again
    # P is list -> mutable
    for i in range(len(P)):
        P[i] += len(P)

    return A


class Ex6_10Test(unittest.TestCase):

    def AuxiliaryFunction(self, f):
        self.assertEquals(f([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEquals(f([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]), [4, 3, 2, 1, 0])
        self.assertEquals(f([2, 1, 0], [2, 1, 0]), [0, 1, 2])
        self.assertEquals(f(['X', 'Y', 'Z', 'K', 'S'], [0, 2, 3, 1, 4]), ['X', 'K', 'Y', 'Z', 'S'])

    def test_PermutationSimple(self):
        self.AuxiliaryFunction(PermutationSimple)

    def test_PermutationMinus(self):
        self.AuxiliaryFunction(PermutationMinus)


if __name__ == "__main__":
    unittest.main()