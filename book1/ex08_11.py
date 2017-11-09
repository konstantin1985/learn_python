# Problem 8.11: Implement a queue using two unsigned integer-valued variables.
# Assume that the only elements pushed into the queue are integers in [0,9].
# Your program should work correctly when 0s are the only elements in the queue.
# What it the maximum number of elements that can be stored in the queue for it
# to operate correctly?

import unittest


class SimpleQueue:
    
    def __init__(self):
        self.queue = 0
        self.end = 0       # index in the integer where we'll add the next element
    
    def Enqueue(self, a):  # a is an integer in [0,9]
        if self.end > 63:
            raise BaseException
        self.queue = self.queue * 10 + a
        self.end += 1

    def Deque(self):
        if self.end == 0:
            raise BaseException
        self.end -= 1
        rv = self.queue // 10 ** self.end
        self.queue = self.queue % 10 ** self.end
        return rv


class Ex8_11Test(unittest.TestCase):
    
    def test_SimpleQueue(self):
        q = SimpleQueue()
        q.Enqueue(1)
        q.Enqueue(5)
        q.Enqueue(7)
        self.assertEqual(q.Deque(), 1)
        self.assertEqual(q.Deque(), 5)
        q.Enqueue(9)
        self.assertEqual(q.Deque(), 7)
        self.assertEqual(q.Deque(), 9)
        self.assertRaises(BaseException, q.Deque)
            

if __name__ == "__main__":
    unittest.main()
