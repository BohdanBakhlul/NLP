import re

name = '1.csv'
a = open(name, 'r')
for line in a:
    if (not bool(re.search(r'.*\; [0-9]\d*\; [0-9]\d*\s', line))):
        print("Error")
