import re
import os

# Ask for a pattern
pattern = r(input("Enter a pattern\n> "))
# Create a list of text files

filelist = []
for file in os.listdir(os.curdir):
    if re.search(r'.txt', file):
        filelist.append(file)

# Print matches
for file in filelist:
    with open(file) as f:
        text = f.read()
        for match in re.findall(pattern, text):
            print(match, "found in", file)
