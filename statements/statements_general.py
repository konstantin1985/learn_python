print('-' * 10 + "A1" + '-' * 10)

# In other words, you can chain together only simple statements,
# like assignments, prints, and function calls. Compound statements like if tests and
# while loops must still appear on lines of their own
a = 1; b = 2; print(a + b)

# To make this work, you simply have to enclose
# part of your statement in a bracketed pair-parentheses (()), square brackets ([]), or
# curly braces ({}). Use parentheses (anything can be in them), not \ symbol
mylist = [1111,
          2222,
          3333]

# This allows us to code single-line if statements, single-line while and for loops, and
# so on. Here again, though, this will work only if the body of the compound statement
# itself does not contain any compound statements.
x = 2
y = 1
if x > y: print(x)
# if x > y: print(x) print(y) # don't work

