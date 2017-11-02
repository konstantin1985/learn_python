# 8.10 Implement a circular queue

# A queue can be implemented using an array and two additional fields, the beginning
# and the end indices. This structure is sometimes referred to as a circular queue.
# Both enqueue and dequeue have O(1) time complexity. 
# If the array is fixed, there is a max number of entries that can be stored.
# If the array is dynamically resized, the total time for m combined
# enqueue and dequeue operations is O(m).

# Problem 8.10: Implement a queue API using an array for storing elements.
# Your API should include a constructor function, which takes as argument the capacity
# of the queue, enqueue, and dequeue functions, a size function, which returns the number of 
# elements stored, and implement dynamic resizing.


# Good explanation of the algorithm
# https://blog.labix.org/2010/12/23/efficient-algorithm-for-expanding-circular-buffers

import unittest


class SimpleQueue:
    
    def __init__(self, length, expandable = False):
        self.queue = [None] * length
        self.beg = 0                   # beginning of the queue, we get elements from here
        self.end = 0                   # end of the queue, we add elements here
        self.length = length           # length of the queue
        self.num = 0                   # current number of elements
        self.expandable = expandable   # can the queue be expanded?
        
    def Enqueue(self, a):
        if self.num == self.length:
            # What to do when there is no more free space?
            if self.expandable:
                raise BaseException
            else:  
                raise BaseException
        
        self.queue[self.end] = a
        self.end = (self.end + 1) % self.length   # circular
        self.num += 1                             # increase number of stored elements
        
    def Dequeue(self):
        if self.num == 0: raise BaseException
        rv = self.queue[self.beg]
        self.beg = (self.beg + 1) % self.length   # circular
        self.num -= 1                             # decrease number of stored elements
        return rv
    
    def Size(self):
        return self.num


class Ex8_10Test(unittest.TestCase):
    
    def test_SimpleQueueNonExpandable(self):
        q = SimpleQueue(3)
        self.assertRaises(BaseException, q.Dequeue)
        # Move q.beg and q.end by enqueue and dequeue
        q.Enqueue(1) 
        q.Enqueue(2)
        q.Dequeue()
        q.Dequeue()
        # Fill the queue
        q.Enqueue(3)
        q.Enqueue(4)
        q.Enqueue(5)
        self.assertEqual(q.Size(), 3)
        # Try to add one more element
        self.assertRaises(BaseException, q.Enqueue, 6)
        self.assertEqual(q.Dequeue(), 3)
        self.assertEqual(q.Dequeue(), 4)
        self.assertEqual(q.Dequeue(), 5)
        self.assertEqual(q.Size(), 0)
        self.assertRaises(BaseException, q.Dequeue)
   
        # [None None None] B:0 E:0 S:0
        # [1,   2,   None] B:0 E:2 S:2
        # [1,   2,   None] B:2 E:2 S:0
        # [4,   5,   3   ] B:2 E:2 S:3
        # [4,   5,   6, None, None, 3] B:5 E:3 S:3
        
        
        # [None None None] B:0 E:0 S:0
        # [1,   2,   3]    B:0 E:2 S:2
        # [1,   2,   3,   4, None, None] B:0 E:3 S:4
    
    def test_SimpleQueueExpandable(self):
        pass

        

if __name__ == "__main__":
    unittest.main()