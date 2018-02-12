
# MAIN SOURCE:
# https://pymotw.com/2/operator/

# USEFUL LINKS:
# https://pymotw.com/2/operator/

# GENERAL INFORMATION:

# Functional programming using iterators occasionally requires creating
# small functions for simple expressions. Sometimes these can be expressed
# as lambda functions, but some operations do not need to be implemented
# with custom functions at all. The operator module defines functions that
# correspond to built-in operations for arithmetic and comparison, as well
# as sequence and dictionary operations.

from operator import *

print('-' * 10 + "# 1. Logical operators" + '-' * 10)

print('-' * 10 + "# 2. Comparison operators" + '-' * 10)

print('-' * 10 + "# 3. Arithmetic operators" + '-' * 10)

a = -1
b = 5.0
c = 2
d = 6

print("Arithmetic:")
print('add(a, b) : %s' % add(a, b))
print('pow(a, b) : %s' % pow(c, d))


print('-' * 10 + "# 4. Sequence operators" + '-' * 10)

print('-' * 10 + "# 5. In-place Operators" + '-' * 10)

print('-' * 10 + "# 6. Attribute and Item 'Getters'" + '-' * 10)

print('-' * 10 + "# 7. Combining Operators and Custom Classes" + '-' * 10)

print('-' * 10 + "# 8. Type Checking" + '-' * 10)



