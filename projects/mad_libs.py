import sys
import re

# Open the file
if len(sys.argv) == 1:
    print('Please give an argument')
    sys.exit()

file = open(sys.argv[1])
text = file.read()

for word in re.split(r'[\s.]', text):
    if any(x.upper() in word for x in ['adjective', 'noun', 'adverb', 'verb']):
        print('Enter %s' % word)
        repl = input()
        text = re.sub(word.upper(), repl, text, count=1)

print(text)
file.close()
