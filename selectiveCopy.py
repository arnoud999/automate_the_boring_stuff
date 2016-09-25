import sys
import os
import re
import shutil


# Create variables
extensions = sys.argv[1].split()
newfolder = sys.argv[2]

# Create the folder if it doesn't exist
if not os.path.isdir(newfolder):
    os.mkdir(newfolder)

# Copy the files
for path, dirs, filenames in os.walk(os.curdir):
    for filename in filenames:
        filext = re.search(r'\.([a-z]{3})$', filename)
        if filext:
            if filext.group(1) in extensions:
                print(filename)
                shutil.copy(filename, newfolder)

