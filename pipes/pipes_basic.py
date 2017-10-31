# https://www.python-course.eu/pipes.php

# os.popen call gives a file-like interface, for reading the outputs of spawned
# shell commands

import os 

for line in os.popen('dir'):
    print(line.rstrip())  # files in the directory

# os.system simply runs a shell command, but os.popen also connects to its streams;
print(os.system('dir'))   # 0
 

