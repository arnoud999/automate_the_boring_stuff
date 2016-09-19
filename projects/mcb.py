""" Gets from or writes to clipboard."""
import sys
import pyperclip
import shelve

getkeyword = ""
writekeyword = ""
delkeyword = ""

if len(sys.argv) == 1:
    print("Please provide at least 1 argument")
elif len(sys.argv) == 2:
    getkeyword = sys.argv[1]
elif len(sys.argv) == 3 and sys.argv[1] == "save":
    writekeyword = sys.argv[2]
elif len(sys.argv) == 3 and sys.argv[1] == "delete":
    delkeyword = sys.argv[2]
else:
    print("Invalid usage!")

# Get the dictionary
keydict = shelve.open('mcb')

# Save a new keyword
if writekeyword and writekeyword != "list":
    getclip = pyperclip.paste()
    keydict[writekeyword] = getclip
    print('Saved "%s" to key "%s"' % (getclip, writekeyword))

# Print an error if trying to write to list
if writekeyword == "list":
    print("Cannot write to keyword list!")

# Get a keyword
if getkeyword and getkeyword != "list":
    pyperclip.copy(keydict[getkeyword])
    print('Copied "%s" to clipboard' % keydict[getkeyword])

# List all keywords
if getkeyword == 'list':
    pyperclip.copy(", ".join(keydict.keys()))
    print(", ".join(keydict.keys()))

# Delete a keyword
if delkeyword:
    del keydict[delkeyword]
    print('Deleted %s' % delkeyword)

# Close the shelf file
keydict.close()
