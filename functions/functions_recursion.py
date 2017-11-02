


print('-' * 10 + "A.1. Summation with Recursion" + '-' * 10)

# When using recursion like this, each open level
# of call to the function has its own copy of the function's local scope on the runtime call
# stack-here, that means L is different in each level.

def mysum1(L):
    if not L:
        return 0
    else:
        return L[0] + mysum1(L[1:])
    
print(mysum1([1, 2, 3, 4, 5]))  # 15

# To achieve the same we can use a ternary expression

def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])

print(mysum2([1, 2, 3, 4, 5]))  # 15

# We can generalize for any summable type (there is no explicit + 0)

def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])

print(mysum3([1, 2, 3, 4, 5]))          # 15
print(mysum3(('spam', 'ham', 'eggs')))  # spamhameggs
# IndexError: list index out of range - doesn't work for empty input
# print(mysum3([]))

# Indirect recursion
# A function that calls another function, which calls back to its caller

def mysum4(L):
    # print('mysum4', L)
    if not L: return 0
    return nonempty(L)             # Call a function that calls me

def nonempty(L):
    # print('nonempty', L)
    return L[0] + mysum4(L[1:])    # Indirectly recursive

print(mysum4([1.1, 2.2, 3.3, 4.4]))  # 11.0 

print('-' * 10 + "A.2. Achieve the same with loops" + '-' * 10)

# With looping statements, we don't require a fresh copy of a local scope on the call stack
# for each iteration, and we avoid the speed costs associated with function calls in general

def mysum5(L):
    s = 0
    while L:
        s += L[0]
        L = L[1:]
    return s

print(mysum5([1.1, 2.2, 3.3, 4.4]))  # 11.0 

def mysum6(L):
    s = 0
    for l in L: s += l
    return s

print(mysum6([1.1, 2.2, 3.3, 4.4]))  # 11.0

print('-' * 10 + "A.3. Handling arbitrary structures" + '-' * 10)

# On the other hand, recursion-or equivalent explicit stack-based algorithms we'll meet
# shortly-can be required to traverse arbitrarily shaped structures. As a simple example
# of recursion's role in this context, consider the task of computing the sum of all the
# numbers in a nested sublists structure

# Nested looping statements do not suffice either, because the sublists may be nested 
# to arbitrary depth and in an arbitrary shape-there's no way to know how many nested 
# loops to code to handle all cases.

def sumtree1(L):
    total = 0
    print(L)
    for x in L:
        # If x is still a list - go deeper
        if isinstance(x, list):
            total += sumtree1(x)
        # L is list, but x is an element
        else:
            total += x
    return total
    
print(sumtree1([[[1, 2], 3], [3, 1], 1]))  # 11
print(sumtree1([1, [2, [3, [4, [5]]]]]))   # 15 (right-heavy)
print(sumtree1([[[[[1], 2], 3], 4], 5]))   # 15 (left-heavy)

print('-' * 10 + "A.4. Recursion versus queues and stacks" + '-' * 10)

# Python implements recursion by
# pushing information on a call stack at each recursive call, so it remembers where it must
# return and continue later. In fact, it's generally possible to implement recursive-style
# procedures without recursive calls, by using an explicit stack or queue of your own to
# keep track of remaining steps.

# Traverses the list in breadth-first fashion by levels, because it adds
# nested lists' contents to the end of the list, forming a first-in-first-out queue.

def sumtree2(L):                           # Breadth-first, explicit queue
    total = 0
    items = list(L)                        # Start with copy of the top level
    while items:                    
        front = items.pop()                # Fetch/delete front item
        if not isinstance(front, list):
            total += front
        else:
            items.extend(front)            # Append all to the nested list 
    return total

print(sumtree2([[[1, 2], 3], [3, 1], 1]))  # 11

# To emulate the traversal of the recursive call version more closely, 
# we can change it to perform depth-first traversal simply by adding
# the content of nested lists to the front of the list, forming 
# a last-in-first-out stack

def sumtree3(L):                           # Depth-first, explicit stack
    total = 0
    items = list(L)                        # Start with copy of top level
    while items:
        front = items.pop()                # Fetch/delete front item
        if not isinstance(front, list):
            total += front                 # Add numbers directly
        else:
            items[:0] = front              # Prepend all to the nested list
    return total

print(sumtree3([[[1, 2], 3], [3, 1], 1]))  # 11

print('-' * 10 + "A.5. Cycles, paths and stack limit" + '-' * 10)

# Neither the recursive call nor the explicit queue/stack examples in this
# section do anything about avoiding cycles-visiting a location already visited. That's
# not required here, because we're traversing strictly hierarchical list object trees. If data
# can be a cyclic graph, though, both these schemes will fail: the recursive call version
# will fall into an infinite recursive loop.

# To do better, the recursive call version could simply keep and pass a set, dictionary, or
# list of states visited so far and check for repeats as it goes.

# The maximum allowed setting can vary per platform.
import sys
print(sys.getrecursionlimit())  # 1000 
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())  # 10000


