


# MAIN SOURSE:
# [Hattem][XXXX] Mastering Python p.86


# USEFUL LINKS:

# 1) To see how sorted and sort works:
#    https://developers.google.com/edu/python/sorting

# 2) Links on Y Combinator
#    http://hisham.hm/2011/04/04/understanding-at-last-the-y-combinator-a-programmer-friendly-perspective/
#    https://gist.github.com/houtianze/b72ab26bb652a4a8241387f188e60a3b
#    https://math.stackexchange.com/questions/51246/can-someone-explain-the-y-combinator
#    http://mvanier.livejournal.com/2897.html

# GENERAL INFORMATION:


print('-' * 10 + "# 1. Lambda functions" + '-' * 10) 

# The lambda statement in Python is simply an anonymous function.
# Due to the syntax, it is slightly more limited than regular 
# functions, but a lot can be done through it. As always though,
# readability counts, so generally it is a good idea to keep it 
# as simple as possible. One of the more common use cases is the
# sort key for the sorted function.

class Spam(object):
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.value)

spams = [Spam(5), Spam(2), Spam(4), Spam(1)]

# For more complex custom sorting, sorted() takes an optional 
# "key=" specifying a "key" function that transforms each element
# before comparison. The key function takes in 1 value and returns
# 1 value, and the returned "proxy" value is used for the comparisons
# within the sort.

# spam is input, spam.value is output
sorted_spams = sorted(spams, key = lambda spam: spam.value)
 
print(spams)
# [<Spam: 5>, <Spam: 2>, <Spam: 4>, <Spam: 1>]

print(sorted_spams)
# [<Spam: 1>, <Spam: 2>, <Spam: 4>, <Spam: 5>]

# While the function could have been written separately or the
# __cmp__ method of Spam could have been overwritten in this case,
# in many cases, this is an easy way to get a quick sort function
# as you would want it.

# It's not that the regular function would be verbose, but by using
# an anonymous function, you have a small advantage; you are not
# contaminating your local scope with an extra function.

# In my opinion, the only valid use case for lambda functions is as
# anonymous functions used as function parameters, and preferably
# only if they are short enough to fit on a single line.

print('-' * 10 + "# 2. The Y combinator" + '-' * 10) 













print('-' * 10 + "# 2. Y Combinator" + '-' * 10)