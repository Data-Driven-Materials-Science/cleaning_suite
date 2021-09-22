import os
import sys

name = ""
# print [name for name in os.listdir("../../helper_functions") if os.path.isdir(name)]

print(os.listdir("../../helper_functions"))

for name in os.listdir("../../helper_functions"):
    if os.path.isdir("../../helper_functions/" + name):
        print(os.path.abspath(name))

exit(0)
