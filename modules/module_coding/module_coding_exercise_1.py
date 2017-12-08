


import import_files.mymod

print(import_files.mymod.countLines("module_coding_exercise_1.py"))
print(import_files.mymod.countChars("module_coding_exercise_1.py"))
print(import_files.mymod.test("module_coding_exercise_1.py"))

from import_files.mymod import countLines
print(countLines("module_coding_exercise_1.py"))

from import_files.mymod import *
print(countChars("module_coding_exercise_1.py"))


