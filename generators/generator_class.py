# class SomeIterable:
#     def __init__(...): ...  # On iter(): return self or supplemental object
#     def __next__(...): ...  # On next(): coded here, or in another class

# As the prior section suggested, these classes usually return their objects directly for
# single-iteration behavior, or a supplemental object with scan-specific state for multiple-
# scan support.

# Alternatively, a user-defined iterable class's method functions can sometimes use
# yield to transform themselves into generators, with an automatically created
# __next__ method—a common application of yield we'll meet in Chapter 30 that is
# both wildly implicit and potentially useful! A __getitem__ indexing method is also
# available as a fallback option for iteration, though this is often not as flexible as the
# __iter__ and __next__ scheme (but has advantages for coding sequences).

# The instance objects created from such a class are considered iterable and may be used
# in for loops and all other iteration contexts.

