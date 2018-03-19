
# BASIC ARTICLE:

# Relative path in Linux - USE AS BASIC ARTICLE HERE
# http://teaching.idallen.com/cst8207/12f/notes/160_pathnames.html#dot-and-dot-dot-.-and-..







# USEFUL LINKS:

# Explanation of file descriptors:
# https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms


# Agnostic filr path on windows and linux (os.path.join)
# https://askubuntu.com/questions/350458/passing-a-file-location-to-python


# Slashes always separate name components. If a pathname starts with a slash,
# e.g. /etc/passwd, the nameless "ROOT" directory is what begins the pathname
# at the far left end. This top-most ROOT directory itself has no name. It is
# the starting point or the tree root of the entire hierarchical Unix/Linux
# file system tree.

# A pathname starting with a slash is called an absolute pathname. It always
# starts at the unique topmost file system ROOT directory.

# "/xxx" - starting from ROOT
# "./xxx" - staring from the current path
# "../xxx" - staring from the parent path
# "~/xxx" - starting from home directory
 
# Every Unix directory contains the name . (dot), which is a name that
# leads right back to the directory in which it is found.

# Every directory contains the name .. (dot dot), which is a name that
# leads to the unique parent directory of the directory in which it is found.

# The topmost ROOT directory is the only directory that is its own parent
 
# If a pathname ends in a directory name followed by a slash at the right end,
# e.g. /usr/bin/ or dir/, the self-referential name . (dot, or period) is
# assumed after the ending slash. In a directory, . refers to the directory
# itself. For example, all these are equivalent:
# $ ls /bin
# ...many names print here...
# $ ls /bin/
# ...same names print here...
# $ ls /bin/.
# ...same names print here...
# $ ls /bin///

# - Absolute pathnames start with a slash on the left, e.g. /etc/passwd
# - Relative pathnames do not start with a slash, e.g. etc/passwd
#   Relative pathnames start in the current working directory

# The current working directory can be displayed in shells using the pwd
# (print working directory) command.

# ls dir1                     # use this
# ls ./dir1                   # same, but unnecessary

# "./" can be used to work with tricky files "rm -r" - doesn't remove file named "-r".
# "rm ./-r" works  





