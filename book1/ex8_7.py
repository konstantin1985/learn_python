# Problem 8.7: Design an algorithm to sort a stack S of numbers in descending order.
# The only operations allowed are push, pop, top (which returns the top of the stack without a pop),
# and empty. You cannot explicitly allocate memory outside of a few words.


# Apparently, recursion is required here
# It's not exactly memory-less, the internal memory for recursion is used

'''
http://www.geeksforgeeks.org/sort-a-stack-using-recursion/

We can use below algorithm to sort stack elements:

sortStack(stack S)
    if stack is not empty:
        temp = pop(S);  
        sortStack(S); 
        sortedInsert(S, temp);
Below algorithm is to insert element is sorted order:

sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)

'''

import unittest


def SortStack(st):
    if st:
        temp = st.pop()
        SortStack(st)
        # Starting from a single element we'll sequentially add all other elements
        SortedInsert(st, temp)


def SortedInsert(st, a):
    # Insert element 'a' in the ALREADY SORTER stack
    if not st or a > st[-1]:
        st.append(a)  # append and stop recursion
    else:
        temp = st.pop()
        SortedInsert(st, a)
        st.append(temp)


class Ex8_7Test(unittest.TestCase):
    
    def test_SortedInsert(self):
        
        st = []
        a = 4
        SortedInsert(st, a)
        self.assertEqual(st, [4])
        
        st = [1, 3, 5]
        a = 4
        SortedInsert(st, a)
        self.assertEqual(st, [1, 3, 4, 5])
    
        st = [1, 9, 10, 12, 40]
        a = 11
        SortedInsert(st, a)
        self.assertEqual(st, [1, 9, 10, 11, 12, 40])
    
    def test_SortStack(self):
        
        st = [1, 5, 2, 8, 4]
        SortStack(st)
        self.assertEqual(st, [1, 2, 4, 5, 8])

        
if __name__ == "__main__":
    unittest.main()