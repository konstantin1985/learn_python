# Note that all of these literals produce integer objects in program code; they are just
# alternative syntaxes for specifying values. The built-in calls hex(I), oct(I), and
# bin(I) convert an integer to its representation string in these three bases, and
# int(str, base) converts a runtime string to an integer per a given base.

# Variuos bases
if 0xB == 11 == 0o13 == 0b1011:
    print "Correct"  # Correct 
    
# Convert string to base N number
a = "101"
print str(int(a,2))            # 5
print str(int(a,10))           # 101
print(oct(64),hex(64),bin(64)) # ('0100', '0x40', '0b1000000')

print('%o, %x, %x, %X' % (64, 64, 255, 255)) # 100, 40, ff, FF

# Division true and floor
print 6/5            # 1, in Python 3.x it will be 1.2
print 6/5.0          # 1.2
print 6//5.0         # 1.0

# You don't need to predeclare variables in Python, but they must have been assigned at
# least once before you can use them. In practice, this means you have to initialize coun-
# ters to zero before you can add to them, initialize lists to an empty list before you can
# append to them, and so on.

# Formats to display numbers
num1 = 1/3.0
num2 = 1/5.0
print(num1)                        # 0.333333333333
print("%e" % num1)                 # 3.333333e-01
print("%4.2f" % num1)              # 0.33
print("a=%f,b=%f" % (num1,num2))   # a=0.333333,b=0.200000
print("{0:4.2f}".format(num1))     # 0.33

# Both of these convert arbitrary objects to their string representations: repr (and the
# default interactive echo) produces results that look as though they were code; str (and
# the print operation) converts to a typically more user-friendly format if available. Some
# objects have both - a str for general use, and a repr with extra details.

print(repr('spam'))  # 'spam'
print(str('spam'))   # spam

# You can use other comparisons in chained tests, but the resulting expressions can be-
# come nonintuitive unless you evaluate them the way Python does. 
print(1 == 2 < 3)    # False, same as: 1 == 2 and 2 < 3

# This stems from the fact that floating-point numbers cannot represent some values
# exactly due to their limited number of bits-a fundamental issue in numeric program-
# ming not unique to Python.

print(1.1 + 2.2 == 3.3)           # False
print(1.1 + 2.2)                  # 3.3000000000000003
print(int(1.1 + 2.2) == int(3.3)) # True

# Truncate vs. floor
print(5 // 2.0, 5 // -2.0)        # (2.0, -3.0) - // is a floor division
import math
print(math.trunc(-2.5))           # -2.0



