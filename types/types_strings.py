

# This is just the sort of thing that raw strings are useful for. If the letter r (uppercase or
# lowercase) appears just before the opening quote of a string, it turns off the escape
# mechanism. The result is that Python retains your backslashes literally, exactly as you
# type them.

# myfile = open(r'C:\new\text.dat', 'w')
# myfile = open('C:\\new\\text.dat', 'w')

S = 'abcdefghijklmnop'
print(S[1:10:2]) # bdfhj
print(S[::2])    # acegikmo
print(S[::-1])   # ponmlkjihgfedcba


# On the subject of conversions, it is also possible to convert a single character to its
# underlying integer code (e.g., its ASCII byte value)

print(ord('s'))  # 115
print(chr(115))  # s


print('%d %s %g you' % (1, 'spam', 4.0)) # 1 spam 4 you
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))  # 'spam, ham and eggs'
template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))

print('-' * 10 + "Exercises" + '-' * 10)

# 1. String indexing

# String is a collection of characters, but Python characters are one-character strings
S = "spam"
print(S[0])                  # s
print(S[0][0][0][0][0])      # s

# 
