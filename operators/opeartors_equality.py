
# https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

# == is an equality test. It checks whether the right hand side and the 
# left hand side are equal objects (according to their __eq__ or __cmp__ 
# methods.)

# is is an identity test. It checks whether the right hand side
# and the left hand side are the very same object. No method calls 
# are done, objects can't influence the is operation.


# https://stackoverflow.com/questions/5782203/python-difference-between-and-is-not

'''
is tests for object identity, but == tests for object value equality:

In [1]: a = 3424
In [2]: b = 3424

In [3]: a is b
Out[3]: False

In [4]: a == b
Out[4]: True
'''


# https://stackoverflow.com/questions/31026754/python-if-not-vs-if
# [not x == 'val'] vs [x != 'val']

'''
class Dummy(object):
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return True


>>> not Dummy() == Dummy()
False
>>> Dummy() != Dummy()
True
'''