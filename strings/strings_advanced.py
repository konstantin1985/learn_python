# -*- coding: utf-8 -*-

# MAIN SOURCE:
# Lutz "Learning Python" Chapter 37

# USEFUL LINKS:
# 
# 1) Raw strings r"..."
#    https://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-and-what-are-raw-string-literals
#



# GENERAL INFORMATION:

# The r doesn't change the type at all, it just changes how the string
# literal is interpreted. Without the r, backslashes are treated as escape
# characters. With the r, backslashes are treated as literal. Either way,
# the type is the same.


print("-" * 20 + "# 1 String Basics" + "-" * 20)



print("-" * 20 + "# 1.1 Character Encoding Schemes" + "-" * 20)

# The way characters are stored can vary, depending on what sort
# of character set must be recorded. When text is stored on files,
# for example, its character set determines its format.

# Character sets are standards that assign integer codes to individual
# characters so they can be represented in computer memory. The ASCII
# standard, for example, was created in the U.S., and it defines many
# U.S. programmers' notion of text strings. ASCII defines character
# codes from 0 through 127 and allows each character to be stored in 
# one 8-bit byte, only 7 bits of which are actually used.

# For example, the ASCII standard maps the character 'a' to the integer
# value 97 (0x61 in hex), which can be stored in a single byte in memory
# and files.

print(ord('a'))                                         # 'a' is a byte with binary value 97 in ASCII (and others)
print(chr(97))                                          # Binary value 97 stands for character 'a'

# Sometimes one byte per character isn't enough, though. Various symbols
# and accented characters, for instance, do not fit into the range of
# possible characters defined by ASCII. To accommodate special characters,
# some standards use all the possible values in an 8-bit byte, 0 through
# 255, to represent characters, and assign the values 128 through 255 
# (outside ASCII's range) to special characters.

# Still, some alphabets define so many characters that it is impossible
# to represent each of them as one byte. Unicode allows more flexibility. 
# Unicode text is sometimes referred to as "wide-character" strings, 
# because characters may be represented with multiple bytes if needed.

# For some encodings, the translation process is trivial-ASCII and Latin-1,
# for instance, map each character to a fixed-size single byte, so no
# translation work is required. For other encodings, the mapping can be
# more complex and yield multiple bytes per character, even for simple
# 8-bit forms of text.

# The widely used UTF-8 encoding, for example, allows a wide range of
# characters to be represented by employing a variable-sized number of
# bytes scheme. Character codes less than 128 are represented as a
# single byte; codes between 128 and 0x7ff (2047) are turned into 2
# bytes, where each byte has a value between 128 and 255; and codes above
# 0x7ff are turned into 3- or 4-byte sequences having values between 
# 128 and 255. This keeps simple ASCII strings compact, sidesteps byte 
# ordering issues, and avoids null (zero value) bytes that can cause 
# problems for C libraries and networking.

# Because their encodings' character maps assign characters to the same 
# codes for compatibility, ASCII is a subset of UTF-8. That is, a valid
# ASCII character string is also a valid UTF-8-encoded string. For example,
# every ASCII file is a valid UTF-8 file.

# Conversely, the UTF-8 encoding is binary compatible with ASCII, but only
# for character codes less than 128. UTF-8 simply allows for additional 
# characters.

# Other encodings allow for richer character sets in different ways. 
# UTF-16 and UTF-32, for example, format text with a fixed-size 2 and 4
# bytes per each character scheme, respectively, even for characters
# that could otherwise fit in a single byte. UTF-16/UTF-32 are incompatible
# with ASCII.

S = "ni"

print(S.encode('ascii'), S.encode('latin1'), S.encode('utf8'))
# ('ni', 'ni', 'ni')

print(S.encode('utf16'), len(S.encode('utf16')))
('\xff\xfen\x00i\x00', 6)

print(S.encode('utf32'), len(S.encode('utf32')))
('\xff\xfe\x00\x00n\x00\x00\x00i\x00\x00\x00', 12)

# ASCII, Latin-1, UTF-8, UTF-16, UTF-32 and many others-are considered
# to be Unicode. Unicode can be implemented by different character encodings.

print("-" * 20 + "# 1.2 How Python Stores Strings in Memory" + "-" * 20)

# The encodings above really only apply when text is stored or transferred
# externally, in files and other mediums. In memory, Python always stores
# decoded text strings in an encoding-neutral format, which may or may not
# use multiple bytes for each character. All text processing occurs in this
# uniform internal format. Text is translated to and from an encoding-specific
# format only when it is transferred to or from external text files, byte
# strings, or APIs with specific encoding requirements. Once in memory, 
# though, strings have no encoding. They are just the string object presented
# in this book

# Though irrelevant to your code, how Python actually stores text in memory:
# - Python 3.2 and earlier UTF-16
# - Python 3.3 and later, variable-length scheme with 1, 2, or 4 bytes per
#   character, depending on a string's content

# Unicode clearly requires us to think of strings in terms of characters,
# instead of bytes. This may be a bigger hurdle for programmers accustomed
# to the simpler ASCII-only world where each character mapped to a single
# byte, but that idea no longer applies, in terms of both the results of
# text string tools and physical character size.

# Today, both string content and length really correspond to Unicode code
# points-identifying ordinal numbers for characters. len returns the number
# of characters, not bytes; the string is probably larger in memory, and
# its characters may not fit in bytes anyhow.

# The key point here, though, is that encoding pertains mostly to files
# and transfers. Once loaded into a Python string, text in memory has no
# notion of an "encoding", and is simply a sequence of Unicode characters
# (a.k.a. code points) stored generically. In your script, that string is
# accessed as a Python string object.

print("-" * 20 + "# 1.3 Python's String Types" + "-" * 20)

# Python 2.X has a general string type for representing binary data and
# simple 8-bit text like ASCII, along with a specific type for representing
# richer Unicode text:
# - str for representing 8-bit text and binary data
# - unicode for representing decoded Unicode text

# By contrast, Python 3.X comes with three string object types-one for
# textual data and two for binary data:
# - str for representing decoded Unicode text (including ASCII)
# - bytes for representing binary data (including encoded text)
# - bytearray, a mutable flavor of the bytes type

# As mentioned earlier, bytearray is also available in Python 2.6 and 2.7,
# but it's simply a back-port from 3.X with less content-specific behavior
# and is generally considered a 3.X type.

# The main goal behind this change in 3.X was to merge the normal and Unicode
# string types of 2.X into a single string type that supports both simple and
# Unicode text: developers wanted to remove the 2.X string dichotomy and make
# Unicode processing more natural. Given that ASCII and other 8-bit text is
# really a simple kind of Unicode, this convergence seems logically sound.

# To achieve this, 3.X stores text in a redefined str type-an immutable
# sequence of characters (not necessarily bytes), which may contain either
# simple text such as ASCII whose character values fit in single bytes,
# or richer character set text such as UTF-8 whose character values may
# require multiple bytes. 

# Because Unicode strings are decoded from bytes, they cannot be used to
# represent bytes. To support processing of such truly binary data, a new 
# string type, bytes, also was introduced-an immutable sequence of 8-bit
# integers representing absolute byte values, which prints as ASCII
# characters when possible.

# To support processing of such truly binary data, a new string type, bytes,
# also was introduced-an immutable sequence of 8-bit integers representing
# absolute byte values, which prints as ASCII characters when possible.
# Python developers also added a bytearray type in 3.X. bytear ray is a
# variant of bytes that is mutable and so supports in-place changes.

# Although Python 2.X and 3.X offer much the same functionality, they
# package it differently. In fact, the mapping from 2.X to 3.X string
# types is not completely direct-2.X's str equates to both str and bytes
# in 3.X, and 3.X's str equates to both str and unicode in 2.X. Moreover,
# the mutability of 3.X's bytearray is unique.

# In practice, it boils down to the following: in 2.X, you will use str
# for simple text and binary data and unicode for advanced forms of text
# whose character sets don't map to 8-bit bytes; in 3.X, you'll use str
# for any kind of text (ASCII, Latin-1, and all other kinds of Unicode) 
# and bytes or bytearray for binary data. In practice, the choice is often
# made for you by the tools you use-especially in the case of file 
# processing tools.

print("-" * 20 + "# 1.4 Text and Binary Files" + "-" * 20)

# Python 3.X:

# Text files
#   When a file is opened in text mode, reading its data automatically
#   decodes its content and returns it as a str; writing takes a str
#   and automatically encodes it before transferring it to the file. 
#   Both reads and writes translate per a platform default or a 
#   provided encoding name.

# Binary files
#  When a file is opened in binary mode by adding a b (lowercase only)
#  to the mode-string argument in the built-in open call, reading its
#  data does not decode it in any way but simply returns its content
#  raw and unchanged, as a bytes object; writing similarly takes a
#  bytes object and transfers it to the file unchanged. Binary-mode
#  files also accept a bytearray object for the content to be written
#  to the file.

# Ultimately, the mode in which you open a file will dictate which
# type of object your script will use to represent its content:

# If you are processing image files, data transferred over networks, 
# packed binary data whose content you must extract, or some device
# data streams, chances are good that you will want to deal with it
# using bytes and binary-mode files.

# If instead you are processing something that is textual in nature,
# such as program output, HTML, email content, or CSV or XML files,
# you'll probably want to use str and text-mode files.

# Notice that the mode string argument to built-in function open 
# (its second argument) becomes fairly crucial in Python 3.X-its
# content not only specifies a file processing mode, but also implies
# a Python object type. Without the b, your file is processed in text
# mode, and you'll use str objects to represent its content in your
# script. For example, the modes rb, wb, and rb+ imply bytes; r, w+,
# and rt (the default) imply str.

# In Python 2.X, the same behavior is supported, but normal files
# created by open are used to access bytes-based data, and Unicode
# files opened with the codecs.open call are used to process Unicode
# text data.

print("-" * 20 + "# 2 Coding Basic Strings" + "-" * 20)

# Although there is no bytes type in Python 2.X (it has just the
# general str), it can usually run code that thinks there is-in 2.6
# and 2.7, the call bytes(X) is present as a synonym for str(X), and
# the new literal form b'...' is taken to be the same as the normal
# string literal '...'. 

print("-" * 20 + "# 2.1 Python 3.X String Literals" + "-" * 20)

# Python 3.X string objects originate when you call a built-in function
# such as str or bytes, read a file created by calling open (described
# in the next section), or code literal syntax in your script. For the
# latter, a new literal form, b'xxx' (and equivalently, B'xxx') is used
# to create bytes objects in 3.X, and you may create bytearray objects by
# calling the bytearray function, with a variety of possible arguments.

# More formally, in 3.X all the current string literal forms-'xxx', "xxx", 
# and triple- quoted blocks-generate a str; adding a b or B just before
# any of them creates a bytes instead. This new b'...' bytes literal is
# similar in form to the r'...' raw string used to suppress backslash escapes.

# A "raw string literal" r"..." is a slightly different syntax for a string literal,
# in which a backslash, \, is taken as meaning "just a backslash" (except when
# it comes right before a quote that would otherwise terminate the literal)
# -- no "escape sequences" to represent newlines, tabs, backspaces, form-feeds,
# and so on. In normal string literals, each backslash must be doubled up to 
# avoid being taken as the start of an escape sequence.

import sys

# Very important that it's Python 3.X

if sys.version_info >= (3, 0):
    
    B = b'spam'                                                # 3.X bytes literal make a bytes object (8-bit bytes)
    S = 'eggs'                                                 # 3.X str literal makes a Unicode text string
    
    print(type(B), type(S))                                    # <class 'bytes'> <class 'str'>
    print(B)                                                   # b'spam'
    print(S)                                                   # eggs

# The 3.X bytes object is actually a sequence of short integers, though it
# prints its content as characters whenever possible

    print(B[0], S[0])                                          # Indexing returns an int for bytes, str for str
    # 115 e
    print(B[1:], S[1:])                                        # Slicing makes another bytes or str object
    # b'pam' ggs
    print(list(B), list(S))                                    # bytes is really 8-bit small ints
    # [115, 112, 97, 109] ['e', 'g', 'g', 's']

    # Both are immutable
    # B[0] = 'x'                                               # TypeError: 'bytes' object does not support item assignment
    # S[0] = 'x'                                               # TypeError: 'str' object does not support item assignment
   
    # bytes prefix (b or B) works on single, double, triple quotes, raw
    B = B"""
    xxx
    yyy
    """
    print(B)                                                   # b'\n    xxx\n    yyy\n    '

# Python 2.X's u'xxx' and U'xxx' Unicode string literal forms were removed
# in Python 3.0 because they were deemed redundant-normal strings are
# Unicode in 3.X. To aid both forward and backward compatibility, though,
# they are available again as of 3.3, where they are treated as normal str
# strings.

    U = u"spam"                                                # 2.X Unicode literal accepted in 3.3+
    print(type(U))                                             # It is just str, but is backward compatible
    # <class 'str'>
    print(U[0])                                                # s
    print(list(U))                                             # ['s', 'p', 'a', 'm']

# These literals (u or U) are gone in 3.0 through 3.2, where you must use
# 'xxx' instead.

# Regardless of how text strings are coded in 3.X, though, they are all 
# Unicode, even if they contain only ASCII characters 

print("-" * 20 + "# 2.2 Python 2.X String Literals" + "-" * 20)

# All three of the 3.X string forms of the prior section can be coded in
# 2.X, but their meaning differs. As mentioned earlier, in Python 2.6
# and 2.7 the b'xxx' bytes literal is present for forward compatibility
# with 3.X, but is the same as 'xxx' and makes a str (the b is ignored),
# and bytes is just a synonym for str; as you've seen, in 3.X both of
# these address the distinct bytes type.

if sys.version_info < (3, 0):
    
    B = b"spam"                                                # 3.X bytes literal is just str in 2.6/2.7
    S = 'eggs'                                                 # str is a bytes/character sequence

    print(type(B), type(S))                                    # (<type 'str'>, <type 'str'>)
    print(B, S)                                                # ('spam', 'eggs')
    print(B[0], S[0])                                          # ('s', 'e')
    print(list(B), list(S))                                    # (['s', 'p', 'a', 'm'], ['e', 'g', 'g', 's'])
    
 
# In 2.X the special Unicode literal and type accommodates richer forms
# of text

    U = u"spam"                                                # 2.X Unicode literal makes a distinct type
    print(type(U))                                             # Works in 3.3 too, but is just a str there
    # <type 'unicode'>
    print(repr(U))                                             # u'spam' 
    print(repr(U[0]))                                          # u's'
    print(list(U))                                             # [u's', u'p', u'a', u'm']

print("-" * 20 + "# 2.3 String Type Conversions" + "-" * 20)

# IMPORTANT:
# encode - from string to bytes
# decode - from bytes to string

# Although Python 2.X allowed str and unicode type objects to be mixed
# in expressions (when the str contained only 7-bit ASCII text), 3.X draws
# a much sharper distinction-str and bytes type objects never mix automatically
# in expressions and never are converted to one another automatically when
# passed to functions. A function that expects an argument to be a str object
# won't generally accept a bytes, and vice versa.

# Because of this, Python 3.X basically requires that you commit to one type
# or the other, or perform manual, explicit conversions when needed:
# - str.encode() and bytes(S, encoding) translate a string to its raw bytes
#   form and create an encoded bytes from a decoded str in the process.
# - bytes.decode() and str(B, encoding) translate raw bytes into its string
#   form and create a decoded str from an encoded bytes in the process.

# These encode and decode methods (as well as file objects, described in
# the next section) use either a default encoding for your platform or an
# explicitly passed-in encoding name. For example, in Python 3.X:

if sys.version_info >= (3, 0):

    S = 'eggs'
    print(S.encode())                                          # str->bytes: encode text into raw bytes
    # b'eggs'
    print(bytes(S, encoding='ascii'))                          # str->bytes, alternative
    # b'eggs'

    B = b"spam"
    print(B.decode())                                          # bytes->str: decode raw bytes into text
    # spam
    print(str(B, encoding='ascii'))                            # bytes->str, alternative
    # spam
    
# Although calls to str do not require the encoding argument like bytes
# does, leaving it off in str calls does not mean that it defaults-instead,
# a str call without an encoding returns the bytes object's PRINT STRING,
# not its str CONVERTED FORM.
    
    print(sys.platform)                                        # Underlying platform
    # linux
    print(sys.getdefaultencoding())                            # Default encoding for str here
    # utf-8
    
    # bytes(S)                                                 # TypeError: string argument without an encoding
    
    print(str(B))                                              # str without encoding
    # "b'spam'"                                                # NOT CONVERSION! a print string
    print(len(str(B)))
    # 7
    
    print(str(B, encoding='ascii'))
    # spam
    print(len(str(B, encoding='ascii')))                       # Use encoding to convert to str
    # 4

# When in doubt, pass in an encoding name argument in 3.X, even if
# it may have a default.

if sys.version_info < (3, 0):

# Conversions are similar in Python 2.X, though 2.X's support for mixing
# string types in expressions makes conversions optional for ASCII text,
# and the tool names differ for the different string type model-conversions
# in 2.X occur between encoded str and decoded unicode, rather than 3.X's
# encoded bytes and decoded str.

    S = "spam"                                                 # 2.X type string conversion tools
    U = u"eggs"
    print(S, U)                                                
    # ('spam', u'eggs')
    print(unicode(S), str(U))                                  # 2.X converts str->uni, uni->str
    # (u'spam', 'eggs')
    print(S.decode(), U.encode())                              # versus 3.X byte->str, str->bytes
    # (u'spam', 'eggs')
    
print("-" * 20 + "# 3 Coding Unicode Strings" + "-" * 20)


print("-" * 20 + "# 3.1 Coding ASCII Text" + "-" * 20)

if sys.version_info >= (3, 0):

# ASCII text is a simple type of Unicode, stored as a sequence of byte values
# that represent characters.

    S = "XYZ"                                                  # A Unicode string of ASCII text
    print(S)
    # XYZ
    print(len(S))                                              # Three characters long
    # 3
    print([ord(c) for c in S])
    # [88, 89, 90]

# Normal 7-bit ASCII text like this is represented with one character per byte
# under each of the Unicode encoding schemes described earlier in this chapter.

    print(S.encode('ascii'))                                   # Values 0..127 in 1 byte (7 bits) each
    # b'XYZ'
    print(S.encode('latin-1'))                                 # Values 0..255 in 1 byte (8 bits) each
    # b'XYZ'
    print(S.encode('utf-8'))                                   # Values 0..127 in 1 byte, 128-2047 in 2, others 3 or 4
    # b'XYZ'

# In fact, the bytes objects returned by encoding ASCII text this way are 
# really a sequence of short integers, which just happen to print as ASCII
# characters when possible.

    print(S.encode('latin-1'))
    # b'XYZ'
    print(S.encode('latin-1')[0])
    # 88
    print(list(S.encode('latin-1')))
    # [88, 89, 90]

print("-" * 20 + "# 3.2 Encoding and Decoding Non-ASCII text" + "-" * 20)

if sys.version_info >= (3, 0):

# If we try to encode the prior section's non-ASCII text string into raw bytes
# using as ASCII, we'll get an error, because its characters are outside ASCII's
# 7-bit code point value range.

    S = '\u00c4\u00e8'                                         # Non-ASCII text string, two characters long
    print(S)
    # two strange letters
    len(S)
    # 2
    # S.encode('ascii')
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

    print(S.encode('latin-1'))                                 # 1 byte per character when encoded 
    # b'\xc4\xe8'
    print(S.encode('utf-8'))                                   # 2 bytes per character when encoded
    # b'\xc3\x84\xc3\xa8'
    print(len(S.encode('latin-1')))
    # 2
    print(len(S.encode('utf-8')))
    # 4
    
# Note that you can also go the other way, reading raw bytes from a file and
# decoding them back to a Unicode string. However, as we'll see later, the
# encoding mode you give to the open call causes this decoding to be done for
# you automatically on input (and avoids issues that may arise from reading
# partial character sequences when readingblocks of bytes).

    B = b'\xc4\xe8'                                            # Text encoded per Latin-1
    print(B)
    # b'\xc4\xe8'
    print(len(B))
    # 2
    print(B.decode('latin-1'))
    # two strange letters

    
print("-" * 20 + "# 3.3 Byte String Literals: Encoded Text" + "-" * 20)

if sys.version_info > (3, 0):
    
    B = b'A\xC4B\xE8C'                                         # bytes recognizes hex but not Unicode
    print(B)
    # b'A\xc4B\xe8C'
    
    B = b'A\u00C4B\U000000E8C'                                 # Escape sequences taken literally
    print(B)
    # b'A\\u00C4B\\U000000E8C'
    
# Second, bytes literals require characters either to be ASCII characters or,
# if their values are greater than 127, to be escaped.

print("-" * 20 + "# 3.4 Converting Encodings" + "-" * 20)

print("-" * 20 + "# 3.5 Coding Unicode Strings in Python 2.X" + "-" * 20)

# In 2.X, though the tools differ unicode is available in Python 2.X, but
# is a distinct type from str, supports most of the same operations, and 
# allows mixing of normal and Unicode strings when the str is all ASCII.

# In fact, you can essentially pretend 2.X's str is 3.X's bytes when it
# comes to decoding raw bytes into a Unicode string, as long as it's in
# the proper form.

if sys.version_info < (3, 0):
    
    S = 'A\xC4B\xE8C'
    print(S)
    # Some nonprintable characters: A�B�
    
    U = S.decode('latin-1')                                    # Decode bytes to Unicode text per latin-1  
    print(U)
    # AÄBèC

    # print(S.decode('utf-8'))
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xc4 in position 1: invalid continuation byte

# To code Unicode text, make a unicode object with the u'xxx' literal form
# (as mentioned, this literal is available again in 3.3, but superfluous in
# 3.X in general, since its normal strings support Unicode)

    U = u'A\xC4B\xE8C'                                         # Make Unicode string, hex escapes 
    print(U)
    # AÄBèC

# Once you've created it, you can convert Unicode text to different raw
# byte encodings, similar to encoding str objects into bytes objects in 3.X

    print(repr(U))
    # u'A\xc4B\xe8C'
    print(repr(U.encode('latin-1')))
    # 'A\xc4B\xe8C'
    print(U.encode('latin-1'))
    # A�B�

print("-" * 20 + "# 3.6 Mixing string types in 2.X" + "-" * 20)

# Like 3.X's str and bytes, 2.X's unicode and str share nearly identical
# operation sets, so unless you need to convert to other encodings you can
# often treat unicode as though it were str. One of the primary differences
# between 2.X and 3.X, though, is that uni code and non-Unicode str objects
# can be freely mixed in 2.X expressions-as long as the str is compatible 
# with the unicode object, Python will automatically convert it up to unicode.

if sys.version_info < (3, 0):

    print(repr(u'ab' + 'cd'))
    # u'abcd'

# By contrast, in 3.X, str and bytes never mix automatically and require 
# manual conversions.

print("-" * 20 + "# 4 Source File Character Set Encoding Declarations" + "-" * 20)

# The comment must be of this form and must appear as either the first or
# second line in your script in either Python 2.X or 3.X:
# -*- coding: latin-1 -*-
# When a comment of this form is present, Python will recognize strings
# represented natively in the given encoding.


print("-" * 20 + "# 5 Using 3.X bytes Objects" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 6 Using 3.X/2.6+ bytearray Objects" + "-" * 20)

# In Python 2.X, any string may be used to initialize (because any string
# is ASCII, not Unicode u"xxx")
if sys.version_info < (3, 0):
    S = 'spam'
    C = bytearray(S)
    print(repr(C))
    # bytearray(b'spam')

# In Python 3.X, an encoding name or byte string is required, because text
# and binary strings do not mix
if sys.version_info >= (3, 0):
    S = 'spam'
    # C = bytearray(S)
    # TypeError: string argument without an encoding
    C = bytearray(S, 'latin-1')  
    print(C)
    # bytearray(b'spam')

    # C[0] = 'x'                                               # Mutable but might assign ints, not strings              
    # TypeError: an integer is required

    C[0] = ord('x')
    print(C)
    # bytearray(b'xpam')
    
    C[1] = b'Y'[0]                                             # Or index a byte string
    print(C)
    # bytearray(b'xYam')

# Although all three Python 3.X string types can contain character values 
# and support many of the same operations, again, you should always:
# - Use str for textual data.
# - Use bytes for binary data.
# - Use bytearray for binary data you wish to change in place.


print("-" * 20 + "# 7 Using Text and Binary Files" + "-" * 20)

# This section expands on the impact of Python 3.X's string model on
# the file processing. The mode in which you open a file is crucial -
# it determines which object type you will use to represent the file's
# content in your script. Text mode implies str objects, and binary 
# mode implies bytes objects.

# Text-mode files interpret file contents according to a Unicode encoding
# - either the default for your platform, or one whose name you pass in.
# By passing in an encoding name to open, you can force conversions for
# various types of Unicode files.
 
# Binary-mode files instead return file content to you raw, as a sequence
# of integers representing byte values, with no encoding or decoding and
# no line-end translations.

# The second argument to open determines whether you want text or binary
# processing, just as it does in 2.X Python-adding a b to this string 
# implies binary mode (e.g., "rb" to read binary data files). The default
# mode is "rt"; this is the same as "r", which means text input (just as
# in 2.X).

# In 3.X, though, this mode argument to open also implies an object type
# for file content representation, regardless of the underlying platform
#-text files return a str for reads and expect one for writes, but binary
# files return a bytes for reads and expect one (or a bytearray) for writes.

print("-" * 20 + "# 7.1 Text File Basics" + "-" * 20)

# As long as you're processing basic text files (e.g., ASCII) and don't
# care about circumventing the platform-default encoding of strings, files
# in 3.X look and feel much as they do in 2.X (for that matter, so do 
# strings in general). The following, for instance, writes one line of text
# to a file and reads it back in 3.X, exactly as it would in 2.X (note that
# file is no longer a built-in name in 3.X, so it's perfectly OK to use it
# as a variable here)

# Basic text files (and strings) work the same as in 2.X
if sys.version_info >= (3, 0):

    file = open('files/temp', 'w')
    size = file.write('abc\n')                                 # Return number   
    file.close()                                               # Manual close to flush output buffers

    file = open('files/temp')                                  # Default mode is "r" (== "rt"): text input
    text = file.read()
    print(repr(text))
    # 'abc\n'
    print(text)
    # abc
    #

print("-" * 20 + "# 7.2 Text and Binary Modes in 2.X and 3.X" + "-" * 20)

# In Python 2.X, there is no major distinction between text and binary
# files-both accept and return content as str strings. The only major
# difference is that text files automatically map \n end-of-line characters
# to and from \r\n on WINDOWS, while binary files do not.

if sys.version_info < (3, 0):
    open('files/temp', 'w').write('abd\n')                     # Write in text mode: adds \r
    text = open('files/temp', 'r').read()                      # Read in text mode: drops \r
    print(repr(text))
    # 'abd\n'
    text = open('files/temp', 'rb').read()
    print(repr(text))
    # 'abd\r\n' - Windows
    # 'abd\n'   - Linux

# In Python 3.X, things are a bit more complex because of the distinction 
# between str for text data and bytes for binary data. Notice that we are
# required to provide a str for writing, but reading gives us a str or a
# bytes, depending on the open mode.

if sys.version_info >= (3, 0):
    num = open('files/temp', 'w').write('abc\n')               # Text mode output, provide a str
    print(num)
    # 4
    text = open('files/temp', 'r').read()                      # Text mode input, returns a str
    print(repr(text))
    # 'abc\n'
    text = open('files/temp', 'rb').read()                     # Binary mode input, returns a bytes
    print(text)
    # b'abc\r\n'- Windows
    # b'abc\n'  - Linux

# Notice how on Windows text-mode files translate the \n end-of-line 
# character to \r\n on output; on input, text mode translates the \r\n
# back to \n, but binary-mode files do not. This is the same in 2.X, and
# it's normally what we want-text files should for portability map 
# end-of-line markers to and from \n (which is what is actually present
# in files in Linux, where no mapping occurs), and such translations 
# should never occur for binary data (where end-of-line bytes are irrelevant).

# Now let's do the same again, but with a binary file. We provide a bytes
# to write in this case, and we still get back a str or a bytes, depending
# on the input mode.

    num = open('files/temp', 'wb').write(b'abc\n')
    print(num)
    # 4
    text = open('files/temp', 'r').read()
    print(repr(text))
    # 'abc\n'
    text = open('files/temp', 'rb').read()
    print(text)
    # b'abc\n' - Windows/Linux

# Note that the \n end-of-line character is not expanded to \r\n in binary
# - mode output - again, a desired result for binary data. Type requirements
# and file behavior are the same even if the data we're writing to the binary
# file is truly binary in nature.

# Binary-mode files always return contents as a bytes object, but accept
# either a bytes or bytearray object for writing; this naturally follows,
# given that bytearray is basically just a mutable variant of bytes.


print("-" * 20 + "# 7.3 Type and Content Mismatches in 3.X" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 8 Using Unicode Files" + "-" * 20)

# NEED TO LEARN

print("-" * 20 + "# 9 Other String Tool Changes in 3.X" + "-" * 20)

# NEED TO LEARN









