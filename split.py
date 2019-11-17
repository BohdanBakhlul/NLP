import re

print("Enter text to split: ")
data = input()
print(re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]{2,2}\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', "\n", data)) #regex for splitting
