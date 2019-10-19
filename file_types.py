import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('./sampleFiles/'):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files:", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files:", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("Yaml files:", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Python files:", file)

list_files()