


print('-' * 10 + "A.4. Nested imports" + '-' * 10)

import import_files.myclient
print(import_files.myclient.mymod.countLines("module_coding_exercise_2.py"))

from import_files.myclient import mymod
print(import_files.myclient.mymod.countChars("module_coding_exercise_2.py"))


