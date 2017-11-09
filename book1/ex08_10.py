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
        self.beg = 0                   # beginning of the queue, points to the first added element
        self.end = 0                   # end of the queue, points where we'll add the next element
        self.length = length           # length of the queue
        self.num = 0                   # current number of elements
        self.expandable = expandable   # can the queue be expanded?
    
    
    def Enqueue(self, a):
        #print("a: ", a)
        if self.num == self.length:
            # What to do when there is no more free space?
            if self.expandable:
                # Need to add free space AFTER CURRENT END
                self.queue[self.end:self.end] = [None] * self.length
                self.beg += self.length
                self.length *= 2
            else:  
                raise BaseException
        
        # Continue to add where we stopped
        self.queue[self.end] = a
        self.end = (self.end + 1) % self.length   # circular with new length, if the array was expanded
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
    
    
    def test_SimpleQueueExpandable(self):
        q = SimpleQueue(2, True)
        q.Enqueue(1)
        q.Enqueue(2)
        print("q01: ", q.queue)                       # ('q01: ', [1, 2])
        print("B:", q.beg, "E:", q.end, "N:", q.num)  # ('B:', 0, 'E:', 0, 'N:', 2)
        # So next element will be placed at index 0 (E)
        q.Enqueue(3)
        # No problem, we expand the queue starting from E element
        # (add 2 empty spaces at index 0 (because E:0) - before all elements)
        # So we basically expand the nonexistent space into [None None] 
        # Then put '3' into index 0 (E:0 from the previous step as expected)
        print("q02: ", q.queue)                       # ('q01: ', [3, None, 1, 2])
        print("B:", q.beg, "E:", q.end, "N:", q.num)  # ('B:', 2, 'E:', 1, 'N:', 3)
        self.assertEqual(q.Size(), 3)
        self.assertEqual(q.Dequeue(), 1)
        self.assertEqual(q.Dequeue(), 2)
        self.assertEqual(q.Dequeue(), 3)
        self.assertEqual(q.Size(), 0)
    
        
    
    '''
    def test_SimpleQueueExpandableCircle(self):
        q = SimpleQueue(2, True)
        print("q01: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(1)
        print("q02: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(2)
        print("q03: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 1)
        print("q04: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 2)
        print("q05: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(3)
        print("q06: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 3)
        print("q07: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(4)
        print("q08: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(5)
        print("q09: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        q.Enqueue(6)
        print("q10: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 4)
        print("q11: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 5)
        print("q12: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
        self.assertEqual(q.Dequeue(), 6)
        print("q13: ", q.queue)
        print("B:", q.beg, "E:", q.end, "N:", q.num)
    ''' 
        # B - first added
        # E - add next element here (this index)
        
        #q01: [N N] B:0 E:0 N:0
        # enqueue(1)
        #q02: [1 N] B:0 E:1 N:1
        # enqueue(2)
        #q03: [1 2] B:0 E:0 N:2
        # dequeue()
        #q04: [1 2] B:1 E:0 N:1
        # dequeue()
        #q05: [1 2] B:0 E:0 N:0
        # enqueue(3)
        #q06: [3 2] B:0 E:1 N:1
        # dequeue()
        #q07: [3 2] B:1 E:1 N:0
        # enqueue(4)
        #q08: [3 4] B:1 E:0 N:1
        # enqueue(5)
        #q09: [5 4] B:1 E:1 N:2
        # enqueue(6)
        #q10: [5 6 N 4] B:3 E:2 N:3

if __name__ == "__main__":
    unittest.main()