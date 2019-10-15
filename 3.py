import re

print("Enter text: ")
x = input()
print(re.sub('([A-Z][a-z]+)', '[anonymized]', x))
