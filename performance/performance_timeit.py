

# USEFUL LINKS:
# https://docs.python.org/2/library/timeit.html


# GENERAL DESCRIPTION:


import timeit

print("-" * 20 + "#1 timeit for functions" + "-" * 20)

# Just a reminder how timeit works with functions

def test():
    """Some test function"""
    L = []
    for i in range(100):
        L.append(i)

# To give the timeit module access to functions you define, you can pass a 
# setup parameter which contains an import statement:
print("Timeit function: ", timeit.timeit("test()", setup="from __main__ import test", number=10000))
# ('Timeit function: ', 0.13972115516662598)


print("-" * 20 + "#2 timeit for code snippets" + "-" * 20)

some_snippet = """

L = []
for i in range(100):
    L.append(i)

"""

print("Timeit snippet: ", min(timeit.repeat(some_snippet, number=1000, repeat=2)))
# ('Timeit snippet: ', 0.013598918914794922)