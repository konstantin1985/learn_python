

# MAIN SOURCE:
# Lutz, "Programming Python" Chapter 5

# USEFUL LINKS:
#
# 1) The Basics of Python Multithreading and Queues
#    https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
#
# 2) Python threads synchronization: Locks, RLocks, Semaphores, Conditions, Events and Queues
#    NEED TO GO THROUGH
#    https://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/comment-page-1/
#
# 3) Queue.Queue vs multiprocessing.Queue
#    https://stackoverflow.com/questions/925100/python-queue-multiprocessing-queue-how-they-behave
#
# 4) Using locks in the with statement
#    http://www.bogotobogo.com/python/Multithread/python_multithreading_Using_Locks_with_statement_Context_Manager.php
#   
# 5) Re-entrant lock   
#    https://stackoverflow.com/questions/5185568/python-conditional-with-lock-design
#    Just use a threading.RLock which is re-entrant meaning it can be acquired 
#    multiple times by the same thread.
#
# 5) Queue block   
#    https://docs.python.org/2/library/queue.html

# GENERAL INFORMATION:

# You can synchronize your threads' access to shared resources with locks,
# but you often don't have to. As mentioned, realistically scaled threaded
# programs are often structured as a set of producer and consumer threads, 
# which communicate by placing data on, and taking it off of, a shared queue.
# As long as the queue synchronizes access to itself, this automatically
# synchronizes the threads' interactions.

# The Python queue module implements this storage device. It provides a
# standard queue data structure-a first-in first-out (fifo) list of Python
# objects. Like normal lists, the queues provided by this module may contain
# any type of Python object.

# Unlike normal lists, though, the queue object is automatically controlled 
# with thread lock acquire and release operations, such that only one thread
# can modify the queue at any given point in time. Because of this, programs
# that use a queue for their cross-thread communication will be thread-safe
# and can usually avoid dealing with locks of their own for data passed 
# between threads.


print("-" * 20 + "# 1 Queue with the thread module" + "-" * 20)

numconsumers = 2
numproducers = 4
nummessages  = 4                                                       # Messages per producer to put


# Note The thread module has been renamed to _thread in Python 3. The 2to3 tool
# will automatically adapt imports when converting your sources to Python 3;
# however, you should consider using the high-level threading module instead.

import thread
import Queue 
import time

safeprint = thread.allocate_lock()                                     # Create a new lock object
dataQueue = Queue.Queue()                                              # Can be passed as an argument to producer()/consumer()                                          # Shared global, infinite size

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            # block is false: return an item if one is immediately available,
            # else raise the Empty exception (timeout is ignored in that case)
            data = dataQueue.get(block=False)
        except Queue.Empty:
            pass
        else:                                                          # No exception occurred 
            with safeprint:
                print('consumer', idnum, 'got =>', data)

# All of the objects provided by a module that has acquire() and release()
# methods can be used as context managers for a with statement. The acquire()
# method will be called when the block is entered, and release() will be 
# called when the block is exited 

# with some_lock:
#    # do something...

# is equivalent to

# some_lock.acquire()
# try:
#    # do something
# finally:
#    some_lock.release()

if __name__ == "__main__":
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))                        # (i,) is args
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers -1) * nummessages) + 1)                  # if threading, we could have used join()
    print('Main thread exit.')

    # OUTPUT:
    # ('consumer', 0, 'got =>', '[producer id=0, count=0]')
    # ('consumer', 1, 'got =>', '[producer id=0, count=1]')
    # ('consumer', 0, 'got =>', '[producer id=0, count=2]')
    # ('consumer', 1, 'got =>', '[producer id=0, count=3]')
    # ('consumer', 1, 'got =>', '[producer id=1, count=0]')
    # ('consumer', 0, 'got =>', '[producer id=1, count=1]')
    # ('consumer', 1, 'got =>', '[producer id=2, count=0]')
    # ('consumer', 0, 'got =>', '[producer id=1, count=2]')
    # ('consumer', 1, 'got =>', '[producer id=3, count=0]')
    # ('consumer', 0, 'got =>', '[producer id=2, count=1]')
    # ('consumer', 1, 'got =>', '[producer id=1, count=3]')
    # ('consumer', 0, 'got =>', '[producer id=3, count=1]')
    # ('consumer', 1, 'got =>', '[producer id=2, count=2]')
    # ('consumer', 1, 'got =>', '[producer id=2, count=3]')
    # ('consumer', 1, 'got =>', '[producer id=3, count=2]')
    # ('consumer', 0, 'got =>', '[producer id=3, count=3]')
    # Main thread exit.

print("-" * 20 + "# 2 Queue with the threading module" + "-" * 20)

# DAEMON THREADS

# In the alternative threading module, though, the program will not
# exit if any spawned threads are running, unless they are set to be
# daemon threads. Specifically, the entire program exits when only
# daemon threads are left. Threads inherit a default initial daemonic
# value from the thread that creates them. The initial thread of a 
# Python program is considered not daemonic, though alien threads 
# created outside this module's control are considered daemonic 
# (including some threads created in C code). To override inherited
# defaults, a thread object's daemon flag can be set manually. 

# In other words, nondaemon threads prevent program exit, and programs 
# by default do not exit until all threading-managed threads finish.

import threading

numconsumers = 2
numproducers = 4
nummessages  = 4                                                       # Messages per producer to put

safeprint = threading.Lock()
dataQueue = Queue.Queue()

def producer2(idnum, queue):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))
    
def consumer2(idnum, queue):
    while True:
        time.sleep(0.1)
        try:
            data = queue.get(block = False)
        except Queue.Empty:
            pass
        else:
            with safeprint: 
                print('consumer', idnum, 'got =>', data)
    
if __name__ == "__main__":
    
    for i in range(numconsumers):
        thread = threading.Thread(target = consumer2, args = (i, dataQueue))
        thread.daemon = True                                          # else cannot exit!!!
        thread.start()
        
    waitfor = []                                                      # list of threads, necessary for join()
    
    for i in range(numproducers):
        thread = threading.Thread(target = producer2, args = (i, dataQueue))
        waitfor.append(thread)
        thread.start()
        
    # Wait until all producers finish their production
    for thread in waitfor:
        thread.join()

    print('Main thread exit.')

    # OUTPUT:
    # ('consumer', 0, 'got =>', '[producer id=0, count=0]')
    # ('consumer', 1, 'got =>', '[producer id=0, count=1]')
    # ('consumer', 0, 'got =>', '[producer id=0, count=2]')
    # ('consumer', 1, 'got =>', '[producer id=0, count=3]')
    # ('consumer', 0, 'got =>', '[producer id=1, count=0]')
    # ('consumer', 1, 'got =>', '[producer id=1, count=1]')
    # ('consumer', 0, 'got =>', '[producer id=2, count=0]')
    # ('consumer', 1, 'got =>', '[producer id=1, count=2]')
    # ('consumer', 0, 'got =>', '[producer id=3, count=0]')
    # ('consumer', 0, 'got =>', '[producer id=1, count=3]')
    # ('consumer', 1, 'got =>', '[producer id=2, count=1]')
    # ('consumer', 1, 'got =>', '[producer id=2, count=2]')
    # ('consumer', 0, 'got =>', '[producer id=3, count=1]')
    # ('consumer', 0, 'got =>', '[producer id=2, count=3]')
    # ('consumer', 1, 'got =>', '[producer id=3, count=2]')
    # Main thread exit.

# ON QUEUE BLOCK PARAMETER:
# Remove and return an item from the queue. If optional args block is
# true and timeout is None (the default), block if necessary until an
# item is available. If timeout is a positive number, it blocks at most
# timeout seconds and raises the Empty exception if no item was available
# within that time. Otherwise (block is false), return an item if one is
# immediately available, else raise the Empty exception (timeout is 
# ignored in that case).

