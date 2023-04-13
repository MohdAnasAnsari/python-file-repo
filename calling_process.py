import os
import sys

program = "Python"
print("Process calling")
arguments = ["called_process.py"]

os.execvp(program, (program,) + tuple(arguments))
print("Good Bye")