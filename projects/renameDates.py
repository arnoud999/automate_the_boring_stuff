"""Renames files with American style dates to European style dates."""

import os
import shutil
import re

# Search for files
filelist = []
for file in os.listdir():
    if re.search(r'\d\d-\d\d-\d{4}', file):
        filelist.append(file)
        newfilename = re.sub(r'(\d\d)-(\d\d)-(\d{4})', r'\2-\1-\3', file)
        shutil.move(file, newfilename)

print("Moved", ", ".join(filelist))
