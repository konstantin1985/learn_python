

# Access keys, values and items
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.keys()))    # ['eggs', 'spam', 'ham']
print(list(D.values()))  # [3, 2, 1]
print(list(D.items()))   # [('eggs', 3), ('spam', 2), ('ham', 1)]

# Fetching a nonexistent key is normally an error, but the get method returns a default
# value-None, or a passed-in default-if the key doesn't exist.
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D.get('spam'))       # 2
print(D.get('toast'))      # None, for non-existent keys
print(D.get('toast', 88))  # Return value 88 if the key isn't present
print(len(D))              # 3, still

# Update (concatenate) and pop (only by key) methods
D = {'spam': 2, 'ham': 1, 'eggs': 3}
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)                   # {'toast': 4, 'muffin': 5, 'eggs': 3, 'ham': 1, 'spam': 2}
D.pop('muffin')
D.pop('toast')
print(D)                   # {'eggs': 3, 'ham': 1, 'spam': 2}

# For loop for dictionaries.
# Same as for key in D.keys():
# 3    eggs
# 1    ham
# 2    spam 
D = {'spam': 2, 'ham': 1, 'eggs': 3}
for key in D:    
    print(str(D[key]) + '\t' + key)
    
# If we want to map another way, we can use items() method
table = {"First movie":    '1975',
         "Life of Brian":  '1979',
         "The meaning":    '1983'}
print(list(table.items()))  # [('The meaning', '1983'), ('Life of Brian', '1979'), ('First movie', '1975')]
# Find movie by year even if we have a dictionary with key = movie, not key = year
print([title for (title, year) in table.items() if year == '1975']) # ['First movie']

# Dictionaries can be used to implement sparse data structures
# If you would use lists they will be mostly empty
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
a = 2; b = 3; c = 4        # ; separates statements
print(Matrix[(a, b, c)])   # 88

# We can check presence of the element in 3 ways: if, try or get
if (2, 3, 5) in Matrix:
    print Matrix(2, 3, 5)
else:
    print(0)

Matrix.get((2, 3, 4), 0)   # 88
Matrix.get((2, 3, 5), 0)   # 0

# Move popular way to create dictionaries now
# dict(zip(keyslist, valueslist))
A = dict([('name', 'Bob'), ('age', 40)])   # {'age': 40, 'name': 'Bob'}
print(A)

# Provided all the key's values are the same initially, you can also 
# create a dictionary with this special form-simply pass
# in a list of keys and an initial value for all of the values (the default is None)
print(dict.fromkeys(['a', 'b'],0))         # {'a': 0, 'b': 0}

# In practice, dictionaries tend to be best for data with labeled components, as well as
# structures that can benefit from quick, direct lookups by name, instead of slower linear
# searches. As we've seen, they also may be better for sparse collections and collections
# that grow at arbitrary positions.

# To illustrate, a standard way to initialize a dictionary dynamically in both 2.X and 3.X
# is to combine its keys and values with zip, and pass the result to the dict call.
D = dict(zip(['a', 'b', 'c'], [1, 2, 3])) # {'a': 1, 'c': 3, 'b': 2}
print(D)
D = {k: v for (k,v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)                                  # {'a': 1, 'c': 3, 'b': 2}



print('-' * 10 + 'Exercises' + '-' * 10)

# 1. Dictionary keys (keys are all immutables, so tuple can be a key!)
D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)              # {1: 'a', 2: 'b', (1, 2, 3): 'c'}

# 2. Dictionary indexing
#How does this compare to out-of-bounds assignments and references for lists?
#Does this sound like the rule for variable names?
D = {}
D['a'] = 1
D['b'] = 2
D['c'] = 3
# print(D['d'])       # KeyError: 'd'
D['d'] = "spam"        
print(D)              # {'a': 1, 'c': 3, 'b': 2, 'd': 'spam'}





