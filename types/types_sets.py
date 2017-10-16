



# Sets comprehension

print {x ** 2 for x in [1, 2, 3, 4]}  # set([16, 1, 4, 9])

# Sets can be used to isolate differences in lists, strings, and other iterable objects too-
# simply convert to sets and take the difference-though again the unordered nature of
# sets means that the results may not match that of the originals.

print set(dir(bytes)) - set(dir(bytearray)) # set(['__getslice__', 'format', '__mod__', '_formatter_field_name_split', 'encode', '__rmod__', '__getnewargs__', '_formatter_parser'])

# You can also use sets to perform order-neutral equality tests by converting to a set before
# the test, because order doesn't matter in a set.

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)                   # False
print(set(L1) == set(L2))         # True
print(sorted(L1) == sorted(L2))   # True

# Finally, sets are also convenient when you're dealing with large data sets (database
# query results, for example)-the intersection of two sets contains objects common to
# both categories, and the union contains all items in either set.

engineers = {'bob', 'sue', 'vic'}
managers = {'tom', 'sue'}

print('bob' in engineers)         # True
print(engineers & managers)       # set(['sue'])
print(managers - engineers)       # set(['tom'])
print(engineers > managers)       # False Are all managers engineers? (superset)
print({'bob', 'sue'} < engineers) # True


#
# 