

# Problem 6.15: Implement a function which takes a 2D array A and prints A in spiral order.


import unittest

def SimpleSpiral(A, B):

    N = len(A)

    # Recursion exit condition
    if N == 1:
        B.append(A[0][0])  # central element if matrix initially has odd N
        return
    if N == 0:
        return

    # Add all outer elements
    for i in range(N - 1):  # [1, 2]
        B.append(A[0][i])

    for i in range(N - 1):  # [3, 6]
        B.append(A[i][N - 1])

    for i in range(N-1):  # [9, 8]
        B.append(A[N - 1][N - 1 - i])

    for i in range(N-1):  # [7, 4]
        B.append(A[N - 1 - i][0])

    # IMPORTANT: remove outer layer of a matrix
    A = A[1:N-1]
    for i in range(len(A)):
        A[i] = A[i][1:N-1]

    # Recursive call
    SimpleSpiral(A, B)


class Ex6_15Test(unittest.TestCase):

    def test_SimpleSpiral(self):

        B = []
        SimpleSpiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]], B)
        self.assertEquals(B, [1, 2, 3, 6, 9, 8, 7, 4, 5])
        B = []
        SimpleSpiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], B)
        self.assertEquals(B, [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])


if __name__ == "__main__":
    unittest.main()