

# General loop format

# while test:
#    statements
#    if test: break       # Exit loop now, skip else if present
#    if test: continue    # Go to top of loop now, to test1
# else:
#     statements          # Run if we didn't hit a break

# Calculate whether y is a prime number

y = 7
x = y // 2 # No need to check for numbers greater than y // 2
while x > 1:
    if (y % x) == 0:
        print("y = %d isn't a prime, factor = %d" % (y, x))
        break
    x -= 1
else:
    print("y = %d is prime" % y)
    
# C assignments return the value assigned, but Python assignments are just statements,
# not expressions. This eliminates a notorious class of C errors: you can’t accidentally
# type = in Python when you mean ==. 